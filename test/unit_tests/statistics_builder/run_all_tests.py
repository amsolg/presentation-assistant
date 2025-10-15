#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour lancer tous les tests du Statistics Builder
"""

import os
import sys
from datetime import datetime

def main():
    """Lance tous les tests statistics_builder"""
    print("=== STATISTICS BUILDER TESTS RUNNER ===")
    print(f"Démarrage: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Changer vers le répertoire des tests
    os.chdir(os.path.dirname(__file__))

    # Importer et lancer les tests
    try:
        from test_statistics_builder import run_all_tests
        success = run_all_tests()

        if success:
            print(f"\n🎉 TOUS LES TESTS RÉUSSIS!")
            sys.exit(0)
        else:
            print(f"\n❌ CERTAINS TESTS ONT ÉCHOUÉ!")
            sys.exit(1)

    except Exception as e:
        print(f"\n💥 ERREUR CRITIQUE: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()