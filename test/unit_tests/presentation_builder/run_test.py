#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de lancement pour le test unitaire du Presentation Builder.

Execute le test de l'architecture JSON avec array slides vide.
"""

import sys
from pathlib import Path

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent))

from test_presentation_builder import TestPresentationBuilder

def main():
    print("=== TEST UNITAIRE - PRESENTATION BUILDER ===")
    print("Architecture JSON avec array slides vide")
    print()

    test_runner = TestPresentationBuilder()
    success = test_runner.run_all_tests()

    if success:
        print("\n[SUCCESS] TOUS LES TESTS REUSSIS")
        print("L'architecture JSON fonctionne correctement")
    else:
        print("\n[ERROR] ECHECS DETECTES")
        print("Verifiez les logs pour plus de details")

    return 0 if success else 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)