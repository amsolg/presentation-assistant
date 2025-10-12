#!/usr/bin/env python3
"""
Script d'execution pour le test unitaire du script 10 - Slide 52 Passion Tech
Execute automatiquement le test d'ajout de conclusion Passion et Technologies Premier Tech.
Test: Conclusion corporate avec style passion_tech (slide 52)

Ce test execute sequentiellement:
1. Script 01 pour creer la presentation de base
2. Script 10 pour ajouter la conclusion Passion et Technologies (slide 52)
3. Verification du bon contenu et style corporate
"""

import sys
from pathlib import Path

# Ajouter le repertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et executer le test
from test_slide_52_passion_tech import main

if __name__ == "__main__":
    print("Execution du test unitaire - Script 10 - Slide 52 Passion Tech")
    print("=" * 70)
    main()