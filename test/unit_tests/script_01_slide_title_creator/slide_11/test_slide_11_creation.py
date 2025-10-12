#!/usr/bin/env python3
"""
Test unitaire pour le script 01 - Slide Title Creator
Test de création de slide 11 (page titre Premier Tech)

Ce test vérifie la capacité du script 01 à créer une présentation
avec une page titre utilisant le template slide 11.
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

class TestSlide11Creation:
    """
    Classe de test pour vérifier la création de slide 11 avec le script 01.
    """

    def __init__(self):
        self.test_name = "Test Unitaire - Script 01 - Slide 11"
        self.script_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "01_slide_title_creator.py"
        self.test_output_dir = Path(__file__).parent / "output"
        self.test_output_dir.mkdir(exist_ok=True)

    def setup_test(self):
        """Prépare l'environnement de test"""
        print(f"Debut du test: {self.test_name}")
        print(f"Repertoire de sortie: {self.test_output_dir}")
        print(f"Script teste: {self.script_path}")

        # Vérifier que le script existe
        if not self.script_path.exists():
            raise FileNotFoundError(f"Script non trouvé: {self.script_path}")

    def run_slide_creation_test(self):
        """
        Exécute le test de création de slide 11.

        Returns:
            bool: True si le test réussit, False sinon
        """
        try:
            # Paramètres de test pour la slide 11
            test_title = "TEST UNITAIRE - Script 01"
            test_subtitle = "Validation de la création de slide titre (Template 11)"
            test_metadata = f"{datetime.now().strftime('%Y.%m.%d')} - Test Automatisé"
            test_project = "test_script_01_slide_11"

            # Chemin de sortie pour le test
            output_path = self.test_output_dir / f"{test_project}.pptx"

            # Commande à exécuter
            cmd = [
                sys.executable,
                str(self.script_path),
                test_title,
                "--subtitle", test_subtitle,
                "--metadata", test_metadata,
                "--project", test_project,
                "--output", str(output_path)
            ]

            print(f"Execution de la commande:")
            print(f"   {' '.join(cmd)}")

            # Exécuter le script
            result = subprocess.run(
                cmd,
                cwd=self.script_path.parent,
                capture_output=True,
                text=True,
                timeout=60
            )

            # Vérifier le résultat
            if result.returncode != 0:
                print(f"ERREUR lors de l'execution:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return False

            # Vérifier que le fichier de sortie a été créé
            if not output_path.exists():
                print(f"ERREUR Fichier de sortie non cree: {output_path}")
                return False

            # Vérifier la taille du fichier (doit être > 0)
            file_size = output_path.stat().st_size
            if file_size == 0:
                print(f"ERREUR Fichier de sortie vide: {output_path}")
                return False

            print(f"SUCCES Test reussi!")
            print(f"   Fichier cree: {output_path}")
            print(f"   Taille du fichier: {file_size:,} bytes")
            print(f"   Titre teste: {test_title}")
            print(f"   Sous-titre: {test_subtitle}")
            print(f"   Metadonnees: {test_metadata}")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de l'execution du script")
            return False
        except Exception as e:
            print(f"ERREUR inattendue: {e}")
            return False

    def run_validation_test(self):
        """
        Exécute le test de validation du template.

        Returns:
            bool: True si la validation réussit, False sinon
        """
        try:
            print(f"Test de validation du template...")

            # Commande de validation
            cmd = [
                sys.executable,
                str(self.script_path),
                "dummy",
                "--validate"
            ]

            print(f"Execution de la validation:")
            print(f"   {' '.join(cmd)}")

            # Exécuter la validation
            result = subprocess.run(
                cmd,
                cwd=self.script_path.parent,
                capture_output=True,
                text=True,
                timeout=30
            )

            # Vérifier le résultat
            if result.returncode != 0:
                print(f"ERREUR lors de la validation:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return False

            print(f"SUCCES Validation reussie!")
            print(f"   Template valide avec succes")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de la validation")
            return False
        except Exception as e:
            print(f"ERREUR lors de la validation: {e}")
            return False

    def cleanup_test(self):
        """Nettoie les fichiers de test si nécessaire"""
        print(f"Nettoyage termine")
        print(f"Les fichiers de test sont conserves dans: {self.test_output_dir}")

    def run_all_tests(self):
        """
        Exécute tous les tests pour le script 01.

        Returns:
            bool: True si tous les tests réussissent, False sinon
        """
        try:
            self.setup_test()

            # Test 1: Validation du template
            validation_success = self.run_validation_test()

            # Test 2: Création de slide 11
            creation_success = self.run_slide_creation_test()

            self.cleanup_test()

            # Résultat final
            all_success = validation_success and creation_success

            print(f"\n{'='*60}")
            print(f"RESULTATS DU TEST - {self.test_name}")
            print(f"{'='*60}")
            print(f"Validation template: {'REUSSI' if validation_success else 'ECHEC'}")
            print(f"Creation slide 11: {'REUSSI' if creation_success else 'ECHEC'}")
            print(f"Resultat global: {'TOUS LES TESTS REUSSIS' if all_success else 'ECHECS DETECTES'}")
            print(f"{'='*60}")

            return all_success

        except Exception as e:
            print(f"ERREUR critique dans les tests: {e}")
            return False


def main():
    """Point d'entrée principal pour exécuter les tests"""
    test_runner = TestSlide11Creation()
    success = test_runner.run_all_tests()

    # Code de retour approprié
    exit_code = 0 if success else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()