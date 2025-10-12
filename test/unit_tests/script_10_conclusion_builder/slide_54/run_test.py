#!/usr/bin/env python3
"""
Script d'execution pour le test unitaire du script 10 - Slide 54 Custom Conclusion
Execute automatiquement le test d'ajout de conclusion personnalisée Premier Tech.
Test: Conclusion personnalisée avec style custom_conclusion (slide 54)

Ce test execute sequentiellement:
1. Script 01 pour creer la presentation de base
2. Script 10 pour ajouter la conclusion personnalisée (slide 54)
3. Verification du contenu personnalisé et de l'adaptabilité
"""

import sys
from pathlib import Path

# Ajouter le repertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et executer le test
from test_slide_54_custom_conclusion import main

if __name__ == "__main__":
    print("Execution du test unitaire - Script 10 - Slide 54 Custom Conclusion")
    print("=" * 70)
    main()