#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests unitaires pour le Testimonial Builder - Architecture JSON 2025
Tests exhaustifs pour valider la migration vers l'architecture JSON moderne.
"""

import os
import sys
import json
import unittest
import tempfile
import shutil
from pathlib import Path
from datetime import datetime

# Ajouter le chemin des modules
script_dir = Path(__file__).parent.parent.parent.parent / "presentation_builder"
sys.path.insert(0, str(script_dir))

from testimonial_builder import (
    TestimonialBuilder,
    create_testimonial_from_json,
    load_testimonial_template,
    load_testimonial_payload,
    process_testimonial_from_payload_file
)


class TestTestimonialBuilder(unittest.TestCase):
    """Tests exhaustifs pour le Testimonial Builder JSON 2025"""

    @classmethod
    def setUpClass(cls):
        """Configuration initiale pour tous les tests"""
        cls.project_root = Path(__file__).parent.parent.parent.parent
        cls.template_path = cls.project_root / "templates" / "Template_PT.pptx"
        cls.test_dir = Path(__file__).parent

        # Créer un dossier temporaire pour les tests
        cls.temp_dir = Path(tempfile.mkdtemp(prefix="testimonial_test_"))

        print(f"[TEST SETUP] Dossier temporaire: {cls.temp_dir}")
        print(f"[TEST SETUP] Template: {cls.template_path}")

    @classmethod
    def tearDownClass(cls):
        """Nettoyage après tous les tests"""
        if cls.temp_dir.exists():
            shutil.rmtree(cls.temp_dir)
            print(f"[TEST CLEANUP] Dossier temporaire supprimé")

    def setUp(self):
        """Configuration avant chaque test"""
        self.builder = TestimonialBuilder(str(self.template_path))
        self.test_presentation_path = self.temp_dir / f"test_presentation_{datetime.now().strftime('%H%M%S')}.pptx"

    def test_01_template_validation(self):
        """Test 1: Validation du template Premier Tech pour témoignages"""
        print("\n[TEST 1] Validation template Premier Tech...")

        # Vérifier que le template existe
        self.assertTrue(self.template_path.exists(), "Template Premier Tech doit exister")

        # Valider avec le builder
        is_valid = self.builder.validate_template()
        self.assertTrue(is_valid, "Template doit être valide pour témoignages")

        # Vérifier les informations du témoignage
        self.assertIsNotNone(self.builder.testimonial_info, "Informations témoignage doivent être disponibles")
        self.assertEqual(self.builder.testimonial_slide_index, 44, "Index slide témoignage doit être 44")
        self.assertEqual(self.builder.testimonial_info['slide_number'], 45, "Numéro slide témoignage doit être 45")

        print(f"[SUCCESS] Template validé - Slide {self.builder.testimonial_info['slide_number']} ({self.builder.testimonial_info['layout_name']})")

    def test_02_json_config_validation(self):
        """Test 2: Validation des configurations JSON de témoignages"""
        print("\n[TEST 2] Validation configurations JSON...")

        # Configuration valide
        valid_config = {
            "quote_text": "Témoignage de test valide pour validation.",
            "author": "Test Auteur",
            "position": "Test Position",
            "company": "Test Company",
            "style": "standard",
            "options": {"auto_widen": True}
        }

        validation_result = self.builder._validate_testimonial_config(valid_config)
        self.assertTrue(validation_result['valid'], "Configuration valide doit passer la validation")
        self.assertEqual(len(validation_result['errors']), 0, "Aucune erreur pour configuration valide")

        # Configuration invalide - citation manquante
        invalid_config_1 = {
            "author": "Test Auteur"
        }

        validation_result = self.builder._validate_testimonial_config(invalid_config_1)
        self.assertFalse(validation_result['valid'], "Configuration sans citation doit échouer")
        self.assertGreater(len(validation_result['errors']), 0, "Erreurs attendues pour citation manquante")

        # Configuration invalide - auteur manquant
        invalid_config_2 = {
            "quote_text": "Citation sans auteur"
        }

        validation_result = self.builder._validate_testimonial_config(invalid_config_2)
        self.assertFalse(validation_result['valid'], "Configuration sans auteur doit échouer")

        # Configuration invalide - citation trop courte
        invalid_config_3 = {
            "quote_text": "Court",
            "author": "Test Auteur"
        }

        validation_result = self.builder._validate_testimonial_config(invalid_config_3)
        self.assertFalse(validation_result['valid'], "Citation trop courte doit échouer")

        print(f"[SUCCESS] Validation JSON - Configurations testées avec succès")

    def test_03_client_testimonial_creation(self):
        """Test 3: Création d'un témoignage client complet"""
        print("\n[TEST 3] Création témoignage client...")

        # Charger la configuration client
        payload_path = self.test_dir / "client_testimonial" / "testimonial_payload.json"
        self.assertTrue(payload_path.exists(), "Payload client testimonial doit exister")

        # Créer une présentation de base d'abord
        self._create_base_presentation()

        # Traiter le témoignage
        result = process_testimonial_from_payload_file(
            str(payload_path),
            str(self.test_presentation_path),
            str(self.template_path)
        )

        self.assertTrue(result.get('success', False), f"Traitement doit réussir: {result.get('error', 'Aucune erreur')}")
        self.assertIn('processing_details', result, "Détails de traitement attendus")

        # Vérifier que le fichier existe et est valide
        self.assertTrue(self.test_presentation_path.exists(), "Fichier de présentation doit exister")
        self.assertGreater(self.test_presentation_path.stat().st_size, 10000, "Fichier doit avoir une taille significative")

        print(f"[SUCCESS] Témoignage client créé: {self.test_presentation_path}")

    def test_04_quote_testimonial_creation(self):
        """Test 4: Création d'une citation courte"""
        print("\n[TEST 4] Création citation courte...")

        # Charger la configuration quote
        payload_path = self.test_dir / "quote_testimonial" / "testimonial_payload.json"
        self.assertTrue(payload_path.exists(), "Payload quote testimonial doit exister")

        # Créer une présentation de base d'abord
        self._create_base_presentation()

        # Traiter la citation
        result = process_testimonial_from_payload_file(
            str(payload_path),
            str(self.test_presentation_path),
            str(self.template_path)
        )

        self.assertTrue(result.get('success', False), f"Traitement doit réussir: {result.get('error', 'Aucune erreur')}")

        # Vérifier que le fichier existe
        self.assertTrue(self.test_presentation_path.exists(), "Fichier de présentation doit exister")

        print(f"[SUCCESS] Citation courte créée: {self.test_presentation_path}")

    def test_05_expert_testimonial_creation(self):
        """Test 5: Création d'un témoignage d'expert"""
        print("\n[TEST 5] Création témoignage expert...")

        # Charger la configuration expert
        payload_path = self.test_dir / "expert_testimonial" / "testimonial_payload.json"
        self.assertTrue(payload_path.exists(), "Payload expert testimonial doit exister")

        # Créer une présentation de base d'abord
        self._create_base_presentation()

        # Traiter le témoignage expert
        result = process_testimonial_from_payload_file(
            str(payload_path),
            str(self.test_presentation_path),
            str(self.template_path)
        )

        self.assertTrue(result.get('success', False), f"Traitement doit réussir: {result.get('error', 'Aucune erreur')}")

        # Vérifier contenu spécifique à l'expert
        processing_details = result.get('processing_details', {})
        self.assertIn('title_applied', processing_details, "Titre expert doit être appliqué")
        self.assertEqual(processing_details.get('title_applied'), "Avis d'Expert", "Titre doit être 'Avis d'Expert'")

        print(f"[SUCCESS] Témoignage expert créé avec titre: {processing_details.get('title_applied')}")

    def test_06_custom_testimonial_creation(self):
        """Test 6: Création d'un témoignage personnalisé"""
        print("\n[TEST 6] Création témoignage personnalisé...")

        # Charger la configuration custom
        payload_path = self.test_dir / "custom_testimonial" / "testimonial_payload.json"
        self.assertTrue(payload_path.exists(), "Payload custom testimonial doit exister")

        # Créer une présentation de base d'abord
        self._create_base_presentation()

        # Traiter le témoignage personnalisé
        result = process_testimonial_from_payload_file(
            str(payload_path),
            str(self.test_presentation_path),
            str(self.template_path)
        )

        self.assertTrue(result.get('success', False), f"Traitement doit réussir: {result.get('error', 'Aucune erreur')}")

        # Vérifier configuration personnalisée
        processing_details = result.get('processing_details', {})
        self.assertIn('insert_position', processing_details, "Position d'insertion doit être spécifiée")
        self.assertEqual(processing_details.get('insert_position'), 5, "Position doit être 5")

        print(f"[SUCCESS] Témoignage personnalisé créé à la position: {processing_details.get('insert_position')}")

    def test_07_template_loading_functions(self):
        """Test 7: Fonctions de chargement de templates"""
        print("\n[TEST 7] Test fonctions de chargement...")

        # Test de chargement de templates prédéfinis
        templates_to_test = ["client_testimonial", "expert_testimonial", "quote_testimonial", "custom_testimonial"]

        for template_name in templates_to_test:
            template_config = load_testimonial_template(template_name)

            self.assertIsInstance(template_config, dict, f"Template {template_name} doit être un dictionnaire")
            self.assertIn('quote_text', template_config, f"Template {template_name} doit avoir quote_text")
            self.assertIn('author', template_config, f"Template {template_name} doit avoir author")
            self.assertIn('style', template_config, f"Template {template_name} doit avoir style")

            print(f"[SUCCESS] Template {template_name} chargé: {template_config['author']}")

        # Test de fallback pour template inexistant
        fallback_config = load_testimonial_template("nonexistent_template")
        self.assertIsInstance(fallback_config, dict, "Fallback doit retourner un dictionnaire")
        self.assertIn('quote_text', fallback_config, "Fallback doit avoir quote_text")

        print(f"[SUCCESS] Fallback template fonctionne correctement")

    def test_08_direct_json_processing(self):
        """Test 8: Traitement direct depuis JSON avec create_testimonial_from_json"""
        print("\n[TEST 8] Traitement JSON direct...")

        # Configuration de test directe
        test_config = {
            "quote_text": "Test de traitement JSON direct pour validation de l'architecture 2025.",
            "author": "Test Direct",
            "position": "Testeur JSON",
            "company": "Direct Test Corp",
            "testimonial_title": "Test Direct",
            "style": "standard",
            "options": {
                "auto_widen": True,
                "text_wrapping": {
                    "quote_wrapping": True,
                    "attribution_wrapping": False
                }
            }
        }

        # Créer une présentation de base d'abord
        self._create_base_presentation()

        # Traitement direct
        result = create_testimonial_from_json(
            test_config,
            str(self.test_presentation_path),
            str(self.template_path)
        )

        self.assertTrue(result.get('success', False), f"Traitement JSON direct doit réussir: {result.get('error', 'Aucune erreur')}")

        # Vérifier les détails de configuration
        self.assertIn('configuration', result, "Configuration doit être incluse dans le résultat")
        self.assertIn('validation', result, "Validation doit être incluse dans le résultat")

        # Vérifier que la validation a réussi
        validation = result.get('validation', {})
        self.assertTrue(validation.get('valid', False), "Validation de configuration doit réussir")

        print(f"[SUCCESS] Traitement JSON direct réussi - Config validée: {validation.get('valid')}")

    def _create_base_presentation(self):
        """Crée une présentation de base pour les tests d'insertion"""
        try:
            # Utiliser la logique du script 01 pour créer une présentation de base
            import importlib.util
            slide_creator_path = self.project_root / "presentation_builder" / "01_slide_title_creator.py"
            spec = importlib.util.spec_from_file_location("slide_title_creator", slide_creator_path)
            slide_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(slide_module)
            SlideTitleCreator = slide_module.SlideTitleCreator

            # Créer le dossier parent
            os.makedirs(self.test_presentation_path.parent, exist_ok=True)

            # Créer la présentation de base
            creator = SlideTitleCreator()
            creator.create_title_slide(
                title="Test Presentation pour Testimonial",
                subtitle="Test Unitaire",
                metadata="2025-01-15 – Test",
                output_path=str(self.test_presentation_path),
                auto_widen=True
            )

            return True

        except Exception as e:
            print(f"[ERROR] Erreur création présentation de base: {e}")
            return False


def run_testimonial_tests():
    """Exécute tous les tests du Testimonial Builder"""
    print("=== TESTS TESTIMONIAL BUILDER - ARCHITECTURE JSON 2025 ===")

    # Configuration du test runner
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestTestimonialBuilder)

    # Exécution avec rapport détaillé
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)

    # Rapport final
    print(f"\n=== RAPPORT FINAL ===")
    print(f"Tests exécutés: {result.testsRun}")
    print(f"Échecs: {len(result.failures)}")
    print(f"Erreurs: {len(result.errors)}")
    print(f"Succès: {result.testsRun - len(result.failures) - len(result.errors)}")

    if result.failures:
        print(f"\nÉCHECS:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")

    if result.errors:
        print(f"\nERREURS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")

    success_rate = (result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100
    print(f"\nTaux de succès: {success_rate:.1f}%")

    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_testimonial_tests()
    sys.exit(0 if success else 1)