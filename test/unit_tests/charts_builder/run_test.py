#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de lancement des tests Charts Builder
Simplifie l'exécution des tests unitaires pour le charts_builder.
"""

import os
import sys
from pathlib import Path

# Ajouter le chemin de test au sys.path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et exécuter les tests
from test_charts_builder import run_charts_builder_tests

if __name__ == "__main__":
    print("Lancement des tests Charts Builder...")
    print(f"Répertoire de test: {test_dir}")

    success = run_charts_builder_tests()

    if success:
        print("\n[SUCCESS] TOUS LES TESTS SONT PASSES!")
        print("[SUCCESS] Migration Charts Builder vers l'architecture JSON 2025 REUSSIE!")
    else:
        print("\n[WARNING] CERTAINS TESTS ONT ECHOUE")
        print("[ERROR] Verifiez les erreurs ci-dessus")

    sys.exit(0 if success else 1)