#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracteur de Contenu PowerPoint avec Analyse XML Directe
=========================================================

Implémentation complète selon l'architecture d'héritage PPTX avec analyse XML directe
pour extraire toutes les métadonnées de formatage (police, couleur, taille, etc.)
en respectant la cascade de styles : Thème -> Masque -> Layout -> Slide.

Ce script résout les limitations de python-pptx en accédant directement aux fichiers
XML dans l'archive .pptx et en implémentant la logique de résolution de styles.

Architecture:
- PPTXPackage: Navigation dans l'archive ZIP et résolution des relations
- Theme: Parse et cache les schémas de couleurs et polices du thème
- StyleResolver: Implémente la cascade de style pour résoudre les propriétés
- SlideExtractor: Orchestre l'extraction complète pour une diapositive

Auteur: Basé sur l'analyse architecturale OOXML approfondie
"""

import zipfile
import argparse
import json
import sys
import os
from typing import Dict, List, Any, Optional, Union
from pathlib import Path

try:
    from lxml import etree
    LXML_AVAILABLE = True
except ImportError:
    import xml.etree.ElementTree as etree
    LXML_AVAILABLE = False
    print("[WARNING] lxml non disponible, utilisation xml.etree (performances réduites)")


# =============================================================================
# CONSTANTES ET ESPACES DE NOMS OOXML
# =============================================================================

NAMESPACES = {
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'xml': 'http://www.w3.org/XML/1998/namespace'
}

# Unités de conversion OOXML
EMU_PER_POINT = 12700  # 1 point = 12700 EMUs (English Metric Units)
CENTIPOINTS_PER_POINT = 100  # 1 point = 100 centipoints

# Couleurs prédéfinies OOXML
PRESET_COLORS = {
    'black': '#000000',
    'white': '#FFFFFF',
    'red': '#FF0000',
    'green': '#00FF00',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
    'magenta': '#FF00FF',
    'cyan': '#00FFFF'
}


# =============================================================================
# CLASSE PPTXPackage - Navigation Archive et Relations
# =============================================================================

class PPTXPackage:
    """
    Navigateur pour l'archive .pptx et le graphe de relations OOXML.

    Gère l'accès de bas niveau à l'archive ZIP et la résolution des relations
    entre les différentes parties du document (slide -> layout -> master -> theme).
    """

    def __init__(self, pptx_path: str):
        """
        Initialise le package PPTX.

        Args:
            pptx_path: Chemin vers le fichier .pptx
        """
        self.pptx_path = Path(pptx_path)
        self.zip_file = zipfile.ZipFile(pptx_path, 'r')
        self._xml_cache = {}  # Cache pour éviter de parser plusieurs fois les mêmes fichiers
        self._relations_cache = {}

        # Charger les relations principales
        self._load_main_relations()

    def _load_main_relations(self):
        """Charge les relations principales du document."""
        try:
            main_rels = self.get_xml_tree('_rels/.rels')
            if main_rels is not None:
                self._relations_cache['main'] = self._parse_relations(main_rels)
        except:
            pass

    def get_xml_tree(self, part_name: str):
        """
        Lit et parse un fichier XML depuis l'archive avec mise en cache.

        Args:
            part_name: Nom de la partie XML dans l'archive

        Returns:
            Arbre XML parsé ou None si inexistant
        """
        if part_name in self._xml_cache:
            return self._xml_cache[part_name]

        try:
            with self.zip_file.open(part_name) as xml_file:
                if LXML_AVAILABLE:
                    tree = etree.parse(xml_file)
                else:
                    # Enregistrer les namespaces pour ElementTree
                    for prefix, uri in NAMESPACES.items():
                        etree.register_namespace(prefix, uri)
                    tree = etree.parse(xml_file)

                self._xml_cache[part_name] = tree
                return tree

        except (KeyError, etree.XMLSyntaxError) as e:
            print(f"[WARNING] Impossible de lire {part_name}: {e}")
            return None

    def _parse_relations(self, rels_tree) -> Dict[str, str]:
        """
        Parse un fichier .rels et retourne un mapping ID -> Target.

        Args:
            rels_tree: Arbre XML du fichier .rels

        Returns:
            Dict mapping relation ID vers target path
        """
        relations = {}

        # Le namespace pour les fichiers .rels est différent
        rels_ns = "http://schemas.openxmlformats.org/package/2006/relationships"

        if LXML_AVAILABLE:
            # lxml avec namespace
            rels = rels_tree.xpath('//pr:Relationship', namespaces={'pr': rels_ns})
        else:
            # ElementTree fallback
            root = rels_tree.getroot()
            rels = root.findall(f'.//{{{rels_ns}}}Relationship')

        for rel in rels:
            rel_id = rel.get('Id')
            target = rel.get('Target')
            rel_type = rel.get('Type')
            if rel_id and target:
                relations[rel_id] = target

        return relations

    def get_slide_layout_part(self, slide_part_name: str) -> Optional[str]:
        """
        Trouve la partie layout d'une slide donnée.

        Args:
            slide_part_name: Nom de la partie slide (ex: 'ppt/slides/slide1.xml')

        Returns:
            Nom de la partie layout ou None
        """
        # Construire le nom du fichier .rels correspondant
        rels_name = slide_part_name.replace('.xml', '.xml.rels').replace('ppt/slides/', 'ppt/slides/_rels/')

        rels_tree = self.get_xml_tree(rels_name)
        if rels_tree is None:
            return None

        # Le namespace pour les fichiers .rels
        rels_ns = "http://schemas.openxmlformats.org/package/2006/relationships"

        # Chercher directement la relation de type slideLayout
        if LXML_AVAILABLE:
            rel_elements = rels_tree.xpath('//pr:Relationship[contains(@Type, "slideLayout")]', namespaces={'pr': rels_ns})
        else:
            root = rels_tree.getroot()
            rel_elements = root.findall(f'.//{{{rels_ns}}}Relationship')
            rel_elements = [rel for rel in rel_elements if 'slideLayout' in rel.get('Type', '')]

        for rel_elem in rel_elements:
            target = rel_elem.get('Target')
            if target:
                # Résoudre le chemin relatif depuis slides vers slideLayouts
                return f"ppt/slideLayouts/{target.split('/')[-1]}"

        return None

    def get_slide_master_part(self, layout_part_name: str) -> Optional[str]:
        """
        Trouve la partie master d'un layout donné.

        Args:
            layout_part_name: Nom de la partie layout

        Returns:
            Nom de la partie master ou None
        """
        rels_name = layout_part_name.replace('.xml', '.xml.rels').replace('ppt/slideLayouts/', 'ppt/slideLayouts/_rels/')

        rels_tree = self.get_xml_tree(rels_name)
        if rels_tree is None:
            return None

        # Le namespace pour les fichiers .rels
        rels_ns = "http://schemas.openxmlformats.org/package/2006/relationships"

        # Chercher directement la relation de type slideMaster
        if LXML_AVAILABLE:
            rel_elements = rels_tree.xpath('//pr:Relationship[contains(@Type, "slideMaster")]', namespaces={'pr': rels_ns})
        else:
            root = rels_tree.getroot()
            rel_elements = root.findall(f'.//{{{rels_ns}}}Relationship')
            rel_elements = [rel for rel in rel_elements if 'slideMaster' in rel.get('Type', '')]

        for rel_elem in rel_elements:
            target = rel_elem.get('Target')
            if target:
                # Résoudre le chemin relatif depuis slideLayouts vers slideMasters
                return f"ppt/slideMasters/{target.split('/')[-1]}"

        return None

    def get_theme_part(self, master_part_name: str) -> Optional[str]:
        """
        Trouve la partie theme d'un master donné.

        Args:
            master_part_name: Nom de la partie master

        Returns:
            Nom de la partie theme ou None
        """
        rels_name = master_part_name.replace('.xml', '.xml.rels').replace('ppt/slideMasters/', 'ppt/slideMasters/_rels/')

        rels_tree = self.get_xml_tree(rels_name)
        if rels_tree is None:
            return None

        # Le namespace pour les fichiers .rels
        rels_ns = "http://schemas.openxmlformats.org/package/2006/relationships"

        # Chercher directement la relation de type theme
        if LXML_AVAILABLE:
            rel_elements = rels_tree.xpath('//pr:Relationship[contains(@Type, "theme")]', namespaces={'pr': rels_ns})
        else:
            root = rels_tree.getroot()
            rel_elements = root.findall(f'.//{{{rels_ns}}}Relationship')
            rel_elements = [rel for rel in rel_elements if 'theme' in rel.get('Type', '')]

        for rel_elem in rel_elements:
            target = rel_elem.get('Target')
            if target:
                # Résoudre le chemin relatif depuis slideMasters vers theme
                return f"ppt/theme/{target.split('/')[-1]}"

        return None

    def close(self):
        """Ferme l'archive ZIP."""
        if self.zip_file:
            self.zip_file.close()


