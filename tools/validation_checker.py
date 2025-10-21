#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation Checker - Contrôle Qualité Automatique
=================================================

Script de validation automatique pour vérifier que les présentations générées
respectent fidèlement leurs schémas de configuration.

Workflow:
1. Prend en entrée un chemin d'audience et un numéro de slide
2. Trouve et parse le presentation_schema.json associé
3. Exécute slide_extractor.py sur la présentation générée
4. Compare shape par shape chaque configuration
5. Génère un rapport détaillé des résultats

Usage:
    python tools/validation_checker.py "tests\\ia-generative-integration\\technique" 1
"""

import os
import sys
import json
import argparse
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple


class PresentationValidator:
    """
    Validateur automatique de conformité entre schéma et présentation générée.

    Compare les configurations du schéma JSON avec les métadonnées extraites
    de la présentation PowerPoint pour détecter les écarts de conformité.
    """

    def __init__(self):
        """Initialise le validateur avec les chemins de base."""
        self.script_dir = Path(__file__).parent
        self.slide_extractor_path = self.script_dir / "slide_extractor.py"

        if not self.slide_extractor_path.exists():
            raise FileNotFoundError(f"slide_extractor.py non trouvé: {self.slide_extractor_path}")

    def validate_slide(self, audience_path: str, slide_number: int) -> Dict[str, Any]:
        """
        Valide une slide spécifique d'une présentation.

        Args:
            audience_path: Chemin vers le dossier d'audience (ex: "tests\\ia-generative-integration\\technique")
            slide_number: Numéro de la slide à valider (1-based)

        Returns:
            Dict: Résultats complets de la validation
        """
        try:
            print(f"[VALIDATION] Démarrage validation slide {slide_number}")
            print(f"[VALIDATION] Chemin audience: {audience_path}")

            # 1. Trouver et parser le schéma de présentation
            schema_data = self._load_presentation_schema(audience_path)
            presentation_name = schema_data.get("presentation_name", "Unknown")
            output_path = schema_data.get("output_path", "")

            print(f"[SCHEMA] Présentation: {presentation_name}")
            print(f"[SCHEMA] Output path: {output_path}")

            # 2. Trouver la slide dans le schéma
            schema_slide = self._find_slide_in_schema(schema_data, slide_number)
            if not schema_slide:
                return {
                    "status": "ERROR",
                    "message": f"Slide {slide_number} non trouvée dans le schéma",
                    "timestamp": datetime.now().isoformat()
                }

            # 3. Trouver et vérifier la présentation générée
            presentation_path = self._resolve_presentation_path(audience_path, output_path)
            if not presentation_path or not os.path.exists(presentation_path):
                return {
                    "status": "ERROR",
                    "message": f"Présentation non trouvée: {presentation_path}",
                    "timestamp": datetime.now().isoformat()
                }

            print(f"[PRESENTATION] Fichier trouvé: {presentation_path}")

            # 4. Extraire la slide de la présentation
            extracted_slide = self._extract_slide_from_presentation(presentation_path, slide_number)
            if not extracted_slide:
                return {
                    "status": "ERROR",
                    "message": f"Impossible d'extraire la slide {slide_number}",
                    "timestamp": datetime.now().isoformat()
                }

            # 5. Comparer les configurations
            comparison_results = self._compare_configurations(schema_slide, extracted_slide)

            # 6. Générer le rapport
            report_data = {
                "status": self._determine_overall_status(comparison_results),
                "presentation_name": presentation_name,
                "slide_number": slide_number,
                "layout_name": schema_slide.get("layout_name", extracted_slide.get("layout_name", "Unknown")),
                "audience_path": audience_path,
                "presentation_path": presentation_path,
                "timestamp": datetime.now().isoformat(),
                "comparison_results": comparison_results,
                "summary": self._generate_summary(comparison_results)
            }

            # 7. Sauvegarder le rapport
            self._save_validation_report(report_data, audience_path)

            return report_data

        except Exception as e:
            return {
                "status": "ERROR",
                "message": f"Erreur validation: {e}",
                "timestamp": datetime.now().isoformat()
            }

    def _load_presentation_schema(self, audience_path: str) -> Dict[str, Any]:
        """Charge le fichier presentation_schema.json."""
        schema_path = os.path.join(audience_path, "presentation_schema.json")

        if not os.path.exists(schema_path):
            raise FileNotFoundError(f"Schema non trouvé: {schema_path}")

        with open(schema_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _find_slide_in_schema(self, schema_data: Dict[str, Any], slide_number: int) -> Optional[Dict[str, Any]]:
        """Trouve la slide correspondante dans le schéma."""
        slides = schema_data.get("slides", [])

        # Chercher par position dans le tableau (slide_number correspond à la position)
        if 1 <= slide_number <= len(slides):
            return slides[slide_number - 1]

        # Chercher par slide_number explicite (si présent)
        for slide in slides:
            if slide.get("slide_number") == slide_number:
                return slide

        return None

    def _resolve_presentation_path(self, audience_path: str, output_path: str) -> Optional[str]:
        """Résout le chemin complet vers la présentation générée."""
        if os.path.isabs(output_path):
            return output_path

        # Chemin relatif - plusieurs options à essayer
        possible_paths = [
            os.path.join(audience_path, output_path),
            os.path.join(audience_path, "output", os.path.basename(output_path)),
            output_path  # Peut être relatif au répertoire de travail
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None

    def _extract_slide_from_presentation(self, presentation_path: str, slide_number: int) -> Optional[Dict[str, Any]]:
        """Utilise slide_extractor.py pour extraire les métadonnées de la slide."""
        try:
            # Créer un fichier temporaire pour la sortie
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp_file:
                temp_output = temp_file.name

            # Exécuter slide_extractor.py
            cmd = [
                sys.executable,
                str(self.slide_extractor_path),
                presentation_path,
                "--slide-number", str(slide_number),
                "--output", temp_output
            ]

            print(f"[EXTRACTION] Commande: {' '.join(cmd)}")

            result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')

            if result.returncode != 0:
                print(f"[ERROR] Échec extraction: {result.stderr}")
                return None

            # Charger les métadonnées extraites
            with open(temp_output, 'r', encoding='utf-8') as f:
                extracted_data = json.load(f)

            # Nettoyer le fichier temporaire
            os.unlink(temp_output)

            print(f"[EXTRACTION] Slide extraite: {extracted_data.get('layout_name', 'Unknown')}")
            print(f"[EXTRACTION] Shapes trouvées: {extracted_data.get('total_shapes', 0)}")

            return extracted_data

        except Exception as e:
            print(f"[ERROR] Erreur extraction: {e}")
            return None

    def _compare_configurations(self, schema_slide: Dict[str, Any], extracted_slide: Dict[str, Any]) -> Dict[str, Any]:
        """Compare les configurations shape par shape."""
        results = {
            "slide_comparison": self._compare_slide_metadata(schema_slide, extracted_slide),
            "shapes_comparison": [],
            "statistics": {
                "total_shapes": 0,
                "conforming_shapes": 0,
                "non_conforming_shapes": 0,
                "missing_shapes": 0
            }
        }

        schema_shapes = schema_slide.get("shapes", [])
        extracted_shapes = extracted_slide.get("shapes", [])

        print(f"[COMPARISON] Shapes schéma: {len(schema_shapes)}, extraites: {len(extracted_shapes)}")

        # Comparer chaque shape du schéma
        for schema_shape in schema_shapes:
            shape_id = schema_shape.get("shape_id")
            if shape_id is None:
                continue

            # Trouver la shape correspondante dans les données extraites
            extracted_shape = self._find_extracted_shape(extracted_shapes, shape_id)

            shape_comparison = {
                "shape_id": shape_id,
                "shape_name": schema_shape.get("name", f"Shape {shape_id}"),
                "found": extracted_shape is not None,
                "property_comparisons": {},
                "conformity_score": 0.0
            }

            if extracted_shape:
                # Comparer les propriétés
                shape_comparison["property_comparisons"] = self._compare_shape_properties(schema_shape, extracted_shape)
                shape_comparison["conformity_score"] = self._calculate_conformity_score(shape_comparison["property_comparisons"])

                if shape_comparison["conformity_score"] >= 0.95:  # 95% de conformité
                    results["statistics"]["conforming_shapes"] += 1
                else:
                    results["statistics"]["non_conforming_shapes"] += 1
            else:
                results["statistics"]["missing_shapes"] += 1

            results["shapes_comparison"].append(shape_comparison)
            results["statistics"]["total_shapes"] += 1

        return results

    def _compare_slide_metadata(self, schema_slide: Dict[str, Any], extracted_slide: Dict[str, Any]) -> Dict[str, Any]:
        """Compare les métadonnées générales de la slide."""
        return {
            "layout_name": {
                "expected": schema_slide.get("layout_name"),
                "found": extracted_slide.get("layout_name"),
                "match": schema_slide.get("layout_name") == extracted_slide.get("layout_name")
            },
            "total_shapes": {
                "expected": len(schema_slide.get("shapes", [])),
                "found": extracted_slide.get("total_shapes", 0),
                "match": len(schema_slide.get("shapes", [])) == extracted_slide.get("total_shapes", 0)
            }
        }

    def _find_extracted_shape(self, extracted_shapes: List[Dict[str, Any]], shape_id: int) -> Optional[Dict[str, Any]]:
        """Trouve une shape extraite par son shape_id."""
        for shape in extracted_shapes:
            if shape.get("shape_id") == shape_id:
                return shape
        return None

    def _compare_shape_properties(self, schema_shape: Dict[str, Any], extracted_shape: Dict[str, Any]) -> Dict[str, Any]:
        """Compare toutes les propriétés d'une shape."""
        comparisons = {}

        # Propriétés à comparer
        properties_to_compare = [
            "text", "font_name", "font_size", "color", "bold", "italic", "underline",
            "alignment", "vertical_alignment", "margin_left", "margin_right",
            "margin_top", "margin_bottom", "placeholder_type"
        ]

        # Position (objet imbriqué)
        schema_position = schema_shape.get("position", {})
        extracted_position = extracted_shape.get("position", {})

        for prop in ["left", "top", "width", "height"]:
            expected = schema_position.get(prop)
            found = extracted_position.get(prop)
            comparisons[f"position_{prop}"] = {
                "expected": expected,
                "found": found,
                "match": self._values_approximately_equal(expected, found, tolerance=0.1)
            }

        # Autofit (objet imbriqué)
        schema_autofit = schema_shape.get("autofit", {})
        extracted_autofit = extracted_shape.get("autofit", {})

        comparisons["autofit_type"] = {
            "expected": schema_autofit.get("type"),
            "found": extracted_autofit.get("type"),
            "match": schema_autofit.get("type") == extracted_autofit.get("type")
        }

        # Propriétés directes
        for prop in properties_to_compare:
            expected = schema_shape.get(prop)
            found = extracted_shape.get(prop)

            if prop in ["font_size", "margin_left", "margin_right", "margin_top", "margin_bottom"]:
                # Propriétés numériques avec tolérance
                match = self._values_approximately_equal(expected, found, tolerance=0.1)
            else:
                # Propriétés exactes
                match = expected == found

            comparisons[prop] = {
                "expected": expected,
                "found": found,
                "match": match
            }

        return comparisons

    def _values_approximately_equal(self, val1: Any, val2: Any, tolerance: float = 0.1) -> bool:
        """Compare deux valeurs avec une tolérance pour les nombres."""
        if val1 is None and val2 is None:
            return True
        if val1 is None or val2 is None:
            return False

        try:
            float_val1 = float(val1)
            float_val2 = float(val2)
            return abs(float_val1 - float_val2) <= tolerance
        except (ValueError, TypeError):
            return val1 == val2

    def _calculate_conformity_score(self, property_comparisons: Dict[str, Any]) -> float:
        """Calcule un score de conformité basé sur les propriétés qui correspondent."""
        if not property_comparisons:
            return 0.0

        total_properties = len(property_comparisons)
        matching_properties = sum(1 for comp in property_comparisons.values() if comp.get("match", False))

        return matching_properties / total_properties

    def _determine_overall_status(self, comparison_results: Dict[str, Any]) -> str:
        """Détermine le statut global de la validation."""
        stats = comparison_results["statistics"]
        total_shapes = stats["total_shapes"]

        if total_shapes == 0:
            return "WARNING"

        conformity_rate = stats["conforming_shapes"] / total_shapes

        if conformity_rate >= 0.95:
            return "CONFORME"
        elif conformity_rate >= 0.80:
            return "PARTIELLEMENT_CONFORME"
        else:
            return "NON_CONFORME"

    def _generate_summary(self, comparison_results: Dict[str, Any]) -> Dict[str, Any]:
        """Génère un résumé des résultats de validation."""
        stats = comparison_results["statistics"]
        shapes_comparison = comparison_results["shapes_comparison"]

        total_properties = 0
        matching_properties = 0

        for shape_comp in shapes_comparison:
            props = shape_comp.get("property_comparisons", {})
            total_properties += len(props)
            matching_properties += sum(1 for comp in props.values() if comp.get("match", False))

        return {
            "shapes_conformity_rate": stats["conforming_shapes"] / max(stats["total_shapes"], 1),
            "properties_conformity_rate": matching_properties / max(total_properties, 1),
            "total_issues": stats["non_conforming_shapes"] + stats["missing_shapes"],
            "quality_score": (matching_properties / max(total_properties, 1)) * 100
        }

    def _save_validation_report(self, report_data: Dict[str, Any], audience_path: str):
        """Sauvegarde le rapport de validation en format Markdown."""
        # Créer le dossier tests s'il n'existe pas
        tests_dir = os.path.join(audience_path, "tests")
        os.makedirs(tests_dir, exist_ok=True)

        # Nom du fichier de rapport
        presentation_name = report_data["presentation_name"].replace(" ", "_").replace("-", "_")
        slide_number = report_data["slide_number"]
        report_filename = f"report_{presentation_name}_{slide_number}.md"
        report_path = os.path.join(tests_dir, report_filename)

        # Générer le contenu Markdown
        report_content = self._generate_markdown_report(report_data)

        # Sauvegarder le rapport
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)

        print(f"[REPORT] Rapport sauvegardé: {report_path}")

    def _generate_markdown_report(self, report_data: Dict[str, Any]) -> str:
        """Génère le contenu Markdown du rapport de validation."""
        status = report_data["status"]
        summary = report_data["summary"]
        comparison = report_data["comparison_results"]

        # Déterminer l'icône de statut
        status_icons = {
            "CONFORME": "✅",
            "PARTIELLEMENT_CONFORME": "⚠️",
            "NON_CONFORME": "❌",
            "ERROR": "💥",
            "WARNING": "⚠️"
        }

        status_icon = status_icons.get(status, "❓")

        content = f"""# Rapport de Validation - {report_data["presentation_name"]} - Slide {report_data["slide_number"]}

## 📊 Résumé Exécutif
- {status_icon} **Status** : {status}
- **Layout** : {report_data.get("layout_name", "Unknown")}
- **Shapes validés** : {comparison["statistics"]["conforming_shapes"]}/{comparison["statistics"]["total_shapes"]} ({summary["shapes_conformity_rate"]:.1%})
- **Propriétés validées** : {summary["properties_conformity_rate"]:.1%}
- **Score qualité** : {summary["quality_score"]:.1f}%

## 🔍 Détails par Shape

"""

        # Détails pour chaque shape
        for shape_comp in comparison["shapes_comparison"]:
            shape_id = shape_comp["shape_id"]
            shape_name = shape_comp["shape_name"]
            found = shape_comp["found"]
            conformity_score = shape_comp.get("conformity_score", 0)

            if not found:
                content += f"### Shape {shape_id} - {shape_name}\n"
                content += f"❌ **Shape manquante** : Non trouvée dans la présentation générée\n\n"
                continue

            # Icône selon le score de conformité
            if conformity_score >= 0.95:
                shape_icon = "✅"
            elif conformity_score >= 0.80:
                shape_icon = "⚠️"
            else:
                shape_icon = "❌"

            content += f"### Shape {shape_id} - {shape_name}\n"
            content += f"{shape_icon} **Conformité** : {conformity_score:.1%}\n\n"

            # Détails des propriétés
            props = shape_comp.get("property_comparisons", {})

            # Regrouper par catégorie
            categories = {
                "Position": ["position_left", "position_top", "position_width", "position_height"],
                "Texte": ["text", "font_name", "font_size", "color", "bold", "italic", "underline"],
                "Alignement": ["alignment", "vertical_alignment"],
                "Marges": ["margin_left", "margin_right", "margin_top", "margin_bottom"],
                "PowerPoint": ["autofit_type", "placeholder_type"]
            }

            for category, prop_names in categories.items():
                category_props = {name: props[name] for name in prop_names if name in props}
                if not category_props:
                    continue

                content += f"#### {category}\n"
                for prop_name, prop_data in category_props.items():
                    expected = prop_data["expected"]
                    found = prop_data["found"]
                    match = prop_data["match"]

                    prop_icon = "✅" if match else "❌"
                    prop_display_name = prop_name.replace("_", " ").title()

                    if match:
                        content += f"- {prop_icon} **{prop_display_name}** : Conforme ({found})\n"
                    else:
                        content += f"- {prop_icon} **{prop_display_name}** : Non conforme\n"
                        content += f"  - Attendu : `{expected}`\n"
                        content += f"  - Trouvé : `{found}`\n"

                content += "\n"

        # Métriques de qualité
        content += f"""## 📈 Métriques de Qualité
- **Fidélité shapes** : {summary["shapes_conformity_rate"]:.1%}
- **Fidélité propriétés** : {summary["properties_conformity_rate"]:.1%}
- **Issues totales** : {summary["total_issues"]}
- **Score global** : {summary["quality_score"]:.1f}%

## 🛠️ Informations Techniques
- **Fichier schéma** : {report_data["audience_path"]}/presentation_schema.json
- **Présentation générée** : {report_data["presentation_path"]}
- **Validation effectuée** : {report_data["timestamp"]}

"""

        # Recommandations si des problèmes sont détectés
        if status != "CONFORME":
            content += """## 🔧 Recommandations
- Vérifier la configuration des shapes non conformes dans le schéma JSON
- S'assurer que les propriétés utilisent les valeurs Premier Tech valides
- Contrôler que le layout_name correspond au bon template
- Régénérer la présentation après correction du schéma

"""

        return content


