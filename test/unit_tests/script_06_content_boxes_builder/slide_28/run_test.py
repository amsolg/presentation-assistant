#!/usr/bin/env python3
"""
Script d'exécution pour le test unitaire du script 06 - Slide 28
Exécute automatiquement le test de création de slide avec 3 boîtes grises sans sous-titres.
"""

import sys
from pathlib import Path

# Ajouter le répertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et exécuter le test
from test_slide_28_grey_3_simple import main

if __name__ == "__main__":
    print("Execution du test unitaire - Script 06 - Slide 28")
    print("=" * 60)
    main()