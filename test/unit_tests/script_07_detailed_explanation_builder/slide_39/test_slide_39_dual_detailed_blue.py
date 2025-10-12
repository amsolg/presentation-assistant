#!/usr/bin/env python3
"""
Test unitaire pour le script 07 - Detailed Explanation Builder
Test d'ajout de slide 39 (2 énoncés avec sous-titres et ligne bleue Premier Tech)

Ce test vérifie la capacité du script 07 à ajouter une slide d'explication détaillée
dans une présentation existante en utilisant le template slide 39 (dual_detailed_blue).

Workflow du test:
1. Créer une présentation de base avec le script 01
2. Ajouter une slide d'explication avec le script 07 (style dual_detailed_blue)
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

class TestSlide39DualDetailedBlue:
    """
    Classe de test pour vérifier l'ajout de slide 39 avec le script 07.
    """

    def __init__(self):
        self.test_name = "Test Unitaire - Script 07 - Slide 39 (dual_detailed_blue)"
        self.script_01_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "01_slide_title_creator.py"
        self.script_07_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "07_detailed_explanation_builder.py"
        self.test_output_dir = Path(__file__).parent / "output"
        self.test_output_dir.mkdir(exist_ok=True)

    def setup_test(self):
        """Prépare l'environnement de test"""
        print(f"DEBUT du test: {self.test_name}")
        print(f"DOSSIER Répertoire de sortie: {self.test_output_dir}")
        print(f"SCRIPT Script 01 (base): {self.script_01_path}")
        print(f"SCRIPT Script 07 (testé): {self.script_07_path}")

        # Vérifier que les scripts existent
        if not self.script_01_path.exists():
            raise FileNotFoundError(f"Script 01 non trouvé: {self.script_01_path}")
        if not self.script_07_path.exists():
            raise FileNotFoundError(f"Script 07 non trouvé: {self.script_07_path}")

    def create_base_presentation(self):
        """
        Crée une présentation de base avec le script 01.

        Returns:
            Path: Chemin vers la présentation créée, ou None si échec
        """
        try:
            print(f"CREATION Étape 1: Création de la présentation de base...")

            # Paramètres pour la présentation de base
            base_title = "TEST UNITAIRE - Script 07"
            base_subtitle = "Présentation de base pour test d'explication détaillée"
            base_metadata = f"{datetime.now().strftime('%Y.%m.%d')} - Test Dual Detailed Blue"
            base_project = "test_script_07_slide_39_dual_detailed_blue"

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

            print(f"EXEC Création de la base:")
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
                print(f"ERREUR Erreur lors de la création de base:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return None

            # Vérifier que le fichier de base a été créé
            if not base_output_path.exists():
                print(f"ERREUR Fichier de base non créé: {base_output_path}")
                return None

            print(f"SUCCES Présentation de base créée:")
            print(f"   FICHIER Fichier: {base_output_path}")
            print(f"   TAILLE Taille: {base_output_path.stat().st_size:,} bytes")

            return base_output_path

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de la création de base")
            return None
        except Exception as e:
            print(f"ERREUR Erreur lors de la création de base: {e}")
            return None

    def add_dual_detailed_blue_slide(self, base_presentation_path):
        """
        Ajoute une slide explication dual detailed blue avec le script 07.

        Args:
            base_presentation_path (Path): Chemin vers la présentation de base

        Returns:
            bool: True si l'ajout réussit, False sinon
        """
        try:
            print(f"EXPLANATION Étape 2: Ajout de la slide dual detailed blue...")

            # Paramètres pour l'explication dual detailed blue
            explanation_title = "Transformation Digitale vs Legacy"
            explanation_subtitle = "Comparaison des approches technologiques"
            explanation_content = "Architecture cloud-native moderne avec microservices"
            additional_content = "Système monolithique traditionnel avec limitations scalabilité"

            # Commande pour ajouter l'explication détaillée
            cmd_07 = [
                sys.executable,
                str(self.script_07_path),
                explanation_content,
                "--insert-into", str(base_presentation_path),
                "--style", "dual_detailed_blue",
                "--title", explanation_title,
                "--subtitle", explanation_subtitle,
                "--additional", additional_content
            ]

            print(f"EXEC Ajout d'explication dual detailed blue:")
            print(f"   {' '.join(cmd_07)}")

            # Exécuter le script 07 depuis la racine du projet
            project_root = self.script_07_path.parent.parent
            result = subprocess.run(
                cmd_07,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=60
            )

            # Vérifier le résultat
            if result.returncode != 0:
                print(f"ERREUR Erreur lors de l'ajout de l'explication:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return False

            # Vérifier que le fichier a été modifié
            if not base_presentation_path.exists():
                print(f"ERREUR Fichier de présentation perdu: {base_presentation_path}")
                return False

            print(f"SUCCES Explication dual detailed blue ajoutée avec succès!")
            print(f"   FICHIER Fichier modifié: {base_presentation_path}")
            print(f"   TAILLE Nouvelle taille: {base_presentation_path.stat().st_size:,} bytes")
            print(f"   INFO Titre: {explanation_title}")
            print(f"   INFO Sous-titre: {explanation_subtitle}")
            print(f"   INFO Contenu principal: {explanation_content}")
            print(f"   INFO Contenu additionnel: {additional_content}")
            print(f"   INFO Style: dual_detailed_blue (slide 39)")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de l'ajout de l'explication")
            return False
        except Exception as e:
            print(f"ERREUR Erreur lors de l'ajout de l'explication: {e}")
            return False

    def run_validation_test(self):
        """
        Exécute le test de validation du script 07.

        Returns:
            bool: True si la validation réussit, False sinon
        """
        try:
            print(f"TEST Test de validation du script 07...")

            # Commande de validation
            cmd = [
                sys.executable,
                str(self.script_07_path),
                "--validate"
            ]

            print(f"EXEC Exécution de la validation:")
            print(f"   {' '.join(cmd)}")

            # Exécuter la validation depuis la racine du projet
            project_root = self.script_07_path.parent.parent
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

            print(f"SUCCES Validation réussie!")
            print(f"   RESULTAT Script 07 validé avec succès")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de la validation")
            return False
        except Exception as e:
            print(f"ERREUR Erreur lors de la validation: {e}")
            return False

    def cleanup_test(self):
        """Nettoie les fichiers de test si nécessaire"""
        print(f"NETTOIE Nettoyage terminé")
        print(f"DOSSIER Les fichiers de test sont conservés dans: {self.test_output_dir}")

    def run_all_tests(self):
        """
        Exécute tous les tests pour le script 07 slide 39.

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

            # Test 3: Ajout d'explication dual detailed blue (seulement si la base est créée)
            explanation_success = False
            if base_creation_success:
                explanation_success = self.add_dual_detailed_blue_slide(base_presentation_path)

            self.cleanup_test()

            # Résultat final
            all_success = validation_success and base_creation_success and explanation_success

            print(f"\n{'='*60}")
            print(f"STATS RÉSULTATS DU TEST - {self.test_name}")
            print(f"{'='*60}")
            print(f"TEST Validation script: {'RÉUSSI' if validation_success else 'ÉCHEC'}")
            print(f"CREATION Création base (script 01): {'RÉUSSI' if base_creation_success else 'ÉCHEC'}")
            print(f"EXPLANATION Ajout explication (script 07): {'RÉUSSI' if explanation_success else 'ÉCHEC'}")
            print(f"FINAL Résultat global: {'TOUS LES TESTS RÉUSSIS' if all_success else 'ÉCHECS DÉTECTÉS'}")
            print(f"{'='*60}")

            return all_success

        except Exception as e:
            print(f"ERREUR Erreur critique dans les tests: {e}")
            return False


def main():
    """Point d'entrée principal pour exécuter les tests"""
    test_runner = TestSlide39DualDetailedBlue()
    success = test_runner.run_all_tests()

    # Code de retour approprié
    exit_code = 0 if success else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()