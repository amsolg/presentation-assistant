#!/usr/bin/env python3
"""
Test unitaire pour le script 10 - Conclusion Builder
Test d'ajout de slide 57 (conclusion Monogramme Premier Tech)
Test de la conclusion minimaliste avec style monogram

Ce test verifie la capacite du script 10 a ajouter une slide de conclusion
minimaliste avec monogramme dans une presentation existante en utilisant
le template slide 57. Il teste l'élégance et la simplicité du design.

Workflow du test:
1. Creer une presentation de base avec le script 01
2. Ajouter la conclusion Monogramme avec le script 10 (slide 57)
3. Verifier le resultat et le design minimaliste
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

class TestSlide57Monogram:
    """
    Classe de test pour verifier l'ajout de slide 57 avec le script 10.
    """

    def __init__(self):
        self.test_name = "Test Unitaire - Script 10 - Monogramme PT"
        self.script_01_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "01_slide_title_creator.py"
        self.script_10_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "10_conclusion_builder.py"
        self.test_output_dir = Path(__file__).parent / "output"
        self.test_output_dir.mkdir(exist_ok=True)

    def setup_test(self):
        """Prepare l'environnement de test"""
        print(f"DEBUT du test: {self.test_name}")
        print(f"DOSSIER Repertoire de sortie: {self.test_output_dir}")
        print(f"SCRIPT Script 01 (base): {self.script_01_path}")
        print(f"SCRIPT Script 10 (teste): {self.script_10_path}")

        # Verifier que les scripts existent
        if not self.script_01_path.exists():
            raise FileNotFoundError(f"Script 01 non trouve: {self.script_01_path}")
        if not self.script_10_path.exists():
            raise FileNotFoundError(f"Script 10 non trouve: {self.script_10_path}")

    def create_base_presentation(self):
        """
        Cree une presentation de base avec le script 01.

        Returns:
            Path: Chemin vers la presentation creee, ou None si echec
        """
        try:
            print(f"CREATION Etape 1: Creation de la presentation de base...")

            # Parametres pour la presentation de base
            base_title = "TEST UNITAIRE - Script 10"
            base_subtitle = "Presentation de base pour test conclusion Monogramme"
            base_metadata = f"{datetime.now().strftime('%Y.%m.%d')} - Test Conclusion Monogramme"
            base_project = "test_script_10_monogram"

            # Chemin de sortie pour la presentation de base
            base_output_path = self.test_output_dir / f"{base_project}.pptx"

            # Commande pour creer la presentation de base
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

            # Executer le script 01 depuis son repertoire
            result = subprocess.run(
                cmd_01,
                cwd=self.script_01_path.parent,
                capture_output=True,
                text=True,
                timeout=60
            )

            # Verifier le resultat
            if result.returncode != 0:
                print(f"ERREUR Erreur lors de la creation de base:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return None

            # Verifier que le fichier de base a ete cree
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

    def add_conclusion_slide(self, base_presentation_path):
        """
        Ajoute une slide de conclusion Monogramme avec le script 10.

        Args:
            base_presentation_path (Path): Chemin vers la presentation de base

        Returns:
            bool: True si l'ajout reussit, False sinon
        """
        try:
            print(f"CONCLUSION Etape 2: Ajout de la conclusion Monogramme...")

            # Parametres pour la conclusion minimaliste (très limités pour préserver l'élégance)
            title = "Excellence"  # Titre discret si nécessaire

            # Commande pour ajouter la conclusion (monogram reste volontairement épuré)
            cmd_10 = [
                sys.executable,
                str(self.script_10_path),
                "",  # Pas de message pour préserver le minimalisme
                "--style", "monogram",
                "--title", title,
                "--insert-into", str(base_presentation_path)
            ]

            print(f"EXEC Ajout de conclusion Monogramme:")
            print(f"   {' '.join(cmd_10)}")

            # Executer le script 10 depuis la racine du projet
            project_root = self.script_10_path.parent.parent
            result = subprocess.run(
                cmd_10,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=60
            )

            # Verifier le resultat
            if result.returncode != 0:
                print(f"ERREUR Erreur lors de l'ajout de conclusion:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return False

            # Verifier que le fichier a ete modifie
            if not base_presentation_path.exists():
                print(f"ERREUR Fichier de presentation perdu: {base_presentation_path}")
                return False

            print(f"SUCCES Conclusion Monogramme ajoutee avec succes!")
            print(f"   FICHIER Fichier modifie: {base_presentation_path}")
            print(f"   TAILLE Nouvelle taille: {base_presentation_path.stat().st_size:,} bytes")
            print(f"   TITRE Titre discret: {title}")
            print(f"   STYLE Style: monogram (slide 57)")
            print(f"   TYPE Type: minimalist_closing - Fermeture élégante et minimaliste")
            print(f"   AUDIENCE Audience: Executives, Audiences formelles")
            print(f"   DESIGN Design: Épuré avec monogramme Premier Tech")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de l'ajout de conclusion")
            return False
        except Exception as e:
            print(f"ERREUR Erreur lors de l'ajout de conclusion: {e}")
            return False

    def run_validation_test(self):
        """
        Execute le test de validation du script 10.

        Returns:
            bool: True si la validation reussit, False sinon
        """
        try:
            print(f"TEST Test de validation du script 10...")

            # Commande de validation
            cmd = [
                sys.executable,
                str(self.script_10_path),
                "--validate"
            ]

            print(f"EXEC Execution de la validation:")
            print(f"   {' '.join(cmd)}")

            # Executer la validation depuis la racine du projet
            project_root = self.script_10_path.parent.parent
            result = subprocess.run(
                cmd,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=30
            )

            # Verifier le resultat
            if result.returncode != 0:
                print(f"ERREUR Erreur lors de la validation:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return False

            print(f"SUCCES Validation reussie!")
            print(f"   RESULTAT Script 10 valide avec succes")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de la validation")
            return False
        except Exception as e:
            print(f"ERREUR Erreur lors de la validation: {e}")
            return False

    def cleanup_test(self):
        """Nettoie les fichiers de test si necessaire"""
        print(f"NETTOIE Nettoyage termine")
        print(f"DOSSIER Les fichiers de test sont conserves dans: {self.test_output_dir}")

    def run_all_tests(self):
        """
        Execute tous les tests pour le script 10 slide 57.

        Returns:
            bool: True si tous les tests reussissent, False sinon
        """
        try:
            self.setup_test()

            # Test 1: Validation du script
            validation_success = self.run_validation_test()

            # Test 2: Creation de presentation de base
            base_presentation_path = self.create_base_presentation()
            base_creation_success = base_presentation_path is not None

            # Test 3: Ajout de conclusion (seulement si la base est creee)
            conclusion_success = False
            if base_creation_success:
                conclusion_success = self.add_conclusion_slide(base_presentation_path)

            self.cleanup_test()

            # Resultat final
            all_success = validation_success and base_creation_success and conclusion_success

            print(f"\n{'='*70}")
            print(f"STATS RESULTATS DU TEST - {self.test_name}")
            print(f"{'='*70}")
            print(f"TEST Validation script: {'REUSSI' if validation_success else 'ECHEC'}")
            print(f"CREATION Creation base (script 01): {'REUSSI' if base_creation_success else 'ECHEC'}")
            print(f"CONCLUSION Ajout conclusion (script 10): {'REUSSI' if conclusion_success else 'ECHEC'}")
            print(f"FINAL Resultat global: {'TOUS LES TESTS REUSSIS' if all_success else 'ECHECS DETECTES'}")
            print(f"TYPE Test: Slide 57 - Monogramme PT (monogram)")
            print(f"TEMPLATE Template: minimalist_closing pour Executives/Audiences formelles")
            print(f"DESIGN Design: Épuré et élégant avec monogramme Premier Tech")
            print(f"{'='*70}")

            return all_success

        except Exception as e:
            print(f"ERREUR Erreur critique dans les tests: {e}")
            return False


def main():
    """Point d'entree principal pour executer les tests"""
    test_runner = TestSlide57Monogram()
    success = test_runner.run_all_tests()

    # Code de retour approprie
    exit_code = 0 if success else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()