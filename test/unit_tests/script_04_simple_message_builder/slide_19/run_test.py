#!/usr/bin/env python3
"""
Script d'execution pour le test unitaire du script 04 - Slide 19
Execute automatiquement le test d'ajout de message keywords simple Premier Tech.

Ce test execute sequentiellement:
1. Script 01 pour creer la presentation de base
2. Script 04 pour ajouter le message keywords simple (slide 19)
"""

import sys
from pathlib import Path

# Ajouter le repertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et executer le test
from test_slide_19_keyword_simple import main

if __name__ == "__main__":
    print("Execution du test unitaire - Script 04 - Slide 19")
    print("=" * 60)
    main()