# =============================================================================
# CLASSE Theme - Schémas de Couleurs et Polices
# =============================================================================

class Theme:
    """
    Parse et met en cache les schémas de couleurs et polices du thème.

    Le thème définit les palettes de base qui sont ensuite référencées
    sémantiquement dans toute la présentation.
    """

    def __init__(self, theme_tree):
        """
        Initialise le thème depuis son arbre XML.

        Args:
            theme_tree: Arbre XML du fichier theme.xml
        """
        self.tree = theme_tree
        self.colors = self._parse_color_scheme()
        self.fonts = self._parse_font_scheme()

    def _parse_color_scheme(self) -> Dict[str, str]:
        """
        Parse le schéma de couleurs <a:clrScheme> et extrait les couleurs.

        Returns:
            Dict mapping nom couleur -> valeur hex
        """
        colors = {}

        if self.tree is None:
            return colors

        try:
            if LXML_AVAILABLE:
                color_scheme = self.tree.xpath('//a:clrScheme', namespaces=NAMESPACES)
            else:
                color_scheme = self.tree.findall(f'.//{{{NAMESPACES["a"]}}}clrScheme')

            if not color_scheme:
                return colors

            scheme = color_scheme[0]

            # Liste des couleurs standard du thème
            color_names = ['dk1', 'lt1', 'dk2', 'lt2', 'accent1', 'accent2',
                          'accent3', 'accent4', 'accent5', 'accent6', 'hlink', 'folHlink']

            for color_name in color_names:
                if LXML_AVAILABLE:
                    color_elements = scheme.xpath(f'a:{color_name}', namespaces=NAMESPACES)
                else:
                    color_elements = scheme.findall(f'{{{NAMESPACES["a"]}}}{color_name}')

                if color_elements:
                    color_elem = color_elements[0]
                    hex_color = self._extract_color_value(color_elem)
                    if hex_color:
                        colors[color_name] = hex_color

        except Exception as e:
            print(f"[WARNING] Erreur parsing color scheme: {e}")

        return colors

    def _parse_font_scheme(self) -> Dict[str, str]:
        """
        Parse le schéma de polices <a:fontScheme> et extrait les polices.

        Returns:
            Dict mapping type police -> nom police
        """
        fonts = {}

        if self.tree is None:
            return fonts

        try:
            if LXML_AVAILABLE:
                font_scheme = self.tree.xpath('//a:fontScheme', namespaces=NAMESPACES)
            else:
                font_scheme = self.tree.findall(f'.//{{{NAMESPACES["a"]}}}fontScheme')

            if not font_scheme:
                return fonts

            scheme = font_scheme[0]

            # Police majeure (titres)
            if LXML_AVAILABLE:
                major_fonts = scheme.xpath('.//a:majorFont/a:latin', namespaces=NAMESPACES)
            else:
                major_fonts = scheme.findall(f'.//{{{NAMESPACES["a"]}}}majorFont/{{{NAMESPACES["a"]}}}latin')

            if major_fonts:
                fonts['major'] = major_fonts[0].get('typeface', 'Calibri')

            # Police mineure (corps de texte)
            if LXML_AVAILABLE:
                minor_fonts = scheme.xpath('.//a:minorFont/a:latin', namespaces=NAMESPACES)
            else:
                minor_fonts = scheme.findall(f'.//{{{NAMESPACES["a"]}}}minorFont/{{{NAMESPACES["a"]}}}latin')

            if minor_fonts:
                fonts['minor'] = minor_fonts[0].get('typeface', 'Calibri')

        except Exception as e:
            print(f"[WARNING] Erreur parsing font scheme: {e}")

        return fonts

    def _extract_color_value(self, color_element) -> Optional[str]:
        """
        Extrait la valeur hexadécimale d'un élément couleur.

        Args:
            color_element: Élément XML contenant une définition de couleur

        Returns:
            Valeur hexadécimale ou None
        """
        try:
            # sRGB Color
            if LXML_AVAILABLE:
                srgb_colors = color_element.xpath('.//a:srgbClr', namespaces=NAMESPACES)
            else:
                srgb_colors = color_element.findall(f'.//{{{NAMESPACES["a"]}}}srgbClr')

            if srgb_colors:
                val = srgb_colors[0].get('val')
                if val:
                    return f"#{val.upper()}"

            # System Color
            if LXML_AVAILABLE:
                sys_colors = color_element.xpath('.//a:sysClr', namespaces=NAMESPACES)
            else:
                sys_colors = color_element.findall(f'.//{{{NAMESPACES["a"]}}}sysClr')

            if sys_colors:
                val = sys_colors[0].get('lastClr') or sys_colors[0].get('val')
                if val:
                    return f"#{val.upper()}"

        except:
            pass

        return None

    def get_color(self, scheme_color_name: str) -> Optional[str]:
        """
        Obtient la valeur hex d'une couleur de thème.

        Args:
            scheme_color_name: Nom de la couleur (ex: 'accent1')

        Returns:
            Valeur hexadécimale ou None
        """
        color = self.colors.get(scheme_color_name)

        # Couleurs par défaut communes si non trouvées dans le thème
        if color is None:
            default_colors = {
                'tx1': '#FFFFFF',  # Texte principal (blanc)
                'tx2': '#000000',  # Texte secondaire (noir)
                'bg1': '#000000',  # Arrière-plan principal
                'bg2': '#FFFFFF',  # Arrière-plan secondaire
            }
            color = default_colors.get(scheme_color_name)

        return color

    def get_font(self, font_scheme_name: str) -> Optional[str]:
        """
        Obtient le nom d'une police de thème.

        Args:
            font_scheme_name: Type de police ('major' ou 'minor')

        Returns:
            Nom de la police ou None
        """
        return self.fonts.get(font_scheme_name)


# =============================================================================
# CLASSE StyleResolver - Cascade de Styles OOXML
# =============================================================================

