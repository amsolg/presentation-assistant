#!/usr/bin/env python3
"""
Script d'execution pour le test unitaire du script 10 - Slide 57 Monogram
Execute automatiquement le test d'ajout de conclusion Monogramme Premier Tech.
Test: Conclusion minimaliste avec style monogram (slide 57)

Ce test execute sequentiellement:
1. Script 01 pour creer la presentation de base
2. Script 10 pour ajouter la conclusion Monogramme (slide 57)
3. Verification de l'élégance minimaliste et du design épuré
"""

import sys
from pathlib import Path

# Ajouter le repertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et executer le test
from test_slide_57_monogram import main

if __name__ == "__main__":
    print("Execution du test unitaire - Script 10 - Slide 57 Monogram")
    print("=" * 70)
    main()