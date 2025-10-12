#!/usr/bin/env python3
"""
Test unitaire pour le script 02 - Navigation Builder
Test d'ajout de slide 13 (navigation/table des matières Premier Tech)

Ce test vérifie la capacité du script 02 à ajouter une slide de navigation
dans une présentation existante en utilisant le template slide 13.

Workflow du test:
1. Créer une présentation de base avec le script 01
2. Ajouter une slide de navigation avec le script 02
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

class TestSlide13Navigation:
    """
    Classe de test pour vérifier l'ajout de slide 13 avec le script 02.
    """

    def __init__(self):
        self.test_name = "Test Unitaire - Script 02 - Slide 13"
        self.script_01_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "01_slide_title_creator.py"
        self.script_02_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "02_navigation_builder.py"
        self.test_output_dir = Path(__file__).parent / "output"
        self.test_output_dir.mkdir(exist_ok=True)

    def setup_test(self):
        """Prépare l'environnement de test"""
        print(f"DEBUT Début du test: {self.test_name}")
        print(f"DOSSIER Répertoire de sortie: {self.test_output_dir}")
        print(f"SCRIPT Script 01 (base): {self.script_01_path}")
        print(f"SCRIPT Script 02 (testé): {self.script_02_path}")

        # Vérifier que les scripts existent
        if not self.script_01_path.exists():
            raise FileNotFoundError(f"Script 01 non trouvé: {self.script_01_path}")
        if not self.script_02_path.exists():
            raise FileNotFoundError(f"Script 02 non trouvé: {self.script_02_path}")

    def create_base_presentation(self):
        """
        Crée une présentation de base avec le script 01.

        Returns:
            Path: Chemin vers la présentation créée, ou None si échec
        """
        try:
            print(f"CREATION Étape 1: Création de la présentation de base...")

            # Paramètres pour la présentation de base
            base_title = "TEST UNITAIRE - Script 02"
            base_subtitle = "Présentation de base pour test de navigation"
            base_metadata = f"{datetime.now().strftime('%Y.%m.%d')} - Test Navigation"
            base_project = "test_script_02_base"

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

    def add_navigation_slide(self, base_presentation_path):
        """
        Ajoute une slide de navigation avec le script 02.

        Args:
            base_presentation_path (Path): Chemin vers la présentation de base

        Returns:
            bool: True si l'ajout réussit, False sinon
        """
        try:
            print(f"NAV Étape 2: Ajout de la navigation...")

            # Sections de test pour la navigation
            test_sections = [
                "Introduction",
                "Analyse de la Situation",
                "Solutions Proposées",
                "Plan d'Implémentation",
                "Conclusion"
            ]

            # Commande pour ajouter la navigation
            cmd_02 = [
                sys.executable,
                str(self.script_02_path),
                "--insert-into", str(base_presentation_path),
                "--sections"
            ] + test_sections

            print(f"EXEC Ajout de navigation:")
            print(f"   {' '.join(cmd_02)}")

            # Exécuter le script 02 depuis la racine du projet
            project_root = self.script_02_path.parent.parent
            result = subprocess.run(
                cmd_02,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=60
            )

            # Vérifier le résultat
            if result.returncode != 0:
                print(f"ERREUR Erreur lors de l'ajout de navigation:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return False

            # Vérifier que le fichier a été modifié
            if not base_presentation_path.exists():
                print(f"ERREUR Fichier de présentation perdu: {base_presentation_path}")
                return False

            print(f"SUCCES Navigation ajoutée avec succès!")
            print(f"   FICHIER Fichier modifié: {base_presentation_path}")
            print(f"   TAILLE Nouvelle taille: {base_presentation_path.stat().st_size:,} bytes")
            print(f"   RESULTAT Sections ajoutées: {len(test_sections)}")
            print(f"   INFO Sections: {', '.join(test_sections)}")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de l'ajout de navigation")
            return False
        except Exception as e:
            print(f"ERREUR Erreur lors de l'ajout de navigation: {e}")
            return False

    def run_validation_test(self):
        """
        Exécute le test de validation du script 02.

        Returns:
            bool: True si la validation réussit, False sinon
        """
        try:
            print(f"TEST Test de validation du script 02...")

            # Commande de validation
            cmd = [
                sys.executable,
                str(self.script_02_path),
                "--validate"
            ]

            print(f"EXEC Exécution de la validation:")
            print(f"   {' '.join(cmd)}")

            # Exécuter la validation depuis la racine du projet
            project_root = self.script_02_path.parent.parent
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
            print(f"   RESULTAT Script 02 validé avec succès")

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
        Exécute tous les tests pour le script 02.

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

            # Test 3: Ajout de navigation (seulement si la base est créée)
            navigation_success = False
            if base_creation_success:
                navigation_success = self.add_navigation_slide(base_presentation_path)

            self.cleanup_test()

            # Résultat final
            all_success = validation_success and base_creation_success and navigation_success

            print(f"\n{'='*60}")
            print(f"STATS RÉSULTATS DU TEST - {self.test_name}")
            print(f"{'='*60}")
            print(f"TEST Validation script: {'SUCCES RÉUSSI' if validation_success else 'ERREUR ÉCHEC'}")
            print(f"CREATION Création base (script 01): {'SUCCES RÉUSSI' if base_creation_success else 'ERREUR ÉCHEC'}")
            print(f"NAV Ajout navigation (script 02): {'SUCCES RÉUSSI' if navigation_success else 'ERREUR ÉCHEC'}")
            print(f"FINAL Résultat global: {'SUCCES TOUS LES TESTS RÉUSSIS' if all_success else 'ERREUR ÉCHECS DÉTECTÉS'}")
            print(f"{'='*60}")

            return all_success

        except Exception as e:
            print(f"ERREUR Erreur critique dans les tests: {e}")
            return False


def main():
    """Point d'entrée principal pour exécuter les tests"""
    test_runner = TestSlide13Navigation()
    success = test_runner.run_all_tests()

    # Code de retour approprié
    exit_code = 0 if success else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()