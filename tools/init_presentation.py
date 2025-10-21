# -*- coding: utf-8 -*-
"""
Script d'initialisation pour créer la structure d'une nouvelle présentation.

Usage:
    python tools/init_presentation.py <sujet> <audience> <is_test>

Arguments:
    sujet (str): Sujet de la présentation
    audience (str): Audience cible
    is_test (bool): True pour un test, False pour une présentation normale

Exemple:
    python tools/init_presentation.py innovation-strategy c-level false
    python tools/init_presentation.py test-presentation technique true
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

def create_directory_structure(sujet, audience, is_test):
    """Crée la structure de dossiers pour une nouvelle présentation."""
    base_dir = "tests" if is_test else "presentations"
    presentation_dir = Path(base_dir) / sujet / audience

    # Créer les dossiers nécessaires
    presentation_dir.mkdir(parents=True, exist_ok=True)

    # Créer le dossier output
    output_dir = presentation_dir / "output"
    output_dir.mkdir(exist_ok=True)

    # Créer le dossier data (pour les graphiques si nécessaire)
    data_dir = presentation_dir / "data"
    data_dir.mkdir(exist_ok=True)

    return presentation_dir

def create_presentation_schema(presentation_dir, sujet, audience, is_test):
    """Crée le fichier de configuration presentation_schema.json pré-rempli."""

    # Générer le nom de la présentation
    presentation_name = f"Présentation {sujet.replace('-', ' ').title()} - {audience.replace('-', ' ').title()}"

    # Générer le chemin de sortie
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{sujet}_{audience}_{timestamp}.pptx"
    output_path = f"output/{output_filename}"

    # Configuration de base sans slides (à ajouter manuellement)
    config = {
        "presentation_name": presentation_name,
        "subject": sujet,
        "audience": audience,
        "is_test": is_test,
        "output_path": output_path,
        "slides": [],
        "build_options": {
            "base_template": "templates/Template_PT.pptx",
            "auto_widen_text": True,
            "generate_reports": True,
            "preserve_styles": True
        }
    }

    # Écrire le fichier de configuration
    config_path = presentation_dir / "presentation_schema.json"
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    return config_path

def create_readme_file(presentation_dir, sujet, audience, is_test):
    """Crée un fichier README.md pour documenter la présentation."""
    readme_content = f"""# Présentation : {sujet.replace('-', ' ').title()}

## Informations générales
- **Sujet** : {sujet}
- **Audience** : {audience}
- **Type** : {'Test' if is_test else 'Présentation'}
- **Créé le** : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Structure des fichiers
- `presentation_schema.json` : Configuration principale de la présentation
- `output/` : Présentations générées
- `data/` : Données pour graphiques (CSV)

## Utilisation
Pour générer la présentation :
```bash
python presentation_builder/presentation_builder.py {presentation_dir}/presentation_schema.json
```

## Notes
- Modifier `presentation_schema.json` pour personnaliser les slides
- Ajouter des fichiers CSV dans `data/` pour les graphiques
- Les présentations générées seront dans `output/`
"""

    readme_path = presentation_dir / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    return readme_path

def main():
    if len(sys.argv) != 4:
        print("Usage: python tools/init_presentation.py <sujet> <audience> <is_test>")
        print("Exemple: python tools/init_presentation.py innovation-strategy c-level false")
        sys.exit(1)

    sujet = sys.argv[1]
    audience = sys.argv[2]
    is_test_str = sys.argv[3].lower()

    # Convertir le paramètre is_test en booléen
    if is_test_str in ['true', '1', 'yes', 'oui']:
        is_test = True
    elif is_test_str in ['false', '0', 'no', 'non']:
        is_test = False
    else:
        print("Erreur: le paramètre is_test doit être 'true' ou 'false'")
        sys.exit(1)

    print(f"Initialisation d'une nouvelle présentation...")
    print(f"  Sujet: {sujet}")
    print(f"  Audience: {audience}")
    print(f"  Test: {is_test}")
    print()

    try:
        # Créer la structure de dossiers
        presentation_dir = create_directory_structure(sujet, audience, is_test)
        print(f"[OK] Structure créée dans: {presentation_dir}")

        # Créer le fichier de configuration
        config_path = create_presentation_schema(presentation_dir, sujet, audience, is_test)
        print(f"[OK] Configuration créée: {config_path}")

        # Créer le README
        readme_path = create_readme_file(presentation_dir, sujet, audience, is_test)
        print(f"[OK] Documentation créée: {readme_path}")

        print()
        print("Initialisation terminée avec succès!")
        print(f"Pour générer la présentation, utilisez:")
        print(f"  python presentation_builder/presentation_builder.py {config_path}")

    except Exception as e:
        print(f"Erreur lors de l'initialisation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()