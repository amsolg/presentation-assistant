#!/usr/bin/env python3
"""
Script d'exécution pour test unitaire - Script 07 - Slide 35
Point d'entrée simplifié pour exécuter le test de slide 35 avec style four_points
"""

import sys
from pathlib import Path

# Ajouter le répertoire du test au path
sys.path.insert(0, str(Path(__file__).parent))

# Importer et exécuter le test
from test_slide_35_four_points import main

if __name__ == "__main__":
    main()