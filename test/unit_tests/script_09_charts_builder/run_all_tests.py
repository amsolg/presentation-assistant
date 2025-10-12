#!/usr/bin/env python3
"""
Script pour exécuter tous les tests du module 09_charts_builder.py
Exécute les tests unitaires pour chaque style de graphique et les fonctionnalités améliorées.
"""

import unittest
import sys
import json
from pathlib import Path
from datetime import datetime

# Ajouter le chemin du projet
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

# Importer tous les modules de test
test_modules = [
    'test_column_clustered',
    'test_line_chart',
    'test_pie_chart',
    'test_bar_clustered',
    'test_column_compact',
    'test_bar_compact',
    'test_enhanced_features'
]

def run_all_tests():
    """Exécute tous les tests et génère un rapport global"""

    # Créer le test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    results_summary = {
        "test_run": datetime.now().isoformat(),
        "test_suites": {},
        "total_tests": 0,
        "total_passed": 0,
        "total_failed": 0,
        "total_errors": 0
    }

    print("\n" + "="*70)
    print("EXÉCUTION DE TOUS LES TESTS - 09_charts_builder.py")
    print("="*70)

    for module_name in test_modules:
        print(f"\n[TEST SUITE] {module_name}")
        print("-" * 50)

        try:
            # Importer dynamiquement le module de test
            if module_name == 'test_enhanced_features':
                module_path = Path(__file__).parent / f"{module_name}.py"
            else:
                # Pour les tests dans les sous-dossiers
                style = module_name.replace('test_', '')
                module_path = Path(__file__).parent / style / f"{module_name}.py"

            if not module_path.exists():
                print(f"  [SKIP] Module non trouvé: {module_path}")
                continue

            # Charger le module
            from importlib.util import spec_from_file_location, module_from_spec
            spec = spec_from_file_location(module_name, str(module_path))
            module = module_from_spec(spec)
            spec.loader.exec_module(module)

            # Ajouter les tests au suite
            suite.addTests(loader.loadTestsFromModule(module))

            # Exécuter les tests pour ce module
            module_suite = loader.loadTestsFromModule(module)
            runner = unittest.TextTestRunner(verbosity=1, stream=sys.stdout)
            result = runner.run(module_suite)

            # Enregistrer les résultats
            results_summary["test_suites"][module_name] = {
                "tests_run": result.testsRun,
                "failures": len(result.failures),
                "errors": len(result.errors),
                "success": result.wasSuccessful()
            }

            results_summary["total_tests"] += result.testsRun
            results_summary["total_passed"] += (result.testsRun - len(result.failures) - len(result.errors))
            results_summary["total_failed"] += len(result.failures)
            results_summary["total_errors"] += len(result.errors)

        except Exception as e:
            print(f"  [ERROR] Impossible de charger {module_name}: {e}")
            results_summary["test_suites"][module_name] = {
                "error": str(e)
            }

    # Afficher le résumé
    print("\n" + "="*70)
    print("RÉSUMÉ DES TESTS")
    print("="*70)

    print(f"\nTotal des tests exécutés: {results_summary['total_tests']}")
    print(f"Tests réussis: {results_summary['total_passed']}")
    print(f"Tests échoués: {results_summary['total_failed']}")
    print(f"Erreurs: {results_summary['total_errors']}")

    print("\nDétails par suite de tests:")
    for suite_name, suite_results in results_summary["test_suites"].items():
        if "error" in suite_results:
            print(f"  - {suite_name}: [ERROR] {suite_results['error']}")
        else:
            status = "[PASS]" if suite_results["success"] else "[FAIL]"
            print(f"  - {suite_name}: {status} ({suite_results['tests_run']} tests)")

    # Sauvegarder le rapport
    report_path = Path(__file__).parent / "test_results_global.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(results_summary, f, indent=2, ensure_ascii=False)

    print(f"\n[REPORT] Rapport global sauvegardé: {report_path}")

    # Déterminer le statut global
    if results_summary["total_failed"] == 0 and results_summary["total_errors"] == 0:
        print("\n" + "="*70)
        print("[SUCCESS] TOUS LES TESTS SONT PASSÉS AVEC SUCCÈS!")
        print("="*70)
        return 0
    else:
        print("\n" + "="*70)
        print("[WARNING] Certains tests ont échoué. Consultez les détails ci-dessus.")
        print("="*70)
        return 1

if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)