# -*- coding: utf-8 -*-
"""
Script pour ajouter ou insérer des slides dans un schéma de présentation existant.

Usage:
    python tools/add_slide.py <presentation_schema_path> <slide_number> <mode> [position]

Arguments:
    presentation_schema_path (str): Chemin vers le fichier presentation_schema.json
    slide_number (int): Numéro de la slide à copier (1-57)
    mode (str): Mode d'ajout - "ajout" ou "insertion"
    position (int, optionnel): Position d'insertion (requis si mode = "insertion")

Exemples:
    # Ajouter une slide à la fin
    python tools/add_slide.py presentations/mon-sujet/audience/presentation_schema.json 13 ajout

    # Insérer une slide à la position 2 (les slides suivantes sont renumérotées)
    python tools/add_slide.py presentations/mon-sujet/audience/presentation_schema.json 13 insertion 2
"""

import os
import sys
import json
import copy
from pathlib import Path

def load_slide_template(slide_number):
    """Charge le template de slide depuis slide-structure."""
    template_path = Path("templates/presentation-project/slide-structure") / f"slide_{slide_number}.json"

    if not template_path.exists():
        raise FileNotFoundError(f"Template de slide non trouvé: {template_path}")

    with open(template_path, 'r', encoding='utf-8') as f:
        slide_template = json.load(f)

    return slide_template

def load_presentation_schema(schema_path):
    """Charge le schéma de présentation."""
    schema_path = Path(schema_path)

    if not schema_path.exists():
        raise FileNotFoundError(f"Fichier de schéma non trouvé: {schema_path}")

    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)

    return schema, schema_path

def save_presentation_schema(schema, schema_path):
    """Sauvegarde le schéma de présentation mis à jour."""
    with open(schema_path, 'w', encoding='utf-8') as f:
        json.dump(schema, f, indent=2, ensure_ascii=False)

def convert_template_to_slide_config(template, new_slide_number):
    """Convertit un template de slide-structure en configuration pour presentation_schema."""
    slide_config = {
        "slide_number": new_slide_number,
        "layout_name": template.get("layout_name", "Layout inconnu"),
        "shapes": []
    }

    # Convertir chaque shape du template
    for shape in template.get("shapes", []):
        shape_config = {
            "shape_id": shape["shape_id"],
            "name": shape.get("name", f"Shape {shape['shape_id']}"),
            "text": shape.get("text", ""),
            "font_name": shape.get("font_name", "Premier Tech Text"),
            "font_size": shape.get("font_size", 18.0),
            "bold": shape.get("bold", False),
            "alignment": shape.get("alignment", "LEFT"),
            "color": shape.get("color", "#FFFFFF"),
            "vertical_alignment": shape.get("vertical_alignment", "TOP"),
            "margin_left": shape.get("margin_left", 7.2),
            "margin_right": shape.get("margin_right", 7.2),
            "margin_top": shape.get("margin_top", 3.6),
            "margin_bottom": shape.get("margin_bottom", 3.6),
            "autofit_type": shape.get("autofit", {}).get("type", "none"),
            "text_wrapping": shape.get("text_wrapping", "square"),
            "placeholder_type": shape.get("placeholder_type", "body")
        }

        # Ajouter les propriétés de position si disponibles
        if "position" in shape:
            shape_config.update({
                "left": shape["position"].get("left"),
                "top": shape["position"].get("top"),
                "width": shape["position"].get("width"),
                "height": shape["position"].get("height")
            })

        # Ajouter autofit avancé si disponible
        autofit = shape.get("autofit", {})
        if autofit.get("font_scale"):
            shape_config["font_scale"] = autofit["font_scale"]
        if autofit.get("line_spacing_reduction"):
            shape_config["line_spacing_reduction"] = autofit["line_spacing_reduction"]

        slide_config["shapes"].append(shape_config)

    return slide_config

def renumber_slides(slides, start_position):
    """Renumérote les slides à partir de la position donnée."""
    for i, slide in enumerate(slides):
        if i >= start_position:
            slide["slide_number"] = i + 1
    return slides

def add_slide_to_end(schema, slide_template, template_slide_number):
    """Ajoute une slide à la fin du schéma."""
    # Calculer le nouveau numéro de slide
    if schema["slides"]:
        new_slide_number = max(slide["slide_number"] for slide in schema["slides"]) + 1
    else:
        new_slide_number = 1

    # Convertir le template en configuration de slide
    new_slide = convert_template_to_slide_config(slide_template, new_slide_number)

    # Ajouter à la fin
    schema["slides"].append(new_slide)

    print(f"[OK] Slide {template_slide_number} ajoutée à la fin (nouvelle position: {new_slide_number})")

    return schema

