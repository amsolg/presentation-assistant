#!/usr/bin/env python3
"""
Script d'exécution pour le test unitaire du script 07 - Slide 39
Exécute automatiquement le test d'ajout d'explication détaillée Premier Tech.

Ce test exécute séquentiellement:
1. Script 01 pour créer la présentation de base
2. Script 07 pour ajouter l'explication détaillée (dual_detailed_blue)
"""

import sys
from pathlib import Path

# Ajouter le répertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et exécuter le test
from test_slide_39_dual_detailed_blue import main

if __name__ == "__main__":
    print("Execution du test unitaire - Script 07 - Slide 39")
    print("=" * 60)
    main()