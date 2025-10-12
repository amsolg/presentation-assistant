#!/usr/bin/env python3
"""
Script d'exécution pour le test unitaire du script 01 - Slide 11
Exécute automatiquement le test de création de slide titre Premier Tech.
"""

import sys
from pathlib import Path

# Ajouter le répertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et exécuter le test
from test_slide_11_creation import main

if __name__ == "__main__":
    print("Execution du test unitaire - Script 01 - Slide 11")
    print("=" * 60)
    main()