def insert_slide_at_position(schema, slide_template, template_slide_number, position):
    """Insère une slide à la position spécifiée et renumérote les suivantes."""
    if position < 1:
        raise ValueError("La position doit être >= 1")

    if position > len(schema["slides"]) + 1:
        raise ValueError(f"Position trop élevée. Maximum: {len(schema['slides']) + 1}")

    # Convertir le template en configuration de slide
    new_slide = convert_template_to_slide_config(slide_template, position)

    # Insérer à la position spécifiée (index = position - 1)
    schema["slides"].insert(position - 1, new_slide)

    # Renumérotter toutes les slides
    schema["slides"] = renumber_slides(schema["slides"], 0)

    print(f"[OK] Slide {template_slide_number} insérée à la position {position}")
    print(f"[OK] {len(schema['slides']) - position} slides suivantes renumérotées")

    return schema

def validate_arguments(args):
    """Valide les arguments de ligne de commande."""
    if len(args) < 4:
        print("Erreur: Arguments insuffisants")
        print("Usage: python tools/add_slide.py <schema_path> <slide_number> <mode> [position]")
        sys.exit(1)

    schema_path = args[1]

    try:
        slide_number = int(args[2])
        if slide_number < 1 or slide_number > 57:
            raise ValueError("Le numéro de slide doit être entre 1 et 57")
    except ValueError as e:
        print(f"Erreur: Numéro de slide invalide - {e}")
        sys.exit(1)

    mode = args[3].lower()
    if mode not in ["ajout", "insertion"]:
        print("Erreur: Mode doit être 'ajout' ou 'insertion'")
        sys.exit(1)

    position = None
    if mode == "insertion":
        if len(args) < 5:
            print("Erreur: Position requise pour le mode 'insertion'")
            sys.exit(1)
        try:
            position = int(args[4])
            if position < 1:
                raise ValueError("La position doit être >= 1")
        except ValueError as e:
            print(f"Erreur: Position invalide - {e}")
            sys.exit(1)
    elif len(args) >= 5:
        print("Attention: Position ignorée en mode 'ajout'")

    return schema_path, slide_number, mode, position

def main():
    if len(sys.argv) < 4:
        print("Usage: python tools/add_slide.py <schema_path> <slide_number> <mode> [position]")
        print()
        print("Arguments:")
        print("  schema_path   : Chemin vers presentation_schema.json")
        print("  slide_number  : Numéro de slide à copier (1-57)")
        print("  mode          : 'ajout' ou 'insertion'")
        print("  position      : Position d'insertion (requis si mode = 'insertion')")
        print()
        print("Exemples:")
        print("  python tools/add_slide.py presentations/sujet/audience/presentation_schema.json 13 ajout")
        print("  python tools/add_slide.py presentations/sujet/audience/presentation_schema.json 13 insertion 2")
        sys.exit(1)

    try:
        # Valider les arguments
        schema_path, slide_number, mode, position = validate_arguments(sys.argv)

        print(f"Ajout de slide {slide_number} au schéma {schema_path}")
        print(f"Mode: {mode}" + (f", Position: {position}" if position else ""))
        print()

        # Charger le template de slide
        print(f"[INFO] Chargement du template slide_{slide_number}.json...")
        slide_template = load_slide_template(slide_number)
        print(f"[OK] Template chargé: {slide_template.get('layout_name', 'Layout inconnu')}")

        # Charger le schéma de présentation
        print(f"[INFO] Chargement du schéma de présentation...")
        schema, schema_file_path = load_presentation_schema(schema_path)
        print(f"[OK] Schéma chargé: {schema.get('presentation_name', 'Sans nom')}")
        print(f"[INFO] Slides actuelles: {len(schema.get('slides', []))}")

        # Sauvegarder l'état initial
        slides_before = len(schema.get('slides', []))

        # Traiter selon le mode
        if mode == "ajout":
            schema = add_slide_to_end(schema, slide_template, slide_number)
        else:  # insertion
            schema = insert_slide_at_position(schema, slide_template, slide_number, position)

        # Sauvegarder le schéma mis à jour
        print(f"[INFO] Sauvegarde du schéma mis à jour...")
        save_presentation_schema(schema, schema_file_path)

        slides_after = len(schema.get('slides', []))
        print(f"[OK] Schéma sauvegardé avec succès!")
        print(f"[INFO] Slides avant: {slides_before}, après: {slides_after}")

        # Afficher un résumé
        print()
        print("=== RÉSUMÉ ===")
        print(f"Template utilisé: slide_{slide_number}.json ({slide_template.get('layout_name', 'Layout inconnu')})")
        print(f"Mode d'ajout: {mode}")
        if mode == "insertion":
            print(f"Position d'insertion: {position}")
        print(f"Total de slides dans le schéma: {slides_after}")
        print(f"Fichier mis à jour: {schema_file_path}")

    except FileNotFoundError as e:
        print(f"Erreur: Fichier non trouvé - {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Erreur: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()