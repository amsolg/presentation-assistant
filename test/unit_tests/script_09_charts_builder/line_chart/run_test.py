#!/usr/bin/env python3
"""
Script d'exécution pour le test unitaire du style line_chart
Test du script 09_charts_builder.py pour les graphiques linéaires.

Ce test valide:
1. Évolutions temporelles
2. Multi-séries pour comparaisons
3. Configuration JSON
4. Analyse de tendances
5. Patterns saisonniers
"""

import sys
import unittest
from pathlib import Path

# Ajouter le répertoire du test au path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir))

# Importer le test
from test_line_chart import TestLineChart

def main():
    """Fonction principale pour exécuter les tests"""
    print("Execution du test unitaire - Line Chart")
    print("=" * 60)

    # Créer une suite de tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLineChart)

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
