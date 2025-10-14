#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script principal pour exécuter tous les tests du Navigation Builder
Architecture JSON 2025 - Tests unitaires complets
"""

import os
import sys
import json
import subprocess
from datetime import datetime
from pathlib import Path


def main():
    """Exécute tous les tests de navigation builder"""
    print("="*80)
    print("NAVIGATION BUILDER - TESTS UNITAIRES COMPLETS")
    print("Architecture JSON 2025")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("="*80)

    # Changer vers le répertoire de tests
    test_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(test_dir)

    print(f"Répertoire de tests: {test_dir}")

    # Vérifier que les fichiers de test existent
    test_files = [
        "test_navigation_builder.py",
        "basic_toc/navigation_config.json",
        "detailed_toc/navigation_config.json",
        "strategic_toc/navigation_config.json"
    ]

    missing_files = []
    for file in test_files:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        print(f"[ERROR] Fichiers manquants: {missing_files}")
        return False

    print("[OK] Tous les fichiers de test sont présents")

    # Créer le dossier output si nécessaire
    os.makedirs("output", exist_ok=True)

    # Exécuter le script de test principal
    print("\n" + "="*60)
    print("EXECUTION DES TESTS UNITAIRES")
    print("="*60)

    try:
        # Exécuter les tests avec capture de sortie
        result = subprocess.run(
            [sys.executable, "test_navigation_builder.py"],
            capture_output=False,  # Laisser les sorties apparaître en temps réel
            text=True,
            cwd=test_dir
        )

        success = result.returncode == 0

        print("\n" + "="*60)
        print("RÉSULTATS FINAUX")
        print("="*60)

        if success:
            print("[SUCCESS] Tous les tests sont passés avec succès!")
        else:
            print(f"[FAILURE] Certains tests ont échoué (code de retour: {result.returncode})")

        # Lister les fichiers de sortie générés
        output_dir = os.path.join(test_dir, "output")
        if os.path.exists(output_dir):
            output_files = os.listdir(output_dir)
            if output_files:
                print(f"\nFichiers générés dans output/:")
                for file in sorted(output_files):
                    file_path = os.path.join(output_dir, file)
                    file_size = os.path.getsize(file_path) if os.path.exists(file_path) else 0
                    print(f"  - {file} ({file_size:,} bytes)")

        return success

    except Exception as e:
        print(f"[ERROR] Erreur lors de l'exécution des tests: {e}")
        return False


def check_environment():
    """Vérifie que l'environnement est prêt pour les tests"""
    print("Vérification de l'environnement...")

    # Vérifier la présence du template Premier Tech
    template_path = os.path.join('..', '..', '..', 'templates', 'Template_PT.pptx')
    if not os.path.exists(template_path):
        print(f"[WARNING] Template Premier Tech non trouvé: {template_path}")
        print("Les tests peuvent échouer sans le template")

    # Vérifier les modules Python requis
    required_modules = ['pptx', 'json', 'unittest']
    missing_modules = []

    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)

    if missing_modules:
        print(f"[ERROR] Modules Python manquants: {missing_modules}")
        print("Installez les dépendances requises avec: pip install python-pptx")
        return False

    print("[OK] Environnement prêt pour les tests")
    return True


if __name__ == "__main__":
    print("Navigation Builder - Tests Unitaires")
    print(f"Démarrage: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Vérifier l'environnement
    if not check_environment():
        print("[ABORT] Environnement non prêt")
        sys.exit(1)

    # Exécuter les tests
    success = main()

    print(f"\nFin des tests: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    sys.exit(0 if success else 1)