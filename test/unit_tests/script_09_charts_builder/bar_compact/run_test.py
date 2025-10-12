#!/usr/bin/env python3
"""
Script d'exécution pour le test unitaire du style bar_compact
Test du script 09_charts_builder.py pour les graphiques en barres compactes.

Ce test valide:
1. Comparaisons rapides
2. Classement Top 5 compact
3. Comparaisons binaires
4. Scores de satisfaction
5. Indicateurs de progression
"""

import sys
import unittest
from pathlib import Path

# Ajouter le répertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer le test
from test_bar_compact import TestBarCompactChart

def main():
    """Fonction principale pour exécuter les tests"""
    print("Execution du test unitaire - Bar Compact Chart")
    print("=" * 60)

    # Créer une suite de tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestBarCompactChart)

    # Exécuter les tests avec un runner verbeux
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)

    # Afficher le résumé
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print(f"SUCCESS: Tous les {result.testsRun} tests ont réussi")
        return 0
    else:
        print(f"ÉCHEC: {len(result.failures)} échec(s), {len(result.errors)} erreur(s) sur {result.testsRun} tests")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)