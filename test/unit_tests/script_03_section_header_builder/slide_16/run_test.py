#!/usr/bin/env python3
"""
Script d'execution pour le test unitaire du script 03 - Slide 16
Execute automatiquement le test d'ajout de section header moderee Premier Tech.

Ce test execute sequentiellement:
1. Script 01 pour creer la presentation de base
2. Script 03 pour ajouter la section header moderee (slide 16)
"""

import sys
from pathlib import Path

# Ajouter le repertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et executer le test
from test_slide_16_moderate import main

if __name__ == "__main__":
    print("Execution du test unitaire - Script 03 - Slide 16")
    print("=" * 60)
    main()