def main():
    """Interface en ligne de commande."""
    parser = argparse.ArgumentParser(
        description='Validation automatique de conformité présentation vs schéma',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python tools/validation_checker.py "tests\\ia-generative-integration\\technique" 1
  python tools/validation_checker.py "presentations\\mon-sujet\\c-level" 2
        """
    )

    parser.add_argument("audience_path", help="Chemin vers le dossier d'audience")
    parser.add_argument("slide_number", type=int, help="Numéro de la slide à valider (1-based)")
    parser.add_argument("--verbose", action="store_true", help="Affichage détaillé")

    args = parser.parse_args()

    try:
        validator = PresentationValidator()
        results = validator.validate_slide(args.audience_path, args.slide_number)

        # Affichage des résultats
        status = results.get("status", "ERROR")
        print(f"\n=== RÉSULTATS VALIDATION ===")
        print(f"Status: {status}")

        if "summary" in results:
            summary = results["summary"]
            print(f"Score qualité: {summary['quality_score']:.1f}%")
            print(f"Conformité shapes: {summary['shapes_conformity_rate']:.1%}")
            print(f"Conformité propriétés: {summary['properties_conformity_rate']:.1%}")

        if status == "ERROR":
            print(f"Erreur: {results.get('message', 'Erreur inconnue')}")
            sys.exit(1)

    except Exception as e:
        print(f"[ERROR] Erreur validation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()