#!/usr/bin/env python3
"""
Script d'execution pour le test unitaire du script 05 - Satisfaction vs Experience
Execute automatiquement le test d'ajout de statistiques ligne bleue Premier Tech.
Test: 87% Satisfaction Client (droite) vs 23+ Années d'Experience (gauche)

Ce test execute sequentiellement:
1. Script 01 pour creer la presentation de base
2. Script 05 pour ajouter les statistiques ligne bleue (slide 22)
3. Verification du positionnement correct des statistiques
"""

import sys
from pathlib import Path

# Ajouter le repertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer et executer le test
from test_satisfaction_vs_experience_slide_22 import main

if __name__ == "__main__":
    print("Execution du test unitaire - Script 05 - Satisfaction vs Experience")
    print("=" * 70)
    main()