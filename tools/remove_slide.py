# -*- coding: utf-8 -*-
"""
Script pour supprimer des slides d'un schéma de présentation existant.

Usage:
    python tools/remove_slide.py <config_path> <slide_position>

Arguments:
    config_path (str): Chemin vers le fichier config.json
    slide_position (int): Position de la slide à supprimer (1-based)

Exemple:
    python tools/remove_slide.py presentations/mon-sujet/audience/config.json 3
"""

import os
import sys
import json
from pathlib import Path

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

def renumber_slides_after_removal(slides):
    """Renumérote toutes les slides après suppression."""
    for i, slide in enumerate(slides):
        slide["slide_number"] = i + 1
    return slides

def remove_slide_at_position(schema, position):
    """Supprime une slide à la position spécifiée et renumérote les suivantes."""
    slides = schema.get("slides", [])

    if position < 1 or position > len(slides):
        raise ValueError(f"Position invalide. Doit être entre 1 et {len(slides)}")

    # Récupérer des infos sur la slide à supprimer pour le log
    slide_to_remove = slides[position - 1]
    slide_info = f"Slide {slide_to_remove['slide_number']}"
    if slide_to_remove.get('shapes') and len(slide_to_remove['shapes']) > 0:
        first_shape_text = slide_to_remove['shapes'][0].get('text', 'Sans texte')[:30]
        slide_info += f": {first_shape_text}..."

    # Supprimer la slide (index = position - 1)
    removed_slide = slides.pop(position - 1)

    # Renumérotter toutes les slides
    schema["slides"] = renumber_slides_after_removal(slides)

    print(f"[OK] {slide_info} supprimée")
    if len(slides) > position - 1:
        print(f"[OK] {len(slides) - (position - 1)} slides suivantes renumérotées")

    return schema

def validate_arguments(args):
    """Valide les arguments de ligne de commande."""
    if len(args) != 3:
        print("Erreur: Arguments incorrects")
        print("Usage: python tools/remove_slide.py <schema_path> <slide_position>")
        sys.exit(1)

    schema_path = args[1]

    try:
        position = int(args[2])
        if position < 1:
            raise ValueError("La position doit être >= 1")
    except ValueError as e:
        print(f"Erreur: Position invalide - {e}")
        sys.exit(1)

    return schema_path, position

def main():
    if len(sys.argv) != 3:
        print("Usage: python tools/remove_slide.py <schema_path> <slide_position>")
        print()
        print("Arguments:")
        print("  config_path     : Chemin vers config.json")
        print("  slide_position  : Position de la slide à supprimer (1-based)")
        print()
        print("Exemple:")
        print("  python tools/remove_slide.py presentations/sujet/audience/config.json 3")
        sys.exit(1)

    try:
        # Valider les arguments
        schema_path, position = validate_arguments(sys.argv)

        print(f"Suppression de la slide à la position {position} du schéma {schema_path}")
        print()

        # Charger le schéma de présentation
        print(f"[INFO] Chargement du schéma de présentation...")
        schema, schema_file_path = load_presentation_schema(schema_path)
        print(f"[OK] Schéma chargé: {schema.get('presentation_name', 'Sans nom')}")

        slides_before = len(schema.get('slides', []))
        print(f"[INFO] Slides actuelles: {slides_before}")

        if slides_before == 0:
            print("[ERROR] Aucune slide à supprimer")
            sys.exit(1)

        if position > slides_before:
            print(f"[ERROR] Position {position} invalide. Maximum: {slides_before}")
            sys.exit(1)

        # Supprimer la slide
        schema = remove_slide_at_position(schema, position)

        # Sauvegarder le schéma mis à jour
        print(f"[INFO] Sauvegarde du schéma mis à jour...")
        save_presentation_schema(schema, schema_file_path)

        slides_after = len(schema.get('slides', []))
        print(f"[OK] Schéma sauvegardé avec succès!")
        print(f"[INFO] Slides avant: {slides_before}, après: {slides_after}")

        # Afficher un résumé
        print()
        print("=== RÉSUMÉ ===")
        print(f"Position supprimée: {position}")
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