class StyleResolver:
    """
    Implémente la cascade de style OOXML pour résoudre les propriétés de formatage.

    Suit la hiérarchie : Slide -> Layout -> Master -> Theme
    pour chaque propriété de formatage (police, couleur, taille, etc.).
    """

    def __init__(self, slide_tree, layout_tree, master_tree, theme: Theme):
        """
        Initialise le résolveur de styles.

        Args:
            slide_tree: Arbre XML de la slide
            layout_tree: Arbre XML du layout
            master_tree: Arbre XML du master
            theme: Objet Theme parsé
        """
        self.slide_tree = slide_tree
        self.layout_tree = layout_tree
        self.master_tree = master_tree
        self.theme = theme
        self.nsmap = NAMESPACES

    def resolve_text_properties(self, run_element, paragraph_element, shape_element, placeholder_idx: Optional[int] = None, placeholder_type: Optional[str] = None) -> Dict[str, Any]:
        """
        Résout toutes les propriétés de texte pour un run donné.

        Args:
            run_element: Élément <a:r> du segment de texte
            paragraph_element: Élément <a:p> du paragraphe parent
            shape_element: Élément <p:sp> de la forme parente
            placeholder_idx: Index du placeholder si applicable

        Returns:
            Dict avec toutes les propriétés de formatage résolues
        """
        properties = {
            'font_name': None,
            'font_size': None,
            'bold': None,
            'italic': None,
            'underline': None,
            'color': None,
            'alignment': None,
            'vertical_alignment': None,
            'margin_left': None,
            'margin_right': None,
            'margin_top': None,
            'margin_bottom': None
        }

        # Résoudre chaque propriété via la cascade
        properties['font_name'] = self._resolve_font_name(run_element, paragraph_element, placeholder_idx, placeholder_type)
        properties['font_size'] = self._resolve_font_size(run_element, paragraph_element, placeholder_idx, placeholder_type)
        properties['bold'] = self._resolve_bold(run_element, paragraph_element, placeholder_idx, placeholder_type)
        properties['italic'] = self._resolve_italic(run_element, paragraph_element, placeholder_idx, placeholder_type)
        properties['underline'] = self._resolve_underline(run_element, paragraph_element, placeholder_idx, placeholder_type)
        properties['color'] = self._resolve_color(run_element, paragraph_element, placeholder_idx, placeholder_type)
        properties['alignment'] = self._resolve_alignment(paragraph_element, placeholder_idx, placeholder_type)

        # Propriétés de shape/text frame
        if shape_element is not None:
            margins = self._resolve_margins(shape_element)
            properties.update(margins)
            properties['vertical_alignment'] = self._resolve_vertical_alignment(shape_element)

        return properties

    def _resolve_font_name(self, run_element, paragraph_element, placeholder_idx: Optional[int], placeholder_type: Optional[str] = None) -> Optional[str]:
        """Résout le nom de la police via la cascade d'héritage."""

        # 1. Vérifier formatage direct sur le run
        if run_element is not None:
            if LXML_AVAILABLE:
                rpr = run_element.xpath('.//a:rPr/a:latin', namespaces=self.nsmap)
            else:
                rpr = run_element.findall(f'.//{{{self.nsmap["a"]}}}rPr/{{{self.nsmap["a"]}}}latin')

            if rpr:
                typeface = rpr[0].get('typeface')
                if typeface:
                    return self._resolve_font_reference(typeface)

        # 2. Vérifier propriétés par défaut du paragraphe
        if paragraph_element is not None:
            if LXML_AVAILABLE:
                def_rpr = paragraph_element.xpath('.//a:pPr/a:defRPr/a:latin', namespaces=self.nsmap)
            else:
                def_rpr = paragraph_element.findall(f'.//{{{self.nsmap["a"]}}}pPr/{{{self.nsmap["a"]}}}defRPr/{{{self.nsmap["a"]}}}latin')

            if def_rpr:
                typeface = def_rpr[0].get('typeface')
                if typeface:
                    return self._resolve_font_reference(typeface)

        # 3. Vérifier styles du layout (priorité sur master)
        if self.layout_tree is not None:
            layout_font = self._get_layout_text_style_property(placeholder_idx, placeholder_type, 'font_name')
            if layout_font:
                return layout_font

        # 4. Vérifier styles du master
        if self.master_tree is not None:
            master_font = self._get_master_text_style_property(placeholder_idx, placeholder_type, 'font_name')
            if master_font:
                return master_font

        # 5. Valeur par défaut
        return self.theme.get_font('minor') if self.theme else 'Calibri'

    def _resolve_font_size(self, run_element, paragraph_element, placeholder_idx: Optional[int], placeholder_type: Optional[str] = None) -> Optional[float]:
        """Résout la taille de police en points."""

        # 1. Formatage direct sur le run
        if run_element is not None:
            if LXML_AVAILABLE:
                rpr = run_element.xpath('.//a:rPr', namespaces=self.nsmap)
            else:
                rpr = run_element.findall(f'.//{{{self.nsmap["a"]}}}rPr')

            if rpr and rpr[0].get('sz'):
                try:
                    return int(rpr[0].get('sz')) / CENTIPOINTS_PER_POINT
                except:
                    pass

        # 2. Propriétés par défaut du paragraphe
        if paragraph_element is not None:
            if LXML_AVAILABLE:
                def_rpr = paragraph_element.xpath('.//a:pPr/a:defRPr', namespaces=self.nsmap)
            else:
                def_rpr = paragraph_element.findall(f'.//{{{self.nsmap["a"]}}}pPr/{{{self.nsmap["a"]}}}defRPr')

            if def_rpr and def_rpr[0].get('sz'):
                try:
                    return int(def_rpr[0].get('sz')) / CENTIPOINTS_PER_POINT
                except:
                    pass

        # 3. Styles du layout (priorité sur master)
        if self.layout_tree is not None:
            layout_size = self._get_layout_text_style_property(placeholder_idx, placeholder_type, 'font_size')
            if layout_size:
                return layout_size

        # 4. Styles du master
        if self.master_tree is not None:
            master_size = self._get_master_text_style_property(placeholder_idx, placeholder_type, 'font_size')
            if master_size:
                return master_size

        # 5. Valeur par défaut
        return 18.0

    def _resolve_bold(self, run_element, paragraph_element, placeholder_idx: Optional[int], placeholder_type: Optional[str] = None) -> Optional[bool]:
        """Résout la propriété gras."""

        # 1. Formatage direct
        if run_element is not None:
            if LXML_AVAILABLE:
                rpr = run_element.xpath('.//a:rPr', namespaces=self.nsmap)
            else:
                rpr = run_element.findall(f'.//{{{self.nsmap["a"]}}}rPr')

            if rpr:
                bold_attr = rpr[0].get('b')
                if bold_attr is not None:
                    return bold_attr in ('1', 'true')

        # 2. Propriétés par défaut du paragraphe
        if paragraph_element is not None:
            if LXML_AVAILABLE:
                def_rpr = paragraph_element.xpath('.//a:pPr/a:defRPr', namespaces=self.nsmap)
            else:
                def_rpr = paragraph_element.findall(f'.//{{{self.nsmap["a"]}}}pPr/{{{self.nsmap["a"]}}}defRPr')

            if def_rpr:
                bold_attr = def_rpr[0].get('b')
                if bold_attr is not None:
                    return bold_attr in ('1', 'true')

        # 3. Styles du master
        if self.master_tree is not None:
            master_bold = self._get_master_text_style_property(placeholder_idx, placeholder_type, 'bold')
            # print(f"[DEBUG] Master bold for placeholder_type='{placeholder_type}', idx={placeholder_idx}: {master_bold}")
            if master_bold is not None:
                return master_bold

        return False

    def _resolve_italic(self, run_element, paragraph_element, placeholder_idx: Optional[int], placeholder_type: Optional[str] = None) -> Optional[bool]:
        """Résout la propriété italique."""

        # 1. Formatage direct
        if run_element is not None:
            if LXML_AVAILABLE:
                rpr = run_element.xpath('.//a:rPr', namespaces=self.nsmap)
            else:
                rpr = run_element.findall(f'.//{{{self.nsmap["a"]}}}rPr')

            if rpr:
                italic_attr = rpr[0].get('i')
                if italic_attr is not None:
                    return italic_attr in ('1', 'true')

        # 2. Propriétés par défaut du paragraphe
        if paragraph_element is not None:
            if LXML_AVAILABLE:
                def_rpr = paragraph_element.xpath('.//a:pPr/a:defRPr', namespaces=self.nsmap)
            else:
                def_rpr = paragraph_element.findall(f'.//{{{self.nsmap["a"]}}}pPr/{{{self.nsmap["a"]}}}defRPr')

            if def_rpr:
                italic_attr = def_rpr[0].get('i')
                if italic_attr is not None:
                    return italic_attr in ('1', 'true')

        # 3. Styles du master
        if placeholder_idx is not None and self.master_tree is not None:
            master_italic = self._get_master_text_style_property(placeholder_idx, placeholder_type, 'italic')
            if master_italic is not None:
                return master_italic

        return False

    def _resolve_underline(self, run_element, paragraph_element, placeholder_idx: Optional[int], placeholder_type: Optional[str] = None) -> Optional[bool]:
        """Résout la propriété souligné."""

        # 1. Formatage direct
        if run_element is not None:
            if LXML_AVAILABLE:
                rpr = run_element.xpath('.//a:rPr', namespaces=self.nsmap)
            else:
                rpr = run_element.findall(f'.//{{{self.nsmap["a"]}}}rPr')

            if rpr:
                underline_attr = rpr[0].get('u')
                if underline_attr is not None:
                    return underline_attr != 'none'

        # 2. Propriétés par défaut du paragraphe
        if paragraph_element is not None:
            if LXML_AVAILABLE:
                def_rpr = paragraph_element.xpath('.//a:pPr/a:defRPr', namespaces=self.nsmap)
            else:
                def_rpr = paragraph_element.findall(f'.//{{{self.nsmap["a"]}}}pPr/{{{self.nsmap["a"]}}}defRPr')

            if def_rpr:
                underline_attr = def_rpr[0].get('u')
                if underline_attr is not None:
                    return underline_attr != 'none'

        return False

    def _resolve_color(self, run_element, paragraph_element, placeholder_idx: Optional[int], placeholder_type: Optional[str] = None) -> Optional[str]:
        """Résout la couleur du texte."""

        # 1. Formatage direct dans les propriétés du run (a:rPr)
        if run_element is not None:
            if LXML_AVAILABLE:
                rpr = run_element.xpath('.//a:rPr', namespaces=self.nsmap)
            else:
                rpr = run_element.findall(f'.//{{{self.nsmap["a"]}}}rPr')

            if rpr:
                color = self._extract_color_from_element(rpr[0])
                if color:
                    return color

        # 2. Propriétés par défaut du paragraphe
        if paragraph_element is not None:
            if LXML_AVAILABLE:
                def_rpr = paragraph_element.xpath('.//a:pPr/a:defRPr', namespaces=self.nsmap)
            else:
                def_rpr = paragraph_element.findall(f'.//{{{self.nsmap["a"]}}}pPr/{{{self.nsmap["a"]}}}defRPr')

            if def_rpr:
                color = self._extract_color_from_element(def_rpr[0])
                if color:
                    return color

        # 3. Styles du layout (priorité sur master pour les couleurs spécifiques)
        if placeholder_idx is not None and self.layout_tree is not None:
            layout_color = self._get_layout_text_style_property(placeholder_idx, placeholder_type, 'color')
            if layout_color:
                return layout_color

        # 4. Styles du master (fallback pour couleurs génériques)
        if placeholder_idx is not None and self.master_tree is not None:
            master_color = self._get_master_text_style_property(placeholder_idx, placeholder_type, 'color')
            if master_color:
                return master_color

        return None

    def _resolve_alignment(self, paragraph_element, placeholder_idx: Optional[int], placeholder_type: Optional[str] = None) -> Optional[str]:
        """Résout l'alignement du paragraphe."""

        # 1. Propriétés directes du paragraphe
        if paragraph_element is not None:
            if LXML_AVAILABLE:
                ppr = paragraph_element.xpath('.//a:pPr', namespaces=self.nsmap)
            else:
                ppr = paragraph_element.findall(f'.//{{{self.nsmap["a"]}}}pPr')

            if ppr:
                algn = ppr[0].get('algn')
                if algn:
                    return self._map_alignment(algn)

        # 2. Styles du master
        if placeholder_idx is not None and self.master_tree is not None:
            master_align = self._get_master_text_style_property(placeholder_idx, placeholder_type, 'alignment')
            if master_align:
                return master_align

        return 'LEFT'  # Gauche par défaut

    def _resolve_margins(self, shape_element) -> Dict[str, Optional[float]]:
        """Résout les marges du text frame."""
        margins = {
            'margin_left': None,
            'margin_right': None,
            'margin_top': None,
            'margin_bottom': None
        }

        if shape_element is None:
            return margins

        try:
            if LXML_AVAILABLE:
                body_pr = shape_element.xpath('.//a:bodyPr', namespaces=self.nsmap)
            else:
                body_pr = shape_element.findall(f'.//{{{self.nsmap["a"]}}}bodyPr')

            if body_pr:
                bp = body_pr[0]

                # Convertir EMUs en points
                if bp.get('lIns'):
                    margins['margin_left'] = int(bp.get('lIns')) / EMU_PER_POINT
                if bp.get('rIns'):
                    margins['margin_right'] = int(bp.get('rIns')) / EMU_PER_POINT
                if bp.get('tIns'):
                    margins['margin_top'] = int(bp.get('tIns')) / EMU_PER_POINT
                if bp.get('bIns'):
                    margins['margin_bottom'] = int(bp.get('bIns')) / EMU_PER_POINT
        except:
            pass

        return margins

    def _resolve_vertical_alignment(self, shape_element) -> Optional[str]:
        """Résout l'alignement vertical du text frame."""

        if shape_element is None:
            return None

        try:
            if LXML_AVAILABLE:
                body_pr = shape_element.xpath('.//a:bodyPr', namespaces=self.nsmap)
            else:
                body_pr = shape_element.findall(f'.//{{{self.nsmap["a"]}}}bodyPr')

            if body_pr:
                anchor = body_pr[0].get('anchor')
                if anchor:
                    return self._map_vertical_alignment(anchor)
        except:
            pass

        return 'TOP'

    def _extract_color_from_element(self, element) -> Optional[str]:
        """Extrait la couleur d'un élément XML."""

        try:
            # Recherche couleur dans l'élément

            # sRGB Color
            if LXML_AVAILABLE:
                srgb = element.xpath('.//a:srgbClr', namespaces=self.nsmap)
            else:
                srgb = element.findall(f'.//{{{self.nsmap["a"]}}}srgbClr')

            if srgb:
                val = srgb[0].get('val')
                if val:
                    return f"#{val.upper()}"

            # Scheme Color (référence au thème)
            if LXML_AVAILABLE:
                scheme = element.xpath('.//a:schemeClr', namespaces=self.nsmap)
            else:
                scheme = element.findall(f'.//{{{self.nsmap["a"]}}}schemeClr')

            if scheme:
                val = scheme[0].get('val')
                if val and self.theme:
                    theme_color = self.theme.get_color(val)
                    if theme_color:
                        return theme_color

            # Preset Color
            if LXML_AVAILABLE:
                preset = element.xpath('.//a:prstClr', namespaces=self.nsmap)
            else:
                preset = element.findall(f'.//{{{self.nsmap["a"]}}}prstClr')

            if preset:
                val = preset[0].get('val')
                if val and val in PRESET_COLORS:
                    return PRESET_COLORS[val]

        except:
            pass

        return None

    def _resolve_font_reference(self, typeface: str) -> str:
        """Résout une référence de police du thème."""

        if typeface.startswith('+'):
            # Référence au thème
            if typeface == '+mn-lt' and self.theme:
                return self.theme.get_font('minor') or 'Calibri'
            elif typeface == '+mj-lt' and self.theme:
                return self.theme.get_font('major') or 'Calibri'

        return typeface

    def _get_master_text_style_property(self, placeholder_idx: Optional[int], placeholder_type: Optional[str], property_name: str):
        """
        Récupère une propriété de style depuis le master <p:txStyles>.

        Args:
            placeholder_idx: Index du placeholder
            property_name: Nom de la propriété ('font_name', 'font_size', etc.)

        Returns:
            Valeur de la propriété ou None
        """
        if self.master_tree is None:
            return None

        try:
            # Déterminer le type de style basé sur le placeholder_type et idx
            # Dans le template Premier Tech slide 11:
            # - placeholder_type "title": titre principal (titleStyle level 1)
            # - placeholder_idx 11: metadata/date (bodyStyle level 1)
            # - placeholder_idx 14: sous-titre (titleStyle level différent ou styles spéciaux)

            if placeholder_type == "title":
                # Les éléments de type "title" utilisent titleStyle
                style_section = 'titleStyle'
                level = 1
            elif placeholder_idx == 11:
                # Metadata/date - utiliser bodyStyle
                style_section = 'bodyStyle'
                level = 1
            elif placeholder_idx == 14:
                # Sous-titre - essayer titleStyle level 2 ou body level différent
                style_section = 'titleStyle'
                level = 2
            else:
                # Par défaut bodyStyle
                style_section = 'bodyStyle'
                level = 1

            # Debug info pour le style resolver (peut être activé si nécessaire)
            # print(f"[DEBUG] placeholder_idx={placeholder_idx}, placeholder_type={placeholder_type}, property={property_name}, style_section={style_section}, level={level}")

            # Construire le XPath pour trouver le style approprié
            if LXML_AVAILABLE:
                if level == 1:
                    xpath = f'.//p:txStyles/p:{style_section}/a:lvl1pPr/a:defRPr'
                elif level == 2:
                    xpath = f'.//p:txStyles/p:{style_section}/a:lvl2pPr/a:defRPr'
                else:
                    xpath = f'.//p:txStyles/p:{style_section}/a:lvl3pPr/a:defRPr'

                def_rpr_elements = self.master_tree.xpath(xpath, namespaces=self.nsmap)
            else:
                # ElementTree fallback
                if level == 1:
                    path = f'.//{{{self.nsmap["p"]}}}txStyles/{{{self.nsmap["p"]}}}{style_section}/{{{self.nsmap["a"]}}}lvl1pPr/{{{self.nsmap["a"]}}}defRPr'
                elif level == 2:
                    path = f'.//{{{self.nsmap["p"]}}}txStyles/{{{self.nsmap["p"]}}}{style_section}/{{{self.nsmap["a"]}}}lvl2pPr/{{{self.nsmap["a"]}}}defRPr'
                else:
                    path = f'.//{{{self.nsmap["p"]}}}txStyles/{{{self.nsmap["p"]}}}{style_section}/{{{self.nsmap["a"]}}}lvl3pPr/{{{self.nsmap["a"]}}}defRPr'

                def_rpr_elements = self.master_tree.findall(path)

            if not def_rpr_elements:
                return None

            def_rpr = def_rpr_elements[0]

            # Extraire la propriété demandée
            if property_name == 'font_size':
                sz = def_rpr.get('sz')
                if sz:
                    try:
                        return int(sz) / CENTIPOINTS_PER_POINT
                    except:
                        pass

            elif property_name == 'font_name':
                # Chercher la police latin
                if LXML_AVAILABLE:
                    latin_elements = def_rpr.xpath('.//a:latin', namespaces=self.nsmap)
                else:
                    latin_elements = def_rpr.findall(f'.//{{{self.nsmap["a"]}}}latin')

                if latin_elements:
                    typeface = latin_elements[0].get('typeface')
                    if typeface:
                        return self._resolve_font_reference(typeface)

            elif property_name == 'bold':
                bold_val = def_rpr.get('b')
                # print(f"[DEBUG] Bold found in master: b='{bold_val}' for {style_section} level {level}")
                return bold_val == '1'

            elif property_name == 'italic':
                return def_rpr.get('i') == '1'

            elif property_name == 'color':
                # Analyser solidFill/schemeClr pour la couleur
                if LXML_AVAILABLE:
                    scheme_clr = def_rpr.xpath('.//a:solidFill/a:schemeClr', namespaces=self.nsmap)
                else:
                    scheme_clr = def_rpr.findall(f'.//{{{self.nsmap["a"]}}}solidFill/{{{self.nsmap["a"]}}}schemeClr')

                if scheme_clr:
                    scheme_val = scheme_clr[0].get('val')
                    if scheme_val and self.theme:
                        return self.theme.get_color(scheme_val)

        except Exception as e:
            # print(f"[DEBUG] Erreur dans _get_master_text_style_property: {e}")
            pass

        return None

    def _get_layout_text_style_property(self, placeholder_idx: Optional[int], placeholder_type: Optional[str], property_name: str):
        """
        Récupère une propriété de style depuis le layout.

        Args:
            placeholder_idx: Index du placeholder
            placeholder_type: Type du placeholder
            property_name: Nom de la propriété ('font_name', 'font_size', etc.)

        Returns:
            Valeur de la propriété ou None
        """
        if self.layout_tree is None:
            return None

        try:
            # Chercher le placeholder correspondant dans le layout
            if LXML_AVAILABLE:
                # Chercher toutes les shapes avec placeholder
                ph_shapes = self.layout_tree.xpath('//p:sp[.//p:nvSpPr/p:nvPr/p:ph]', namespaces=self.nsmap)
            else:
                # ElementTree fallback
                root = self.layout_tree.getroot()
                ph_shapes = []
                for sp in root.findall(f'.//{{{self.nsmap["p"]}}}sp'):
                    ph_check = sp.findall(f'.//{{{self.nsmap["p"]}}}nvSpPr/{{{self.nsmap["p"]}}}nvPr/{{{self.nsmap["p"]}}}ph')
                    if ph_check:
                        ph_shapes.append(sp)

            for ph_shape in ph_shapes:
                # Vérifier si c'est le bon placeholder
                if LXML_AVAILABLE:
                    ph_elem = ph_shape.xpath('.//p:nvSpPr/p:nvPr/p:ph', namespaces=self.nsmap)[0]
                else:
                    ph_elem = ph_shape.findall(f'.//{{{self.nsmap["p"]}}}nvSpPr/{{{self.nsmap["p"]}}}nvPr/{{{self.nsmap["p"]}}}ph')[0]

                ph_type = ph_elem.get('type')
                ph_idx_str = ph_elem.get('idx')

                # Convertir l'index
                ph_idx = None
                if ph_idx_str and ph_idx_str != "None":
                    try:
                        ph_idx = int(ph_idx_str)
                    except:
                        pass

                # Vérifier si c'est le bon placeholder
                if ((placeholder_type == ph_type) and
                    (placeholder_idx == ph_idx)):

                    # Chercher les styles dans ce placeholder
                    if LXML_AVAILABLE:
                        def_rpr_elements = ph_shape.xpath('.//a:defRPr', namespaces=self.nsmap)
                    else:
                        def_rpr_elements = ph_shape.findall(f'.//{{{self.nsmap["a"]}}}defRPr')

                    if def_rpr_elements:
                        def_rpr = def_rpr_elements[0]

                        if property_name == 'font_size':
                            sz = def_rpr.get('sz')
                            if sz:
                                try:
                                    return int(sz) / CENTIPOINTS_PER_POINT
                                except:
                                    pass

                        elif property_name == 'font_name':
                            # Chercher la police latin
                            if LXML_AVAILABLE:
                                latin_elements = def_rpr.xpath('.//a:latin', namespaces=self.nsmap)
                            else:
                                latin_elements = def_rpr.findall(f'.//{{{self.nsmap["a"]}}}latin')

                            if latin_elements:
                                typeface = latin_elements[0].get('typeface')
                                if typeface:
                                    return self._resolve_font_reference(typeface)

                        elif property_name == 'bold':
                            bold_val = def_rpr.get('b')
                            return bold_val == '1'

                        elif property_name == 'italic':
                            return def_rpr.get('i') == '1'

                        elif property_name == 'color':
                            # Analyser solidFill/schemeClr pour la couleur
                            if LXML_AVAILABLE:
                                scheme_clr = def_rpr.xpath('.//a:solidFill/a:schemeClr', namespaces=self.nsmap)
                            else:
                                scheme_clr = def_rpr.findall(f'.//{{{self.nsmap["a"]}}}solidFill/{{{self.nsmap["a"]}}}schemeClr')

                            if scheme_clr:
                                scheme_val = scheme_clr[0].get('val')
                                if scheme_val and self.theme:
                                    layout_color = self.theme.get_color(scheme_val)
                                    if layout_color:
                                        return layout_color

        except Exception as e:
            # print(f"[DEBUG] Erreur dans _get_layout_text_style_property: {e}")
            pass

        return None

    def _map_alignment(self, algn: str) -> str:
        """Mappe les valeurs d'alignement OOXML vers des noms lisibles."""
        mapping = {
            'l': 'LEFT',
            'ctr': 'CENTER',
            'r': 'RIGHT',
            'just': 'JUSTIFY'
        }
        return mapping.get(algn, 'LEFT')

    def _map_vertical_alignment(self, anchor: str) -> str:
        """Mappe les valeurs d'alignement vertical OOXML."""
        mapping = {
            't': 'TOP',
            'ctr': 'MIDDLE',
            'b': 'BOTTOM'
        }
        return mapping.get(anchor, 'TOP')


