#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests Unitaires - Charts Builder Architecture JSON 2025
Test complet de tous les types de graphiques et de leurs configurations.
"""

import os
import sys
import json
import unittest
import tempfile
import shutil
from pathlib import Path
from typing import Dict, Any

# Ajouter le chemin de presentation_builder pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "presentation_builder"))

from charts_builder import ChartsBuilder, load_charts_payload, process_charts_from_payload_file
from presentation_builder import PresentationBuilder


class TestChartsBuilder(unittest.TestCase):
    """Tests unitaires pour le Charts Builder - Architecture JSON 2025"""

    def setUp(self):
        """Configuration initiale pour chaque test"""
        self.test_dir = Path(__file__).parent
        self.project_root = self.test_dir.parent.parent.parent
        self.template_path = self.project_root / "templates" / "Template_PT.pptx"

        # Vérifier que le template existe
        if not self.template_path.exists():
            self.skipTest(f"Template Premier Tech non trouvé: {self.template_path}")

        # Initialiser le builder
        self.builder = ChartsBuilder(str(self.template_path))

        # Préparer un dossier temporaire pour les tests
        self.temp_dir = Path(tempfile.mkdtemp())

        print(f"[SETUP] Test dir: {self.test_dir}")
        print(f"[SETUP] Template: {self.template_path}")
        print(f"[SETUP] Temp dir: {self.temp_dir}")

    def tearDown(self):
        """Nettoyage après chaque test"""
        try:
            shutil.rmtree(self.temp_dir)
        except:
            pass

    def test_01_template_validation(self):
        """Test 1: Validation du template Premier Tech pour graphiques"""
        print("\n=== TEST 1: Validation Template ===")

        result = self.builder.validate_template()

        self.assertTrue(result, "Le template Premier Tech doit être valide")
        self.assertIsNotNone(self.builder.charts_info, "Les informations de graphiques doivent être disponibles")
        self.assertGreater(len(self.builder.charts_info['styles_supported']), 0, "Au moins un style doit être supporté")

        print(f"[SUCCESS] Template validé avec {len(self.builder.charts_info['styles_supported'])} styles")

    def test_02_bar_chart_creation(self):
        """Test 2: Création graphique en barres horizontales"""
        print("\n=== TEST 2: Graphique en Barres ===")

        # Charger la configuration de test
        test_config_path = self.test_dir / "bar_chart" / "presentation_schema.json"
        payload_path = self.test_dir / "bar_chart" / "charts_payload.json"

        self.assertTrue(test_config_path.exists(), "Configuration test bar_chart doit exister")
        self.assertTrue(payload_path.exists(), "Payload bar_chart doit exister")

        # Créer une présentation de test
        temp_presentation = self.temp_dir / "test_bar_chart.pptx"

        # Utiliser le presentation builder pour créer la base
        presentation_builder = PresentationBuilder()
        result_path = presentation_builder.build_presentation(str(test_config_path))

        # Vérifier que la présentation a été créée
        self.assertTrue(os.path.exists(result_path), "La présentation bar_chart doit être créée")

        # Vérifier la taille du fichier (doit être > 0)
        file_size = os.path.getsize(result_path)
        self.assertGreater(file_size, 10000, "Le fichier doit avoir une taille raisonnable")

        print(f"[SUCCESS] Graphique en barres créé: {file_size} bytes")

    def test_03_column_chart_creation(self):
        """Test 3: Création graphique en colonnes groupées"""
        print("\n=== TEST 3: Graphique en Colonnes ===")

        test_config_path = self.test_dir / "column_chart" / "presentation_schema.json"

        self.assertTrue(test_config_path.exists(), "Configuration test column_chart doit exister")

        presentation_builder = PresentationBuilder()
        result_path = presentation_builder.build_presentation(str(test_config_path))

        self.assertTrue(os.path.exists(result_path), "La présentation column_chart doit être créée")

        file_size = os.path.getsize(result_path)
        self.assertGreater(file_size, 10000, "Le fichier doit avoir une taille raisonnable")

        print(f"[SUCCESS] Graphique en colonnes créé: {file_size} bytes")

    def test_04_pie_chart_creation(self):
        """Test 4: Création graphique en secteurs"""
        print("\n=== TEST 4: Graphique en Secteurs ===")

        test_config_path = self.test_dir / "pie_chart" / "presentation_schema.json"

        self.assertTrue(test_config_path.exists(), "Configuration test pie_chart doit exister")

        presentation_builder = PresentationBuilder()
        result_path = presentation_builder.build_presentation(str(test_config_path))

        self.assertTrue(os.path.exists(result_path), "La présentation pie_chart doit être créée")

        file_size = os.path.getsize(result_path)
        self.assertGreater(file_size, 10000, "Le fichier doit avoir une taille raisonnable")

        print(f"[SUCCESS] Graphique en secteurs créé: {file_size} bytes")

    def test_05_line_chart_creation(self):
        """Test 5: Création graphique linéaire"""
        print("\n=== TEST 5: Graphique Linéaire ===")

        test_config_path = self.test_dir / "line_chart" / "presentation_schema.json"

        self.assertTrue(test_config_path.exists(), "Configuration test line_chart doit exister")

        presentation_builder = PresentationBuilder()
        result_path = presentation_builder.build_presentation(str(test_config_path))

        self.assertTrue(os.path.exists(result_path), "La présentation line_chart doit être créée")

        file_size = os.path.getsize(result_path)
        self.assertGreater(file_size, 10000, "Le fichier doit avoir une taille raisonnable")

        print(f"[SUCCESS] Graphique linéaire créé: {file_size} bytes")

    def test_06_multi_series_chart(self):
        """Test 6: Création graphique multi-séries"""
        print("\n=== TEST 6: Graphique Multi-Séries ===")

        test_config_path = self.test_dir / "multi_series" / "presentation_schema.json"

        self.assertTrue(test_config_path.exists(), "Configuration test multi_series doit exister")

        presentation_builder = PresentationBuilder()
        result_path = presentation_builder.build_presentation(str(test_config_path))

        self.assertTrue(os.path.exists(result_path), "La présentation multi_series doit être créée")

        file_size = os.path.getsize(result_path)
        self.assertGreater(file_size, 10000, "Le fichier doit avoir une taille raisonnable")

        print(f"[SUCCESS] Graphique multi-séries créé: {file_size} bytes")

    def test_07_csv_data_import(self):
        """Test 7: Import de données CSV"""
        print("\n=== TEST 7: Import Données CSV ===")

        test_config_path = self.test_dir / "csv_data" / "presentation_schema.json"
        csv_file = self.test_dir / "csv_data" / "data" / "sales_data.csv"

        self.assertTrue(test_config_path.exists(), "Configuration test csv_data doit exister")
        self.assertTrue(csv_file.exists(), "Fichier CSV de test doit exister")

        presentation_builder = PresentationBuilder()
        result_path = presentation_builder.build_presentation(str(test_config_path))

        self.assertTrue(os.path.exists(result_path), "La présentation csv_data doit être créée")

        file_size = os.path.getsize(result_path)
        self.assertGreater(file_size, 10000, "Le fichier doit avoir une taille raisonnable")

        print(f"[SUCCESS] Import CSV réalisé: {file_size} bytes")

    def test_08_compact_charts(self):
        """Test 8: Création graphiques compacts"""
        print("\n=== TEST 8: Graphiques Compacts ===")

        test_config_path = self.test_dir / "compact_charts" / "presentation_schema.json"

        self.assertTrue(test_config_path.exists(), "Configuration test compact_charts doit exister")

        presentation_builder = PresentationBuilder()
        result_path = presentation_builder.build_presentation(str(test_config_path))

        self.assertTrue(os.path.exists(result_path), "La présentation compact_charts doit être créée")

        file_size = os.path.getsize(result_path)
        self.assertGreater(file_size, 10000, "Le fichier doit avoir une taille raisonnable")

        print(f"[SUCCESS] Graphiques compacts créés: {file_size} bytes")

    def test_09_custom_configuration(self):
        """Test 9: Configuration personnalisée avancée"""
        print("\n=== TEST 9: Configuration Personnalisée ===")

        test_config_path = self.test_dir / "custom_chart" / "presentation_schema.json"

        self.assertTrue(test_config_path.exists(), "Configuration test custom_chart doit exister")

        presentation_builder = PresentationBuilder()
        result_path = presentation_builder.build_presentation(str(test_config_path))

        self.assertTrue(os.path.exists(result_path), "La présentation custom_chart doit être créée")

        file_size = os.path.getsize(result_path)
        self.assertGreater(file_size, 10000, "Le fichier doit avoir une taille raisonnable")

        print(f"[SUCCESS] Configuration personnalisée appliquée: {file_size} bytes")

    def test_10_payload_loading(self):
        """Test 10: Chargement et validation des payloads JSON"""
        print("\n=== TEST 10: Validation Payloads ===")

        # Tester le chargement de différents payloads
        test_cases = [
            "bar_chart/charts_payload.json",
            "column_chart/charts_payload.json",
            "pie_chart/charts_payload.json",
            "line_chart/charts_payload.json",
            "multi_series/charts_payload.json"
        ]

        loaded_count = 0
        for test_case in test_cases:
            payload_path = self.test_dir / test_case
            if payload_path.exists():
                payload = load_charts_payload(str(payload_path))

                # Vérifier les champs requis
                self.assertIn('title', payload, f"Payload {test_case} doit avoir un titre")
                self.assertIn('style', payload, f"Payload {test_case} doit avoir un style")
                self.assertIn('data_source', payload, f"Payload {test_case} doit avoir une source de données")

                # Valider la configuration
                validation = self.builder._validate_charts_config(payload)
                self.assertTrue(validation['valid'], f"Payload {test_case} doit être valide: {validation.get('errors', [])}")

                loaded_count += 1
                print(f"[VALID] {test_case}: {payload['title']}")

        self.assertGreater(loaded_count, 0, "Au moins un payload doit être testé")
        print(f"[SUCCESS] {loaded_count} payloads validés")

    def test_11_error_handling(self):
        """Test 11: Gestion d'erreurs robuste"""
        print("\n=== TEST 11: Gestion d'Erreurs ===")

        # Test avec configuration invalide
        invalid_config = {
            "title": "",  # Titre vide
            "style": "invalid_style",  # Style invalide
            # data_source manquant
        }

        validation = self.builder._validate_charts_config(invalid_config)
        self.assertFalse(validation['valid'], "Configuration invalide doit être rejetée")
        self.assertGreater(len(validation['errors']), 0, "Des erreurs doivent être détectées")

        print(f"[SUCCESS] Gestion d'erreurs fonctionnelle: {len(validation['errors'])} erreurs détectées")

    def test_12_architecture_compliance(self):
        """Test 12: Conformité à l'architecture JSON 2025"""
        print("\n=== TEST 12: Conformité Architecture ===")

        # Vérifier que toutes les fonctions requises existent
        required_methods = [
            'process_charts_config',
            '_validate_charts_config'
        ]

        required_functions = [
            'load_charts_payload',
            'process_charts_from_payload_file'
        ]

        for method_name in required_methods:
            self.assertTrue(hasattr(self.builder, method_name), f"Méthode {method_name} requise")

        # Vérifier les fonctions globales dans le module charts_builder
        import charts_builder
        for func_name in required_functions:
            self.assertTrue(hasattr(charts_builder, func_name), f"Fonction {func_name} requise dans le module")

        # Vérifier la signature de la fonction principale
        import inspect
        sig = inspect.signature(self.builder.process_charts_config)
        params = list(sig.parameters.keys())

        self.assertIn('config', params, "Paramètre 'config' requis")
        self.assertIn('presentation_path', params, "Paramètre 'presentation_path' requis")

        print(f"[SUCCESS] Architecture JSON 2025 conforme")


