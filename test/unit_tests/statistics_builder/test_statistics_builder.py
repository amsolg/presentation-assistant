#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests unitaires pour Statistics Builder - Architecture JSON 2025
Teste le nouveau script statistics_builder.py avec différentes configurations JSON.
"""

import os
import sys
import json
import unittest
from pathlib import Path
from datetime import datetime

# Ajouter le chemin vers presentation_builder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'presentation_builder'))

try:
    from statistics_builder import StatisticsBuilder, process_statistics_from_payload_file
    from presentation_builder import PresentationBuilder

except ImportError as e:
    print(f"[ERROR] Impossible d'importer les modules requis: {e}")
    sys.exit(1)


class TestStatisticsBuilder(unittest.TestCase):
    """Tests pour le StatisticsBuilder avec architecture JSON 2025"""

    def setUp(self):
        """Configuration initiale pour chaque test"""
        self.template_path = os.path.join('..', '..', '..', 'templates', 'Template_PT.pptx')
        self.test_subject = "unit-tests"
        self.test_audience = "statistics_builder_tester"

        # Créer le dossier de sortie
        self.output_dir = os.path.join('output')
        os.makedirs(self.output_dir, exist_ok=True)

        # Timestamp pour l'unicité des fichiers
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def _create_presentation_from_schema(self, test_name: str) -> str:
        """Crée une présentation complète à partir du schéma JSON"""
        try:
            # Créer le PresentationBuilder
            builder = PresentationBuilder()

            # Changer vers le répertoire du test pour les chemins relatifs des payloads
            original_cwd = os.getcwd()
            os.chdir(os.path.dirname(__file__))

            # Construire la présentation
            schema_path = os.path.join(test_name, 'presentation_schema.json')
            output_path = builder.build_presentation(schema_path)

            # Retourner au répertoire original
            os.chdir(original_cwd)

            return output_path

        except Exception as e:
            print(f"[ERROR] Erreur création présentation {test_name}: {e}")
            if 'original_cwd' in locals():
                os.chdir(original_cwd)
            raise

    def _validate_presentation_file(self, file_path: str) -> bool:
        """Valide qu'un fichier PowerPoint existe et est valide"""
        if not os.path.exists(file_path):
            print(f"[ERROR] Fichier non trouvé: {file_path}")
            return False

        # Vérifier la taille minimale (doit contenir au moins quelque chose)
        file_size = os.path.getsize(file_path)
        if file_size < 10000:  # Moins de 10KB
            print(f"[ERROR] Fichier trop petit: {file_size} bytes")
            return False

        # Essayer d'ouvrir avec python-pptx
        try:
            from pptx import Presentation
            pres = Presentation(file_path)
            slide_count = len(pres.slides)
            print(f"[INFO] Présentation valide: {slide_count} slides")

            # Vérifier qu'on a au moins 3 slides (titre + contenu + fermeture)
            if slide_count < 3:
                print(f"[WARNING] Présentation a seulement {slide_count} slides")
                return False

            return True

        except Exception as e:
            print(f"[ERROR] Erreur ouverture PowerPoint: {e}")
            return False

    def test_01_two_stats_blue_line(self):
        """Test: 2 statistiques avec ligne bleue"""
        print(f"\n=== Test 1: 2 statistiques blue_line ===")
        test_name = "stats_2_blue"

        output_path = self._create_presentation_from_schema(test_name)
        self.assertTrue(self._validate_presentation_file(output_path),
                       "Présentation 2 stats blue_line invalide")

        print(f"[SUCCESS] Test {test_name} réussi: {output_path}")

    def test_02_two_stats_grey_line(self):
        """Test: 2 statistiques avec ligne grise"""
        print(f"\n=== Test 2: 2 statistiques grey_line ===")
        test_name = "stats_2_grey"

        output_path = self._create_presentation_from_schema(test_name)
        self.assertTrue(self._validate_presentation_file(output_path),
                       "Présentation 2 stats grey_line invalide")

        print(f"[SUCCESS] Test {test_name} réussi: {output_path}")

    def test_03_three_stats(self):
        """Test: 3 statistiques avec mots-clés"""
        print(f"\n=== Test 3: 3 statistiques three_stats ===")
        test_name = "stats_3"

        output_path = self._create_presentation_from_schema(test_name)
        self.assertTrue(self._validate_presentation_file(output_path),
                       "Présentation 3 stats invalide")

        print(f"[SUCCESS] Test {test_name} réussi: {output_path}")

    def test_04_four_stats(self):
        """Test: 4 statistiques dashboard"""
        print(f"\n=== Test 4: 4 statistiques four_stats ===")
        test_name = "stats_4"

        output_path = self._create_presentation_from_schema(test_name)
        self.assertTrue(self._validate_presentation_file(output_path),
                       "Présentation 4 stats invalide")

        print(f"[SUCCESS] Test {test_name} réussi: {output_path}")

    def test_05_four_stats_lines(self):
        """Test: 4 statistiques premium avec lignes"""
        print(f"\n=== Test 5: 4 statistiques four_stats_lines ===")
        test_name = "stats_4_lines"

        output_path = self._create_presentation_from_schema(test_name)
        self.assertTrue(self._validate_presentation_file(output_path),
                       "Présentation 4 stats lines invalide")

        print(f"[SUCCESS] Test {test_name} réussi: {output_path}")

    def test_06_statistics_builder_validation(self):
        """Test: Validation des configurations JSON"""
        print(f"\n=== Test 6: Validation JSON ===")

        builder = StatisticsBuilder(self.template_path)

        # Test configuration valide
        valid_config = {
            "style": "blue_line",
            "statistics": [
                {"value": "85%", "label": "Satisfaction"},
                {"value": "127M$", "label": "Revenue"}
            ]
        }

        validation = builder._validate_statistics_config(valid_config)
        self.assertTrue(validation["valid"], "Configuration valide rejetée")

        # Test configuration invalide (style inexistant)
        invalid_config = {
            "style": "invalid_style",
            "statistics": [
                {"value": "85%", "label": "Satisfaction"},
                {"value": "127M$", "label": "Revenue"}
            ]
        }

        validation = builder._validate_statistics_config(invalid_config)
        self.assertFalse(validation["valid"], "Configuration invalide acceptée")

        print(f"[SUCCESS] Validation JSON réussie")

    def test_07_payload_processing(self):
        """Test: Traitement des payloads JSON"""
        print(f"\n=== Test 7: Traitement payload JSON ===")

        # Tester avec le payload stats_2_blue
        original_cwd = os.getcwd()
        try:
            os.chdir(os.path.dirname(__file__))

            # Créer une présentation de base pour le test
            builder = PresentationBuilder()
            base_presentation = builder.build_presentation("stats_2_blue/presentation_schema.json")

            # Vérifier que la présentation de base existe
            self.assertTrue(os.path.exists(base_presentation), "Présentation de base non créée")

            # Tester le traitement direct du payload
            payload_path = "stats_2_blue/statistics_payload.json"
            result = process_statistics_from_payload_file(
                payload_path=payload_path,
                presentation_path=base_presentation,
                template_path=self.template_path
            )

            self.assertTrue(result.get("success", False), "Traitement payload échoué")

            print(f"[SUCCESS] Traitement payload réussi")

        finally:
            os.chdir(original_cwd)

    def test_08_template_validation(self):
        """Test: Validation du template Premier Tech"""
        print(f"\n=== Test 8: Validation template ===")

        builder = StatisticsBuilder(self.template_path)
        is_valid = builder.validate_template()

        self.assertTrue(is_valid, "Template Premier Tech invalide")

        # Vérifier que tous les styles sont disponibles
        expected_styles = ["blue_line", "grey_line", "three_stats", "four_stats", "four_stats_lines"]
        statistics_info = builder.statistics_info

        for slide_index, slide_data in builder.statistics_slides.items():
            style = slide_data['style']
            self.assertIn(style, expected_styles, f"Style {style} inattendu")
            self.assertIn(slide_index, statistics_info, f"Slide {slide_index} non analysée")

        print(f"[SUCCESS] Template validation réussie")


