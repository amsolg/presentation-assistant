#!/usr/bin/env python3
"""
Script d'execution pour le test unitaire du script 05 - Slide 23 Grey Line
Execute automatiquement le test d'ajout de statistiques ligne grise Premier Tech.

Ce test execute sequentiellement:
1. Script 01 pour creer la presentation de base
2. Script 05 pour ajouter les statistiques ligne grise (slide 23)
"""

import sys
from pathlib import Path

# Ajouter le repertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et executer le test
from test_slide_23_grey_line import main

if __name__ == "__main__":
    print("Execution du test unitaire - Script 05 - Slide 23 Grey Line")
    print("=" * 60)
    main()