# =============================================================================
# CLASSE SlideExtractor - Orchestrateur Principal
# =============================================================================

class SlideExtractor:
    """
    Orchestre l'extraction complète des métadonnées pour une diapositive.

    Combine la logique d'héritage agnostique avec l'analyse XML directe
    pour produire des JSON complets avec toutes les métadonnées de formatage.
    """

    def __init__(self, package: PPTXPackage, slide_part_name: str):
        """
        Initialise l'extracteur pour une slide donnée.

        Args:
            package: Package PPTX ouvert
            slide_part_name: Nom de la partie slide à extraire
        """
        self.package = package
        self.slide_part_name = slide_part_name

        # Charger la chaîne d'héritage complète
        self.slide_tree = package.get_xml_tree(slide_part_name)

        layout_part = package.get_slide_layout_part(slide_part_name)
        self.layout_tree = package.get_xml_tree(layout_part) if layout_part else None

        master_part = package.get_slide_master_part(layout_part) if layout_part else None
        self.master_tree = package.get_xml_tree(master_part) if master_part else None

        theme_part = package.get_theme_part(master_part) if master_part else None
        theme_tree = package.get_xml_tree(theme_part) if theme_part else None
        self.theme = Theme(theme_tree) if theme_tree else None

        # Initialiser le résolveur de styles
        self.style_resolver = StyleResolver(
            self.slide_tree, self.layout_tree, self.master_tree, self.theme
        )

    def extract_metadata(self) -> Dict[str, Any]:
        """
        Extrait toutes les métadonnées de la slide avec formatage complet.

        Returns:
            Dict avec métadonnées complètes incluant formatage détaillé
        """
        if self.slide_tree is None:
            return {"error": "Impossible de charger la slide"}

        # Métadonnées de base
        slide_number = self._extract_slide_number()
        layout_name = self._extract_layout_name()

        result = {
            "slide_number": slide_number,
            "layout_name": layout_name,
            "extraction_method": "xml_direct_analysis_with_inheritance",
            "shapes": []
        }

        # Extraire toutes les formes avec formatage complet
        shapes = self._extract_all_shapes()

        # Appliquer la logique de classification (éviter données parasites)
        filtered_shapes = self._filter_populated_content(shapes)

        result["shapes"] = filtered_shapes
        result["total_shapes"] = len(filtered_shapes)

        return result

    def _extract_slide_number(self) -> int:
        """Extrait le numéro de la slide depuis le nom de fichier."""
        try:
            import re
            match = re.search(r'slide(\d+)\.xml', self.slide_part_name)
            return int(match.group(1)) if match else 1
        except:
            return 1

    def _extract_layout_name(self) -> str:
        """Extrait le nom du layout."""

        if self.layout_tree is None:
            return "Unknown Layout"

        try:
            root = self.layout_tree.getroot()

            if LXML_AVAILABLE:
                csldes = root.xpath('.//p:cSld', namespaces=NAMESPACES)
            else:
                csldes = root.findall(f'.//{{{NAMESPACES["p"]}}}cSld')

            if csldes:
                name = csldes[0].get('name')
                if name:
                    return name

        except:
            pass

        return "Unknown Layout"

    def _extract_all_shapes(self) -> List[Dict[str, Any]]:
        """Extrait toutes les formes de la slide avec leur formatage."""

        shapes = []

        if self.slide_tree is None:
            return shapes

        try:
            root = self.slide_tree.getroot()

            if LXML_AVAILABLE:
                shape_elements = root.xpath('.//p:sp', namespaces=NAMESPACES)
            else:
                shape_elements = root.findall(f'.//{{{NAMESPACES["p"]}}}sp')

            for i, shape_elem in enumerate(shape_elements):
                shape_data = self._extract_shape_data(shape_elem, i + 1)
                if shape_data:
                    shapes.append(shape_data)

        except Exception as e:
            print(f"[WARNING] Erreur extraction formes: {e}")

        return shapes

    def _extract_shape_data(self, shape_element, shape_index: int) -> Optional[Dict[str, Any]]:
        """Extrait les données complètes d'une forme."""

        try:
            # Données de base
            shape_data = {
                "name": self._get_shape_name(shape_element),
                "shape_id": shape_index,
                "type": "placeholder" if self._is_placeholder(shape_element) else "shape",
                "position": self._get_shape_position(shape_element)
            }

            # Si c'est un placeholder, ajouter les métadonnées
            if self._is_placeholder(shape_element):
                placeholder_info = self._get_placeholder_info(shape_element)
                shape_data.update(placeholder_info)

            # Extraire le contenu texte avec formatage complet
            text_content = self._extract_text_with_formatting(shape_element)
            if text_content:
                shape_data["text"] = text_content["text"]
                shape_data.update(text_content["formatting"])

            return shape_data

        except Exception as e:
            print(f"[WARNING] Erreur extraction forme {shape_index}: {e}")
            return None

    def _extract_text_with_formatting(self, shape_element) -> Optional[Dict[str, Any]]:
        """Extrait le texte avec toutes les métadonnées de formatage."""

        try:
            if LXML_AVAILABLE:
                txbody = shape_element.xpath('.//p:txBody', namespaces=NAMESPACES)
            else:
                txbody = shape_element.findall(f'.//{{{NAMESPACES["p"]}}}txBody')

            if not txbody:
                return None

            # Obtenir le texte brut
            if LXML_AVAILABLE:
                paragraphs = txbody[0].xpath('.//a:p', namespaces=NAMESPACES)
            else:
                paragraphs = txbody[0].findall(f'.//{{{NAMESPACES["a"]}}}p')

            full_text = ""
            formatting = {}

            if paragraphs:
                # Prendre le premier paragraphe pour le formatage de référence
                para = paragraphs[0]

                # Obtenir le texte de tous les runs
                if LXML_AVAILABLE:
                    runs = para.xpath('.//a:r', namespaces=NAMESPACES)
                else:
                    runs = para.findall(f'.//{{{NAMESPACES["a"]}}}r')

                for run in runs:
                    if LXML_AVAILABLE:
                        t_elements = run.xpath('.//a:t', namespaces=NAMESPACES)
                    else:
                        t_elements = run.findall(f'.//{{{NAMESPACES["a"]}}}t')

                    for t_elem in t_elements:
                        if t_elem.text:
                            full_text += t_elem.text

                # Résoudre le formatage en analysant tous les runs
                if runs:
                    placeholder_idx = self._get_placeholder_idx(shape_element)
                    placeholder_type = self._get_placeholder_type(shape_element)
                    formatting = self._analyze_comprehensive_formatting(
                        runs, para, shape_element, placeholder_idx, placeholder_type
                    )

            if full_text.strip():
                return {
                    "text": full_text.strip(),
                    "formatting": formatting
                }

        except Exception as e:
            print(f"[WARNING] Erreur extraction texte: {e}")

        return None

    def _analyze_comprehensive_formatting(self, runs, paragraph_element, shape_element, placeholder_idx, placeholder_type):
        """
        Analyse le formatage de tous les runs pour déterminer l'état global des propriétés.

        Logique tri-état :
        - true : tous les runs ont la propriété activée
        - false : tous les runs ont la propriété désactivée
        - null : formatage mixte (certains runs activés, d'autres non)
        """
        if not runs:
            return {}

        # Collecter le formatage de tous les runs qui contiennent du texte
        run_formats = []

        for run in runs:
            # Vérifier si ce run contient du texte
            if LXML_AVAILABLE:
                t_elements = run.xpath('.//a:t', namespaces=NAMESPACES)
            else:
                t_elements = run.findall(f'.//{{{NAMESPACES["a"]}}}t')

            has_text = any(t.text and t.text.strip() for t in t_elements if t.text)

            if has_text:
                run_format = self.style_resolver.resolve_text_properties(
                    run, paragraph_element, shape_element, placeholder_idx, placeholder_type
                )
                run_formats.append(run_format)

        if not run_formats:
            # Si aucun run avec texte, utiliser le formatage par défaut
            return self.style_resolver.resolve_text_properties(
                runs[0], paragraph_element, shape_element, placeholder_idx, placeholder_type
            )

        # Analyser les propriétés tri-état pour bold, italic, underline
        comprehensive_format = run_formats[0].copy()  # Base format

        # Analyser bold - respect de la valeur résolue par défaut si pas de formatage explicite
        bold_values = [rf.get('bold') for rf in run_formats if 'bold' in rf and rf.get('bold') is not None]
        if bold_values:
            unique_bold_values = set(bold_values)
            if len(unique_bold_values) == 1:
                # Tous les runs ont la même valeur
                comprehensive_format['bold'] = bold_values[0]
            else:
                # Formatage mixte (certains True, certains False)
                comprehensive_format['bold'] = None
        # Si aucune valeur bold explicite dans les runs, garder la valeur par défaut résolue

        # Analyser italic - respect de la valeur résolue par défaut si pas de formatage explicite
        italic_values = [rf.get('italic') for rf in run_formats if 'italic' in rf and rf.get('italic') is not None]
        if italic_values:
            unique_italic_values = set(italic_values)
            if len(unique_italic_values) == 1:
                # Tous les runs ont la même valeur
                comprehensive_format['italic'] = italic_values[0]
            else:
                # Formatage mixte (certains True, certains False)
                comprehensive_format['italic'] = None
        # Si aucune valeur italic explicite dans les runs, garder la valeur par défaut résolue

        # Analyser underline - respect de la valeur résolue par défaut si pas de formatage explicite
        underline_values = [rf.get('underline') for rf in run_formats if 'underline' in rf and rf.get('underline') is not None]
        if underline_values:
            unique_underline_values = set(underline_values)
            if len(unique_underline_values) == 1:
                # Tous les runs ont la même valeur
                comprehensive_format['underline'] = underline_values[0]
            else:
                # Formatage mixte (certains True, certains False)
                comprehensive_format['underline'] = None
        # Si aucune valeur underline explicite dans les runs, garder la valeur par défaut résolue

        # Analyser color - respect de la valeur résolue par défaut si pas de couleur explicite
        color_values = [rf.get('color') for rf in run_formats if 'color' in rf and rf.get('color') is not None]
        if color_values:
            unique_color_values = set(color_values)
            if len(unique_color_values) == 1:
                # Tous les runs ont la même couleur
                comprehensive_format['color'] = color_values[0]
            else:
                # Formatage mixte (couleurs différentes dans les runs)
                comprehensive_format['color'] = None
        # Si aucune valeur color explicite dans les runs, garder la valeur par défaut résolue

        return comprehensive_format

    def _filter_populated_content(self, shapes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Filtre les formes pour ne garder que le contenu spécifique à la slide.

        Applique la logique de comparaison différentielle pour éliminer
        les données parasites héritées du layout.
        """
        filtered = []

        for shape in shapes:
            # Si ce n'est pas un placeholder, c'est une forme directe -> toujours inclure
            if shape.get("type") != "placeholder":
                filtered.append(shape)
                continue

            # Pour les placeholders, vérifier s'ils sont peuplés
            if self._is_placeholder_populated(shape):
                filtered.append(shape)

        return filtered

    def _is_placeholder_populated(self, shape_data: Dict[str, Any]) -> bool:
        """
        Détermine si un placeholder est peuplé avec du contenu spécifique.

        Utilise la comparaison différentielle entre slide et layout.
        """
        # Si pas de texte, considéré comme non peuplé
        if not shape_data.get("text"):
            return False

        # Pour une implémentation complète, on devrait comparer avec le layout
        # Pour l'instant, version simplifiée qui évite les textes par défaut courants
        text = shape_data.get("text", "").strip().lower()

        # Textes d'invite courants (à compléter selon les templates)
        default_texts = [
            "cliquez pour ajouter un titre",
            "cliquez pour ajouter du texte",
            "cliquez pour ajouter un sous-titre",
            "click to add title",
            "click to add text",
            "click to add subtitle"
        ]

        return text not in default_texts

    def _get_shape_name(self, shape_element) -> str:
        """Obtient le nom de la forme."""
        try:
            if LXML_AVAILABLE:
                nvsppr = shape_element.xpath('.//p:nvSpPr/p:cNvPr', namespaces=NAMESPACES)
            else:
                nvsppr = shape_element.findall(f'.//{{{NAMESPACES["p"]}}}nvSpPr/{{{NAMESPACES["p"]}}}cNvPr')

            if nvsppr:
                return nvsppr[0].get('name', 'Unknown Shape')
        except:
            pass

        return 'Unknown Shape'

    def _is_placeholder(self, shape_element) -> bool:
        """Vérifie si la forme est un placeholder."""
        try:
            if LXML_AVAILABLE:
                ph = shape_element.xpath('.//p:nvSpPr/p:nvPr/p:ph', namespaces=NAMESPACES)
            else:
                ph = shape_element.findall(f'.//{{{NAMESPACES["p"]}}}nvSpPr/{{{NAMESPACES["p"]}}}nvPr/{{{NAMESPACES["p"]}}}ph')

            return len(ph) > 0
        except:
            return False

    def _get_placeholder_info(self, shape_element) -> Dict[str, Any]:
        """Obtient les informations de placeholder."""
        info = {}

        try:
            if LXML_AVAILABLE:
                ph = shape_element.xpath('.//p:nvSpPr/p:nvPr/p:ph', namespaces=NAMESPACES)
            else:
                ph = shape_element.findall(f'.//{{{NAMESPACES["p"]}}}nvSpPr/{{{NAMESPACES["p"]}}}nvPr/{{{NAMESPACES["p"]}}}ph')

            if ph:
                ph_elem = ph[0]
                info["placeholder_type"] = ph_elem.get('type', 'body')

                idx = ph_elem.get('idx')
                if idx:
                    info["placeholder_idx"] = int(idx)
        except:
            pass

        return info

    def _get_placeholder_idx(self, shape_element) -> Optional[int]:
        """Obtient l'index du placeholder."""
        try:
            if LXML_AVAILABLE:
                ph = shape_element.xpath('.//p:nvSpPr/p:nvPr/p:ph', namespaces=NAMESPACES)
            else:
                ph = shape_element.findall(f'.//{{{NAMESPACES["p"]}}}nvSpPr/{{{NAMESPACES["p"]}}}nvPr/{{{NAMESPACES["p"]}}}ph')

            if ph:
                idx = ph[0].get('idx')
                if idx and idx != "None":  # Vérifier que ce n'est pas la chaîne "None"
                    return int(idx)
        except:
            pass

        return None

    def _get_placeholder_type(self, shape_element) -> Optional[str]:
        """Obtient le type du placeholder."""
        try:
            if LXML_AVAILABLE:
                ph = shape_element.xpath('.//p:nvSpPr/p:nvPr/p:ph', namespaces=NAMESPACES)
            else:
                ph = shape_element.findall(f'.//{{{NAMESPACES["p"]}}}nvSpPr/{{{NAMESPACES["p"]}}}nvPr/{{{NAMESPACES["p"]}}}ph')

            if ph:
                return ph[0].get('type', 'body')
        except:
            pass

        return None

    def _get_shape_position(self, shape_element) -> Dict[str, float]:
        """Obtient la position et dimensions de la forme."""
        position = {"left": 0, "top": 0, "width": 0, "height": 0}

        # Étape 1: Chercher position directe dans la forme
        xfrm_elem = self._find_xfrm_in_shape(shape_element)

        # Étape 2: Si pas trouvé et c'est un placeholder, chercher dans le layout
        if xfrm_elem is None and self._is_placeholder(shape_element):
            xfrm_elem = self._find_xfrm_in_layout_for_placeholder(shape_element)

        if xfrm_elem is not None:
            self._extract_position_from_xfrm(xfrm_elem, position)

        return position

    def _find_xfrm_in_shape(self, shape_element):
        """Cherche l'élément xfrm directement dans la forme."""
        try:
            if LXML_AVAILABLE:
                xfrm = shape_element.xpath('./p:spPr/a:xfrm', namespaces=NAMESPACES)
            else:
                xfrm = shape_element.findall(f'./{{{NAMESPACES["p"]}}}spPr/{{{NAMESPACES["a"]}}}xfrm')

            return xfrm[0] if xfrm else None
        except:
            return None

    def _find_xfrm_in_layout_for_placeholder(self, shape_element):
        """Cherche la position dans le layout pour un placeholder."""
        if self.layout_tree is None:
            return None

        try:
            # Obtenir les informations du placeholder
            placeholder_info = self._get_placeholder_info(shape_element)
            placeholder_type = placeholder_info.get("placeholder_type")
            placeholder_idx = placeholder_info.get("placeholder_idx")

            # Chercher le placeholder correspondant dans le layout
            if LXML_AVAILABLE:
                layout_shapes = self.layout_tree.xpath('//p:sp', namespaces=NAMESPACES)
            else:
                layout_shapes = self.layout_tree.findall(f'.//{{{NAMESPACES["p"]}}}sp')

            for layout_shape in layout_shapes:
                # Vérifier si c'est le bon placeholder
                if LXML_AVAILABLE:
                    ph_elements = layout_shape.xpath('.//p:nvSpPr/p:nvPr/p:ph', namespaces=NAMESPACES)
                else:
                    ph_elements = layout_shape.findall(f'.//{{{NAMESPACES["p"]}}}nvSpPr/{{{NAMESPACES["p"]}}}nvPr/{{{NAMESPACES["p"]}}}ph')

                if ph_elements:
                    ph_elem = ph_elements[0]
                    layout_type = ph_elem.get('type', 'body')
                    layout_idx_str = ph_elem.get('idx')

                    layout_idx = None
                    if layout_idx_str and layout_idx_str != "None":
                        try:
                            layout_idx = int(layout_idx_str)
                        except:
                            pass

                    # Vérifier correspondance
                    if ((placeholder_type == layout_type) and
                        (placeholder_idx == layout_idx)):

                        # Chercher xfrm dans ce placeholder du layout
                        if LXML_AVAILABLE:
                            xfrm = layout_shape.xpath('./p:spPr/a:xfrm', namespaces=NAMESPACES)
                        else:
                            xfrm = layout_shape.findall(f'./{{{NAMESPACES["p"]}}}spPr/{{{NAMESPACES["a"]}}}xfrm')

                        if xfrm:
                            return xfrm[0]

        except Exception as e:
            # print(f"[DEBUG] Erreur recherche dans layout: {e}")
            pass

        return None

    def _extract_position_from_xfrm(self, xfrm_elem, position):
        """Extrait les positions depuis un élément xfrm."""
        try:
            # Position (off)
            if LXML_AVAILABLE:
                off = xfrm_elem.xpath('./a:off', namespaces=NAMESPACES)
            else:
                off = xfrm_elem.findall(f'./{{{NAMESPACES["a"]}}}off')

            if off:
                x = off[0].get('x')
                y = off[0].get('y')
                if x:
                    try:
                        position["left"] = round(int(x) / EMU_PER_POINT, 2)
                    except ValueError:
                        pass
                if y:
                    try:
                        position["top"] = round(int(y) / EMU_PER_POINT, 2)
                    except ValueError:
                        pass

            # Dimensions (ext)
            if LXML_AVAILABLE:
                ext = xfrm_elem.xpath('./a:ext', namespaces=NAMESPACES)
            else:
                ext = xfrm_elem.findall(f'./{{{NAMESPACES["a"]}}}ext')

            if ext:
                cx = ext[0].get('cx')
                cy = ext[0].get('cy')
                if cx:
                    try:
                        position["width"] = round(int(cx) / EMU_PER_POINT, 2)
                    except ValueError:
                        pass
                if cy:
                    try:
                        position["height"] = round(int(cy) / EMU_PER_POINT, 2)
                    except ValueError:
                        pass

        except Exception as e:
            print(f"[WARNING] Erreur extraction depuis xfrm: {e}")


# =============================================================================
# FONCTIONS UTILITAIRES ET POINT D'ENTRÉE
# =============================================================================

def find_slide_part_name(package: PPTXPackage, slide_number: int) -> Optional[str]:
    """
    Trouve le nom de la partie pour un numéro de slide donné.

    Args:
        package: Package PPTX ouvert
        slide_number: Numéro de slide (1-indexé)

    Returns:
        Nom de la partie slide ou None
    """
    try:
        presentation_tree = package.get_xml_tree('ppt/presentation.xml')
        if presentation_tree is None:
            return None

        root = presentation_tree.getroot()

        if LXML_AVAILABLE:
            slide_ids = root.xpath('.//p:sldIdLst/p:sldId', namespaces=NAMESPACES)
        else:
            slide_ids = root.findall(f'.//{{{NAMESPACES["p"]}}}sldIdLst/{{{NAMESPACES["p"]}}}sldId')

        if slide_number <= len(slide_ids):
            slide_id_elem = slide_ids[slide_number - 1]
            rel_id = slide_id_elem.get(f'{{{NAMESPACES["r"]}}}id')

            if rel_id:
                # Résoudre la relation
                pres_rels = package.get_xml_tree('ppt/_rels/presentation.xml.rels')
                if pres_rels:
                    relations = package._parse_relations(pres_rels)
                    target = relations.get(rel_id)
                    if target:
                        return f"ppt/{target}"

    except Exception as e:
        print(f"[WARNING] Erreur recherche slide {slide_number}: {e}")

    # Fallback : nom standard
    return f"ppt/slides/slide{slide_number}.xml"


def main():
    """Point d'entrée principal du script."""
    parser = argparse.ArgumentParser(
        description="Extracteur de métadonnées PowerPoint avec analyse XML directe",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python tools/slide_extractor.py presentation.pptx --slide-number 11
  python tools/slide_extractor.py presentation.pptx --slide-number 11 --output slide_11.json
  python tools/slide_extractor.py presentation.pptx --slide-number 11 --debug
        """
    )

    parser.add_argument("pptx_file", help="Chemin vers le fichier .pptx")
    parser.add_argument("--slide-number", type=int, required=True,
                       help="Numéro de la slide à extraire (commence à 1)")
    parser.add_argument("--output", help="Chemin du fichier JSON de sortie")
    parser.add_argument("--debug", action="store_true",
                       help="Affichage des informations de debug détaillées")

    args = parser.parse_args()

    # Vérifier que le fichier existe
    if not os.path.exists(args.pptx_file):
        print(f"[ERROR] Fichier non trouvé : {args.pptx_file}")
        sys.exit(1)

    package = None
    try:
        if args.debug:
            print(f"[DEBUG] Ouverture de {args.pptx_file}")
            print(f"[DEBUG] lxml disponible: {LXML_AVAILABLE}")

        # Initialiser le package
        package = PPTXPackage(args.pptx_file)

        # Trouver la partie slide
        slide_part_name = find_slide_part_name(package, args.slide_number)
        if not slide_part_name:
            print(f"[ERROR] Impossible de trouver la slide {args.slide_number}")
            sys.exit(1)

        if args.debug:
            print(f"[DEBUG] Partie slide trouvée: {slide_part_name}")

        # Extraire les métadonnées
        extractor = SlideExtractor(package, slide_part_name)

        if args.debug:
            print(f"[DEBUG] Chaîne d'héritage:")
            print(f"  - Slide: {slide_part_name}")
            print(f"  - Layout: {'Trouvé' if extractor.layout_tree else 'Non trouvé'}")
            print(f"  - Master: {'Trouvé' if extractor.master_tree else 'Non trouvé'}")
            print(f"  - Theme: {'Trouvé' if extractor.theme else 'Non trouvé'}")

        metadata = extractor.extract_metadata()

        # Sortie des résultats
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            print(f"[SUCCESS] Métadonnées sauvegardées dans {args.output}")
        else:
            print(json.dumps(metadata, indent=2, ensure_ascii=False))

        # Affichage du résumé
        print(f"\n[INFO] Slide {args.slide_number} - Layout: {metadata.get('layout_name', 'Unknown')}")
        print(f"[INFO] Formes extraites : {metadata.get('total_shapes', 0)}")

        if args.debug:
            shapes_with_text = [s for s in metadata.get('shapes', []) if s.get('text')]
            print(f"[DEBUG] Formes avec texte : {len(shapes_with_text)}")

            for shape in shapes_with_text:
                text_preview = shape.get('text', '')[:50] + ('...' if len(shape.get('text', '')) > 50 else '')
                print(f"[DEBUG] - {shape.get('name', 'Unknown')}: {text_preview}")

    except Exception as e:
        print(f"[ERROR] Erreur lors de l'extraction : {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        sys.exit(1)

    finally:
        if package:
            package.close()


if __name__ == "__main__":
    main()