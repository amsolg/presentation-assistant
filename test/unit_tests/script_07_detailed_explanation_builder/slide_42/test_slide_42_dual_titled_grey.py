#!/usr/bin/env python3
"""
Test unitaire pour le script 07 - Detailed Explanation Builder
Test d'ajout de slide 42 (2 listes avec sous-titres et ligne bleue Premier Tech)

Ce test vérifie la capacité du script 07 à ajouter une slide avec 2 listes structurées
avec ligne bleue dans une présentation existante en utilisant le template slide 42.

Workflow du test:
1. Créer une présentation de base avec le script 01
2. Ajouter une slide explication détaillée avec le script 07 (slide 42)
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

class TestSlide42DualListsBlue:
    """
    Classe de test pour vérifier l'ajout de slide 42 avec le script 07.
    """

    def __init__(self):
        self.test_name = "Test Unitaire - Script 07 - Slide 42"
        self.script_01_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "01_slide_title_creator.py"
        self.script_07_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "07_detailed_explanation_builder.py"
        self.test_output_dir = Path(__file__).parent / "output"
        self.test_output_dir.mkdir(exist_ok=True)

    def setup_test(self):
        """Prépare l'environnement de test"""
        print(f"DEBUT du test: {self.test_name}")
        print(f"DOSSIER Repertoire de sortie: {self.test_output_dir}")
        print(f"SCRIPT Script 01 (base): {self.script_01_path}")
        print(f"SCRIPT Script 07 (teste): {self.script_07_path}")

        # Vérifier que les scripts existent
        if not self.script_01_path.exists():
            raise FileNotFoundError(f"Script 01 non trouve: {self.script_01_path}")
        if not self.script_07_path.exists():
            raise FileNotFoundError(f"Script 07 non trouve: {self.script_07_path}")

    def create_base_presentation(self):
        """
        Crée une présentation de base avec le script 01.

        Returns:
            Path: Chemin vers la présentation créée, ou None si échec
        """
        try:
            print(f"CREATION Etape 1: Creation de la presentation de base...")

            # Paramètres pour la présentation de base
            base_title = "TEST UNITAIRE - Script 07"
            base_subtitle = "Presentation de base pour test listes structurees"
            base_metadata = f"{datetime.now().strftime('%Y.%m.%d')} - Test Dual Lists Blue"
            base_project = "test_script_07_slide_42"

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

    def add_explanation_slide(self, base_presentation_path):
        """
        Ajoute une slide explication détaillée avec le script 07.

        Args:
            base_presentation_path (Path): Chemin vers la présentation de base

        Returns:
            bool: True si l'ajout réussit, False sinon
        """
        try:
            print(f"EXPLANATION Etape 2: Ajout de la slide explication detaillee...")

            # Paramètres du test pour listes structurées avec ligne bleue
            content = "Technologies Frontend • React, Vue.js, Angular • TypeScript, JavaScript ES6+ • CSS3, SASS, Tailwind"
            subtitle = "Comparaison détaillée des stacks technologiques front-end et back-end"
            title = "Stack Technologique Moderne"
            additional_content = [
                "Technologies Backend • Node.js, Python Django • PostgreSQL, MongoDB • Docker, Kubernetes"
            ]

            # Commande pour ajouter la slide explication détaillée
            cmd_07 = [
                sys.executable,
                str(self.script_07_path),
                content,
                "--insert-into", str(base_presentation_path),
                "--title", title,
                "--subtitle", subtitle,
                "--style", "dual_lists_blue",
                "--additional"
            ] + additional_content

            print(f"EXEC Ajout de l'explication detaillee:")
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
                print(f"ERREUR Erreur lors de l'ajout d'explication:")
                print(f"   STDOUT: {result.stdout}")
                print(f"   STDERR: {result.stderr}")
                return False

            # Vérifier que le fichier a été modifié
            if not base_presentation_path.exists():
                print(f"ERREUR Fichier de presentation perdu: {base_presentation_path}")
                return False

            print(f"SUCCES Explication detaillee ajoutee avec succes!")
            print(f"   FICHIER Fichier modifie: {base_presentation_path}")
            print(f"   TAILLE Nouvelle taille: {base_presentation_path.stat().st_size:,} bytes")
            print(f"   CONTENU Principal: {content}")
            print(f"   TITRE: {title}")
            print(f"   SOUS-TITRE: {subtitle}")
            print(f"   LISTES: {len(additional_content)} listes additionnelles")

            return True

        except subprocess.TimeoutExpired:
            print(f"ERREUR Timeout lors de l'ajout d'explication")
            return False
        except Exception as e:
            print(f"ERREUR Erreur lors de l'ajout d'explication: {e}")
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

            print(f"EXEC Execution de la validation:")
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

            print(f"SUCCES Validation reussie!")
            print(f"   RESULTAT Script 07 valide avec succes")

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
        Exécute tous les tests pour le script 07.

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

            # Test 3: Ajout d'explication détaillée (seulement si la base est créée)
            explanation_success = False
            if base_creation_success:
                explanation_success = self.add_explanation_slide(base_presentation_path)

            self.cleanup_test()

            # Résultat final
            all_success = validation_success and base_creation_success and explanation_success

            print(f"\n{'='*60}")
            print(f"STATS RESULTATS DU TEST - {self.test_name}")
            print(f"{'='*60}")
            print(f"TEST Validation script: {'SUCCES REUSSI' if validation_success else 'ERREUR ECHEC'}")
            print(f"CREATION Creation base (script 01): {'SUCCES REUSSI' if base_creation_success else 'ERREUR ECHEC'}")
            print(f"EXPLANATION Ajout explication (script 07): {'SUCCES REUSSI' if explanation_success else 'ERREUR ECHEC'}")
            print(f"FINAL Resultat global: {'SUCCES TOUS LES TESTS REUSSIS' if all_success else 'ERREUR ECHECS DETECTES'}")
            print(f"{'='*60}")

            return all_success

        except Exception as e:
            print(f"ERREUR Erreur critique dans les tests: {e}")
            return False


def main():
    """Point d'entrée principal pour exécuter les tests"""
    test_runner = TestSlide42DualListsBlue()
    success = test_runner.run_all_tests()

    # Code de retour approprié
    exit_code = 0 if success else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()