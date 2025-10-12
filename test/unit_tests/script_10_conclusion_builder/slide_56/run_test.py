#!/usr/bin/env python3
"""
Script d'execution pour le test unitaire du script 10 - Slide 56 We are PT
Execute automatiquement le test d'ajout de conclusion We are PT Premier Tech.
Test: Conclusion identité collective avec style we_are_pt (slide 56)

Ce test execute sequentiellement:
1. Script 01 pour creer la presentation de base
2. Script 10 pour ajouter la conclusion We are PT (slide 56)
3. Verification de l'identité collective et l'appartenance PT
"""

import sys
from pathlib import Path

# Ajouter le repertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et executer le test
from test_slide_56_we_are_pt import main

if __name__ == "__main__":
    print("Execution du test unitaire - Script 10 - Slide 56 We are PT")
    print("=" * 70)
    main()