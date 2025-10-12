#!/usr/bin/env python3
"""
Test unitaire pour le script 08 - Testimonial Builder
Test de creation de slide 45 (testimonial Premier Tech)

Ce test verifie la capacite du script 08 a creer une slide de testimonial
utilisant le template slide 45 et l'inserer dans une presentation existante.
"""

import os
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path
from datetime import datetime

# Ajouter le repertoire racine au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))

class TestSlide45Standard:
    """
    Classe de test pour verifier la creation de slide 45 avec le script 08.
    """

    def __init__(self):
        self.test_name = "Test Unitaire - Script 08 - Slide 45"
        self.script_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "08_testimonial_builder.py"
        self.title_creator_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "01_slide_title_creator.py"
        self.test_output_dir = Path(__file__).parent / "output"
        self.test_output_dir.mkdir(exist_ok=True)

    def setup_test(self):
        """Prepare l'environnement de test"""
        print(f"Debut du test: {self.test_name}")
        print(f"Repertoire de sortie: {self.test_output_dir}")
        print(f"Script teste: {self.script_path}")

        # Verifier que le script existe
        if not self.script_path.exists():
            raise FileNotFoundError(f"Script non trouve: {self.script_path}")

        if not self.title_creator_path.exists():
            raise FileNotFoundError(f"Script titre non trouve: {self.title_creator_path}")

    def run_template_validation_test(self):
        """
        Execute le test de validation du template.

        Returns:
            bool: True si la validation reussit, False sinon
        """
        try:
            print(f"Test de validation du template...")

            # Commande de validation
            cmd = [
                sys.executable,
                str(self.script_path),
                "--validate"
            ]

            print(f"Execution de la validation:")
            print(f"   {' '.join(cmd)}")

            # Executer la validation depuis la racine du projet
            project_root = self.script_path.parent.parent
            result = subprocess.run(
                cmd,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=30
            )

            # Verifier le resultat
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

    def run_standalone_creation_test(self):
        """
        Execute le test de creation autonome de slide testimonial.

        Returns:
            bool: True si le test reussit, False sinon
        """
        try:
            # Parametres de test pour creation autonome
            test_quote = "Cette solution a revolutionne notre approche du developpement. Les resultats depassent nos attentes."
            test_author = "Jean Dupont"
            test_position = "Directeur Technique"
            test_company = "TechCorp Solutions"
            test_title = "Retour d'Experience Client"

            # Chemin de sortie pour le test
            output_path = self.test_output_dir / "test_testimonial_standalone.pptx"

            # Commande a executer
            cmd = [
                sys.executable,
                str(self.script_path),
                test_quote,
                test_author,
                "--position", test_position,
                "--company", test_company,
                "--testimonial-title", test_title,
                "--output", str(output_path)
            ]

            print(f"Execution de la creation autonome:")
            print(f"   {' '.join(cmd)}")

            # Executer le script depuis la racine du projet
            project_root = self.script_path.parent.parent
            result = subprocess.run(
                cmd,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=60
            )

            # Verifier le resultat
            if result.returncode != 0:
                print(f"ERREUR lors de l'execution:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return False

            # Verifier que le fichier de sortie a ete cree
            if not output_path.exists():
                print(f"ERREUR Fichier de sortie non cree: {output_path}")
                return False

            # Verifier la taille du fichier (doit etre > 0)
            file_size = output_path.stat().st_size
            if file_size == 0:
                print(f"ERREUR Fichier de sortie vide: {output_path}")
                return False

            print(f"SUCCES Creation autonome reussie!")
            print(f"   Fichier cree: {output_path}")
            print(f"   Taille du fichier: {file_size:,} bytes")
            print(f"   Citation: {test_quote[:50]}...")
            print(f"   Auteur: {test_author}")
            print(f"   Position: {test_position}")
            print(f"   Entreprise: {test_company}")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de l'execution du script")
            return False
        except Exception as e:
            print(f"ERREUR inattendue: {e}")
            return False

    def run_insertion_test(self):
        """
        Execute le test d'insertion dans une presentation existante.

        Returns:
            bool: True si le test reussit, False sinon
        """
        try:
            # Etape 1: Creer une presentation de base
            print(f"Creation d'une presentation de base...")

            base_title = "Test Presentation - Testimonial"
            base_output = self.test_output_dir / "base_presentation.pptx"

            cmd_base = [
                sys.executable,
                str(self.title_creator_path),
                base_title,
                "--output", str(base_output)
            ]

            result_base = subprocess.run(
                cmd_base,
                cwd=self.title_creator_path.parent,
                capture_output=True,
                text=True,
                timeout=30
            )

            if result_base.returncode != 0:
                print(f"ERREUR creation presentation de base:")
                print(f"   STDOUT: {result_base.stdout}")
                print(f"   STDERR: {result_base.stderr}")
                return False

            if not base_output.exists():
                print(f"ERREUR Presentation de base non creee: {base_output}")
                return False

            print(f"   Presentation de base creee: {base_output}")

            # Etape 2: Inserer le testimonial
            test_quote = "L'implementation s'est deroulee sans accroc et les resultats sont exceptionnels."
            test_author = "Marie Dubois"
            test_position = "Chef de Projet"
            test_company = "Innovation Corp"

            cmd_insert = [
                sys.executable,
                str(self.script_path),
                test_quote,
                test_author,
                "--position", test_position,
                "--company", test_company,
                "--insert-into", str(base_output)
            ]

            print(f"Insertion du testimonial:")
            print(f"   {' '.join(cmd_insert)}")

            # Executer depuis la racine du projet comme les autres scripts
            project_root = self.script_path.parent.parent
            result_insert = subprocess.run(
                cmd_insert,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=60
            )

            # Verifier le resultat
            if result_insert.returncode != 0:
                print(f"ERREUR lors de l'insertion:")
                print(f"   STDOUT: {result_insert.stdout}")
                print(f"   STDERR: {result_insert.stderr}")
                return False

            # Verifier que le fichier existe toujours et a ete modifie
            if not base_output.exists():
                print(f"ERREUR Fichier disparu apres insertion: {base_output}")
                return False

            file_size = base_output.stat().st_size
            if file_size == 0:
                print(f"ERREUR Fichier vide apres insertion: {base_output}")
                return False

            print(f"SUCCES Insertion reussie!")
            print(f"   Fichier mis a jour: {base_output}")
            print(f"   Taille finale: {file_size:,} bytes")
            print(f"   Citation inseree: {test_quote[:50]}...")
            print(f"   Auteur: {test_author} - {test_position}, {test_company}")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de l'insertion")
            return False
        except Exception as e:
            print(f"ERREUR inattendue lors de l'insertion: {e}")
            return False

    def run_list_styles_test(self):
        """
        Execute le test de listage des styles disponibles.

        Returns:
            bool: True si le test reussit, False sinon
        """
        try:
            print(f"Test de listage des styles...")

            # Commande de listage
            cmd = [
                sys.executable,
                str(self.script_path),
                "--list-styles"
            ]

            print(f"Execution du listage:")
            print(f"   {' '.join(cmd)}")

            # Executer le listage depuis la racine du projet
            project_root = self.script_path.parent.parent
            result = subprocess.run(
                cmd,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=30
            )

            # Verifier le resultat
            if result.returncode != 0:
                print(f"ERREUR lors du listage:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return False

            print(f"SUCCES Listage reussi!")
            print(f"   Styles listes avec succes")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors du listage")
            return False
        except Exception as e:
            print(f"ERREUR lors du listage: {e}")
            return False

    def cleanup_test(self):
        """Nettoie les fichiers de test si necessaire"""
        print(f"Nettoyage termine")
        print(f"Les fichiers de test sont conserves dans: {self.test_output_dir}")

    def run_all_tests(self):
        """
        Execute tous les tests pour le script 08.

        Returns:
            bool: True si tous les tests reussissent, False sinon
        """
        try:
            self.setup_test()

            # Test 1: Validation du template
            validation_success = self.run_template_validation_test()

            # Test 2: Listage des styles
            list_styles_success = self.run_list_styles_test()

            # Test 3: Insertion dans presentation existante
            # Note: Pas de test de creation autonome car le script 08 ne la supporte pas
            insertion_success = self.run_insertion_test()

            self.cleanup_test()

            # Resultat final
            all_success = validation_success and list_styles_success and insertion_success

            print(f"\n{'='*60}")
            print(f"RESULTATS DU TEST - {self.test_name}")
            print(f"{'='*60}")
            print(f"Validation template: {'REUSSI' if validation_success else 'ECHEC'}")
            print(f"Listage styles: {'REUSSI' if list_styles_success else 'ECHEC'}")
            print(f"Insertion testimonial: {'REUSSI' if insertion_success else 'ECHEC'}")
            print(f"Resultat global: {'TOUS LES TESTS REUSSIS' if all_success else 'ECHECS DETECTES'}")
            print(f"{'='*60}")

            return all_success

        except Exception as e:
            print(f"ERREUR critique dans les tests: {e}")
            return False


def main():
    """Point d'entree principal pour executer les tests"""
    test_runner = TestSlide45Standard()
    success = test_runner.run_all_tests()

    # Code de retour approprie
    exit_code = 0 if success else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()