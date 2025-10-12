#!/usr/bin/env python3
"""
Script d'execution pour le test unitaire du script 08 - Slide 45
Execute automatiquement le test de creation de slide testimonial Premier Tech.
"""

import sys
from pathlib import Path

# Ajouter le repertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et executer le test
from test_slide_45_standard import main

if __name__ == "__main__":
    print("Execution du test unitaire - Script 08 - Slide 45")
    print("=" * 60)
    main()