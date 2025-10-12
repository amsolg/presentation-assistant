#!/usr/bin/env python3
"""
Test unitaire pour le script 06 - Content Boxes Builder
Test d'ajout de slide 34 (4 boîtes bleues sans sous-titres Premier Tech)

Ce test vérifie la capacité du script 06 à ajouter une slide avec 4 boîtes bleues
sans sous-titres dans une présentation existante en utilisant le template slide 34.

Workflow du test:
1. Créer une présentation de base avec le script 01
2. Ajouter une slide content boxes avec le script 06 (slide 34)
3. Vérifier le résultat
"""

import os
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path
from datetime import datetime

# Ajouter le répertoire racine au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))

class TestSlide34BlueSimple:
    """
    Classe de test pour vérifier l'ajout de slide 34 avec le script 06.
    """

    def __init__(self):
        self.test_name = "Test Unitaire - Script 06 - Slide 34"
        self.script_01_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "01_slide_title_creator.py"
        self.script_06_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "06_content_boxes_builder.py"
        self.test_output_dir = Path(__file__).parent / "output"
        self.test_output_dir.mkdir(exist_ok=True)

    def setup_test(self):
        """Prépare l'environnement de test"""
        print(f"DEBUT du test: {self.test_name}")
        print(f"DOSSIER Repertoire de sortie: {self.test_output_dir}")
        print(f"SCRIPT Script 01 (base): {self.script_01_path}")
        print(f"SCRIPT Script 06 (teste): {self.script_06_path}")

        # Vérifier que les scripts existent
        if not self.script_01_path.exists():
            raise FileNotFoundError(f"Script 01 non trouve: {self.script_01_path}")
        if not self.script_06_path.exists():
            raise FileNotFoundError(f"Script 06 non trouve: {self.script_06_path}")

    def create_base_presentation(self):
        """
        Crée une présentation de base avec le script 01.

        Returns:
            Path: Chemin vers la présentation créée, ou None si échec
        """
        try:
            print(f"CREATION Etape 1: Creation de la presentation de base...")

            # Paramètres pour la présentation de base
            base_title = "TEST UNITAIRE - Script 06"
            base_subtitle = "Presentation de base pour test content boxes"
            base_metadata = f"{datetime.now().strftime('%Y.%m.%d')} - Test Content Boxes"
            base_project = "test_script_06_slide_34"

            # Chemin de sortie pour la présentation de base
            base_output_path = self.test_output_dir / f"{base_project}.pptx"

            # Commande pour créer la présentation de base
            cmd_01 = [
                sys.executable,
                str(self.script_01_path),
                base_title,
                "--subtitle", base_subtitle,
                "--metadata", base_metadata,
                "--project", base_project,
                "--output", str(base_output_path)
            ]

            print(f"EXEC Creation de la base:")
            print(f"   {' '.join(cmd_01)}")

            # Exécuter le script 01 depuis son répertoire
            result = subprocess.run(
                cmd_01,
                cwd=self.script_01_path.parent,
                capture_output=True,
                text=True,
                timeout=60
            )

            # Vérifier le résultat
            if result.returncode != 0:
                print(f"ERREUR Erreur lors de la creation de base:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return None

            # Vérifier que le fichier de base a été créé
            if not base_output_path.exists():
                print(f"ERREUR Fichier de base non cree: {base_output_path}")
                return None

            print(f"SUCCES Presentation de base creee:")
            print(f"   FICHIER Fichier: {base_output_path}")
            print(f"   TAILLE Taille: {base_output_path.stat().st_size:,} bytes")

            return base_output_path

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de la creation de base")
            return None
        except Exception as e:
            print(f"ERREUR Erreur lors de la creation de base: {e}")
            return None

    def add_content_boxes_slide(self, base_presentation_path):
        """
        Ajoute une slide content boxes avec le script 06.

        Args:
            base_presentation_path (Path): Chemin vers la présentation de base

        Returns:
            bool: True si l'ajout réussit, False sinon
        """
        try:
            print(f"CONTENT Etape 2: Ajout de la slide content boxes...")

            # Paramètres du test pour 4 boîtes bleues sans sous-titres
            title = "Méthodologie agile complète pour la gestion de projets technologiques d'envergure"
            concept1 = "Planification stratégique avec analyse approfondie des besoins, définition des objectifs SMART et élaboration de roadmaps détaillées pour garantir l'alignement organisationnel."
            concept2 = "Exécution méthodique avec équipes cross-fonctionnelles, gestion des sprints agile et coordination continue des livrables pour respecter les échéances critiques."
            concept3 = "Contrôle qualité rigoureux avec indicateurs de performance clés, revues régulières des jalons et ajustements proactifs pour maintenir la trajectoire stratégique."
            concept4 = "Amélioration continue avec retours d'expérience structurés, optimisation des processus et capitalisation des apprentissages pour excellence opérationnelle durable."

            # Commande pour ajouter la slide content boxes
            cmd_06 = [
                sys.executable,
                str(self.script_06_path),
                "--insert-into", str(base_presentation_path),
                concept1,
                concept2,
                concept3,
                "--concept4", concept4,
                "--title", title,
                "--style", "blue_4_simple"
            ]

            print(f"EXEC Ajout de content boxes:")
            print(f"   {' '.join(cmd_06)}")

            # Exécuter le script 06 depuis la racine du projet
            project_root = self.script_06_path.parent.parent
            result = subprocess.run(
                cmd_06,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=60
            )

            # Vérifier le résultat
            if result.returncode != 0:
                print(f"ERREUR Erreur lors de l'ajout de content boxes:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return False

            # Vérifier que le fichier a été modifié
            if not base_presentation_path.exists():
                print(f"ERREUR Fichier de presentation perdu: {base_presentation_path}")
                return False

            print(f"SUCCES Content boxes ajoutee avec succes!")
            print(f"   FICHIER Fichier modifie: {base_presentation_path}")
            print(f"   TAILLE Nouvelle taille: {base_presentation_path.stat().st_size:,} bytes")
            print(f"   CONTENU Concepts: {concept1}, {concept2}, {concept3}, {concept4}")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de l'ajout de content boxes")
            return False
        except Exception as e:
            print(f"ERREUR Erreur lors de l'ajout de content boxes: {e}")
            return False

    def run_validation_test(self):
        """
        Exécute le test de validation du script 06.

        Returns:
            bool: True si la validation réussit, False sinon
        """
        try:
            print(f"TEST Test de validation du script 06...")

            # Commande de validation
            cmd = [
                sys.executable,
                str(self.script_06_path),
                "dummy1",
                "dummy2",
                "dummy3",
                "--validate"
            ]

            print(f"EXEC Execution de la validation:")
            print(f"   {' '.join(cmd)}")

            # Exécuter la validation depuis la racine du projet
            project_root = self.script_06_path.parent.parent
            result = subprocess.run(
                cmd,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=30
            )

            # Vérifier le résultat
            if result.returncode != 0:
                print(f"ERREUR Erreur lors de la validation:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return False

            print(f"SUCCES Validation reussie!")
            print(f"   RESULTAT Script 06 valide avec succes")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de la validation")
            return False
        except Exception as e:
            print(f"ERREUR Erreur lors de la validation: {e}")
            return False

    def cleanup_test(self):
        """Nettoie les fichiers de test si nécessaire"""
        print(f"NETTOIE Nettoyage termine")
        print(f"DOSSIER Les fichiers de test sont conserves dans: {self.test_output_dir}")

    def run_all_tests(self):
        """
        Exécute tous les tests pour le script 06.

        Returns:
            bool: True si tous les tests réussissent, False sinon
        """
        try:
            self.setup_test()

            # Test 1: Validation du script
            validation_success = self.run_validation_test()

            # Test 2: Création de présentation de base
            base_presentation_path = self.create_base_presentation()
            base_creation_success = base_presentation_path is not None

            # Test 3: Ajout de content boxes (seulement si la base est créée)
            content_boxes_success = False
            if base_creation_success:
                content_boxes_success = self.add_content_boxes_slide(base_presentation_path)

            self.cleanup_test()

            # Résultat final
            all_success = validation_success and base_creation_success and content_boxes_success

            print(f"\n{'='*60}")
            print(f"STATS RESULTATS DU TEST - {self.test_name}")
            print(f"{'='*60}")
            print(f"TEST Validation script: {'SUCCES REUSSI' if validation_success else 'ERREUR ECHEC'}")
            print(f"CREATION Creation base (script 01): {'SUCCES REUSSI' if base_creation_success else 'ERREUR ECHEC'}")
            print(f"CONTENT Ajout content boxes (script 06): {'SUCCES REUSSI' if content_boxes_success else 'ERREUR ECHEC'}")
            print(f"FINAL Resultat global: {'SUCCES TOUS LES TESTS REUSSIS' if all_success else 'ERREUR ECHECS DETECTES'}")
            print(f"{'='*60}")

            return all_success

        except Exception as e:
            print(f"ERREUR Erreur critique dans les tests: {e}")
            return False


def main():
    """Point d'entrée principal pour exécuter les tests"""
    test_runner = TestSlide34BlueSimple()
    success = test_runner.run_all_tests()

    # Code de retour approprié
    exit_code = 0 if success else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()