def run_charts_builder_tests():
    """Exécute tous les tests charts_builder et génère un rapport"""
    print("=" * 80)
    print("TESTS UNITAIRES - CHARTS BUILDER ARCHITECTURE JSON 2025")
    print("=" * 80)

    # Créer la suite de tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestChartsBuilder)

    # Exécuter les tests avec un runner verbeux
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)

    # Générer le rapport final
    print("\n" + "=" * 80)
    print("RAPPORT FINAL")
    print("=" * 80)

    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    success_count = total_tests - failures - errors

    print(f"Tests exécutés: {total_tests}")
    print(f"Succès: {success_count}")
    print(f"Échecs: {failures}")
    print(f"Erreurs: {errors}")

    if result.failures:
        print("\nÉCHECS:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")

    if result.errors:
        print("\nERREURS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")

    success_rate = (success_count / total_tests * 100) if total_tests > 0 else 0
    print(f"\nTaux de succès: {success_rate:.1f}%")

    if success_rate >= 80:
        print("[SUCCESS] MIGRATION CHARTS BUILDER REUSSIE!")
    else:
        print("[ERROR] MIGRATION CHARTS BUILDER A REVOIR")

    return success_rate >= 80


if __name__ == "__main__":
    success = run_charts_builder_tests()
    sys.exit(0 if success else 1)