#!/usr/bin/env python3
"""
Test unitaire pour le script 05 - Statistics Builder
Test d'ajout de slide 24 (3 statistiques & Mots-clés Premier Tech)

Ce test verifie la capacite du script 05 a ajouter une slide de 3 statistiques
avec mots-cles dans une presentation existante en utilisant le template slide 24.

Workflow du test:
1. Creer une presentation de base avec le script 01
2. Ajouter les 3 statistiques avec le script 05
3. Verifier le resultat
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

class TestSlide24ThreeStats:
    """
    Classe de test pour verifier l'ajout de slide 24 (three_stats) avec le script 05.
    """

    def __init__(self):
        self.test_name = "Test Unitaire - Script 05 - Slide 24 Three Stats"
        self.script_01_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "01_slide_title_creator.py"
        self.script_05_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "05_statistics_builder.py"
        self.test_output_dir = Path(__file__).parent / "output"
        self.test_output_dir.mkdir(exist_ok=True)

    def setup_test(self):
        """Prepare l'environnement de test"""
        print(f"DEBUT du test: {self.test_name}")
        print(f"DOSSIER Repertoire de sortie: {self.test_output_dir}")
        print(f"SCRIPT Script 01 (base): {self.script_01_path}")
        print(f"SCRIPT Script 05 (teste): {self.script_05_path}")

        # Verifier que les scripts existent
        if not self.script_01_path.exists():
            raise FileNotFoundError(f"Script 01 non trouve: {self.script_01_path}")
        if not self.script_05_path.exists():
            raise FileNotFoundError(f"Script 05 non trouve: {self.script_05_path}")

    def create_base_presentation(self):
        """
        Cree une presentation de base avec le script 01.

        Returns:
            Path: Chemin vers la presentation creee, ou None si echec
        """
        try:
            print(f"CREATION Etape 1: Creation de la presentation de base...")

            # Parametres pour la presentation de base
            base_title = "TEST UNITAIRE - Script 05 Three Stats"
            base_subtitle = "Presentation de base pour test 3 statistiques"
            base_metadata = f"{datetime.now().strftime('%Y.%m.%d')} - Test 3 Statistiques"
            base_project = "test_script_05_slide_24_three"

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

    def add_statistics_slide(self, base_presentation_path):
        """
        Ajoute une slide de 3 statistiques avec le script 05.

        Args:
            base_presentation_path (Path): Chemin vers la presentation de base

        Returns:
            bool: True si l'ajout reussit, False sinon
        """
        try:
            print(f"STATISTIQUES Etape 2: Ajout des 3 statistiques...")

            # Parametres pour les statistiques (3 statistiques requises)
            stat1_value = "95%"
            stat1_label = "Satisfaction Client"
            stat2_value = "47M€"
            stat2_label = "Revenue Annuel"
            stat3_value = "28+"
            stat3_label = "Pays Desservis"
            slide_title = "Notre Impact Global"

            # Commande pour ajouter les statistiques
            # Note: Besoin d'ajouter stat3_value et stat3_label aux arguments CLI
            cmd_05 = [
                sys.executable,
                str(self.script_05_path),
                stat1_value,
                stat1_label,
                stat2_value,
                stat2_label,
                stat3_value,
                stat3_label,
                "--style", "three_stats",
                "--title", slide_title,
                "--insert-into", str(base_presentation_path)
            ]

            print(f"EXEC Ajout de 3 statistiques:")
            print(f"   {' '.join(cmd_05)}")

            # Executer le script 05 depuis la racine du projet
            project_root = self.script_05_path.parent.parent
            result = subprocess.run(
                cmd_05,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=60
            )

            # Verifier le resultat
            if result.returncode != 0:
                print(f"ERREUR Erreur lors de l'ajout de statistiques:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return False

            # Verifier que le fichier a ete modifie
            if not base_presentation_path.exists():
                print(f"ERREUR Fichier de presentation perdu: {base_presentation_path}")
                return False

            print(f"SUCCES 3 statistiques ajoutees avec succes!")
            print(f"   FICHIER Fichier modifie: {base_presentation_path}")
            print(f"   TAILLE Nouvelle taille: {base_presentation_path.stat().st_size:,} bytes")
            print(f"   INFO Statistique 1: {stat1_value} - {stat1_label}")
            print(f"   INFO Statistique 2: {stat2_value} - {stat2_label}")
            print(f"   INFO Statistique 3: {stat3_value} - {stat3_label}")
            print(f"   INFO Titre: {slide_title}")
            print(f"   INFO Style: three_stats (slide 24)")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de l'ajout de statistiques")
            return False
        except Exception as e:
            print(f"ERREUR Erreur lors de l'ajout de statistiques: {e}")
            return False

    def run_validation_test(self):
        """
        Execute le test de validation du script 05.

        Returns:
            bool: True si la validation reussit, False sinon
        """
        try:
            print(f"TEST Test de validation du script 05...")

            # Commande de validation
            cmd = [
                sys.executable,
                str(self.script_05_path),
                "--validate"
            ]

            print(f"EXEC Execution de la validation:")
            print(f"   {' '.join(cmd)}")

            # Executer la validation depuis la racine du projet
            project_root = self.script_05_path.parent.parent
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
            print(f"   RESULTAT Script 05 valide avec succes")

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
        Execute tous les tests pour le script 05 slide 24 three stats.

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

            # Test 3: Ajout de statistiques (seulement si la base est creee)
            statistics_success = False
            if base_creation_success:
                statistics_success = self.add_statistics_slide(base_presentation_path)

            self.cleanup_test()

            # Resultat final
            all_success = validation_success and base_creation_success and statistics_success

            print(f"\n{'='*60}")
            print(f"STATS RESULTATS DU TEST - {self.test_name}")
            print(f"{'='*60}")
            print(f"TEST Validation script: {'REUSSI' if validation_success else 'ECHEC'}")
            print(f"CREATION Creation base (script 01): {'REUSSI' if base_creation_success else 'ECHEC'}")
            print(f"STATISTIQUES Ajout statistiques (script 05): {'REUSSI' if statistics_success else 'ECHEC'}")
            print(f"FINAL Resultat global: {'TOUS LES TESTS REUSSIS' if all_success else 'ECHECS DETECTES'}")
            print(f"{'='*60}")

            return all_success

        except Exception as e:
            print(f"ERREUR Erreur critique dans les tests: {e}")
            return False


def main():
    """Point d'entree principal pour executer les tests"""
    test_runner = TestSlide24ThreeStats()
    success = test_runner.run_all_tests()

    # Code de retour approprie
    exit_code = 0 if success else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()