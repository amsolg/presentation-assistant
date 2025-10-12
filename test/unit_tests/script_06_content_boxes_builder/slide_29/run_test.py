#!/usr/bin/env python3
"""
Script d'exécution pour le test unitaire du script 06 - Slide 29
Exécute automatiquement le test de création de slide avec 3 boîtes bleues avec sous-titres.
"""

import sys
from pathlib import Path

# Ajouter le répertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et exécuter le test
from test_slide_29_blue_3_detailed import main

if __name__ == "__main__":
    print("Execution du test unitaire - Script 06 - Slide 29")
    print("=" * 60)
    main()