class TestStatisticsBuilderPerformance(unittest.TestCase):
    """Tests de performance pour le StatisticsBuilder"""

    def setUp(self):
        """Configuration pour les tests de performance"""
        self.template_path = os.path.join('..', '..', '..', 'templates', 'Template_PT.pptx')

    def test_01_loading_performance(self):
        """Test: Performance de chargement du builder"""
        print(f"\n=== Test Performance: Chargement ===")

        start_time = datetime.now()
        builder = StatisticsBuilder(self.template_path)
        end_time = datetime.now()

        loading_time = (end_time - start_time).total_seconds()
        print(f"[INFO] Temps de chargement: {loading_time:.3f}s")

        # Le chargement doit être rapide (moins de 2 secondes)
        self.assertLess(loading_time, 2.0, "Chargement trop lent")

        print(f"[SUCCESS] Performance de chargement acceptable")


def run_all_tests():
    """Lance tous les tests"""
    print("=== TESTS STATISTICS BUILDER - Architecture JSON 2025 ===")

    # Créer la suite de tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Ajouter les tests principaux
    suite.addTests(loader.loadTestsFromTestCase(TestStatisticsBuilder))
    suite.addTests(loader.loadTestsFromTestCase(TestStatisticsBuilderPerformance))

    # Lancer les tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Résumé des résultats
    tests_run = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    success_count = tests_run - failures - errors

    print(f"\n=== RÉSULTATS ===")
    print(f"Tests exécutés: {tests_run}")
    print(f"Succès: {success_count}")
    print(f"Échecs: {failures}")
    print(f"Erreurs: {errors}")

    if failures > 0:
        print(f"\nÉCHECS:")
        for test, error in result.failures:
            print(f"- {test}: {error}")

    if errors > 0:
        print(f"\nERREURS:")
        for test, error in result.errors:
            print(f"- {test}: {error}")

    # Retourner True si tous les tests passent
    return failures == 0 and errors == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)