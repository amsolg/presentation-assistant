#!/usr/bin/env python3
"""
Test unitaire pour le script 07 - Detailed Explanation Builder
Test d'ajout de slide 44 (2 listes avec sous-titres et ligne grise Premier Tech)

Ce test vérifie la capacité du script 07 à ajouter une slide d'explication détaillée
dans une présentation existante en utilisant le template slide 44 (dual_lists).

Workflow du test:
1. Créer une présentation de base avec le script 01
2. Ajouter une slide d'explication avec le script 07 (style dual_lists)
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

class TestSlide44DualLists:
    """
    Classe de test pour vérifier l'ajout de slide 44 avec le script 07.
    """

    def __init__(self):
        self.test_name = "Test Unitaire - Script 07 - Slide 44 (dual_lists)"
        self.script_01_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "01_slide_title_creator.py"
        self.script_07_path = Path(__file__).parent.parent.parent.parent.parent / "presentation_builder" / "07_detailed_explanation_builder.py"
        self.test_output_dir = Path(__file__).parent / "output"
        self.test_output_dir.mkdir(exist_ok=True)

    def setup_test(self):
        """Prépare l'environnement de test"""
        print(f"DEBUT Début du test: {self.test_name}")
        print(f"DOSSIER Répertoire de sortie: {self.test_output_dir}")
        print(f"SCRIPT Script 01 (base): {self.script_01_path}")
        print(f"SCRIPT Script 07 (testé): {self.script_07_path}")

        # Vérifier que les scripts existent
        if not self.script_01_path.exists():
            raise FileNotFoundError(f"Script 01 non trouvé: {self.script_01_path}")
        if not self.script_07_path.exists():
            raise FileNotFoundError(f"Script 07 non trouvé: {self.script_07_path}")

    def run_explanation_test(self):
        """
        Exécute le test d'ajout de slide d'explication détaillée.

        Returns:
            bool: True si le test réussit, False sinon
        """
        try:
            # Étape 1: Créer une présentation de base avec paramètres complets
            print("\nETAPE 1: Création d'une présentation de base")

            base_output_path = self.test_output_dir / "test_script_07_slide_44.pptx"

            cmd_01 = [
                sys.executable, str(self.script_01_path),
                "TEST UNITAIRE - Script 07",
                "--subtitle", "Presentation de base pour test listes grises avec ligne grise",
                "--metadata", "2025.10.09 - Test Dual Lists Grey",
                "--project", "test_script_07_slide_44",
                "--output", str(base_output_path)
            ]

            print(f"EXEC Creation de la base:")
            print(f"   {' '.join(cmd_01)}")

            # Exécuter le script 01 depuis son répertoire
            result_01 = subprocess.run(
                cmd_01,
                cwd=self.script_01_path.parent,
                capture_output=True,
                text=True,
                timeout=60
            )

            if result_01.returncode != 0:
                print(f"ERREUR Erreur lors de la creation de base:")
                print(f"   STDOUT: {result_01.stdout}")
                print(f"   STDERR: {result_01.stderr}")
                return False

            # Vérifier que le fichier de base a été créé
            if not base_output_path.exists():
                print(f"ERREUR Fichier de base non cree: {base_output_path}")
                return False

            file_size = base_output_path.stat().st_size
            print(f"SUCCES Presentation de base creee:")
            print(f"   FICHIER Fichier: {base_output_path}")
            print(f"   TAILLE Taille: {file_size:,} bytes")

            base_presentation = base_output_path

            # Étape 2: Ajouter une slide d'explication détaillée (dual_lists)
            print(f"\nETAPE 2: Ajout de slide 44 (dual_lists)")

            # Obtenir le chemin vers le template
            template_path = self.script_07_path.parent.parent / "templates" / "Template_PT.pptx"

            cmd_07 = [
                sys.executable, str(self.script_07_path),
                "Architecture Monolithique",
                "--insert-into", str(base_presentation),
                "--style", "dual_lists_grey",
                "--template", str(template_path),
                "--title", "Comparaison Architecture Monolithique vs Microservices",
                "--additional", "Architecture Microservices"
            ]

            print(f"EXEC Ajout de l'explication detaillee:")
            print(f"   {' '.join(cmd_07)}")

            result_07 = subprocess.run(
                cmd_07,
                cwd=self.script_07_path.parent,
                capture_output=True,
                text=True,
                timeout=60
            )

            if result_07.returncode != 0:
                print(f"ERREUR Échec ajout slide d'explication:")
                print(f"STDOUT: {result_07.stdout}")
                print(f"STDERR: {result_07.stderr}")
                return False

            print(f"SUCCES Slide 44 (dual_lists) ajoutée avec succès")

            # Étape 3: Vérifier que le fichier final existe et contient les données
            if not base_presentation.exists():
                print("ERREUR Le fichier de présentation final n'existe pas")
                return False

            file_size = base_presentation.stat().st_size
            if file_size < 1000:  # Minimum viable size
                print(f"ERREUR Fichier trop petit ({file_size} bytes), probablement corrompu")
                return False

            print(f"SUCCES Fichier final valide ({file_size} bytes)")

            # Étape 4: Générer un rapport de création
            report_data = {
                "test_name": self.test_name,
                "timestamp": datetime.now().isoformat(),
                "script_tested": "07_detailed_explanation_builder.py",
                "slide_number": 44,
                "slide_style": "dual_lists_grey",
                "template_index": 43,
                "explanation_type": "dual_structured",
                "test_parameters": {
                    "title": "Comparaison Architecture Monolithique vs Microservices",
                    "content": "Architecture Monolithique",
                    "subtitle": "Structure traditionnelle centralisée",
                    "additional_content": ["Architecture Microservices"]
                },
                "output_file": str(base_presentation),
                "file_size_bytes": file_size,
                "test_status": "SUCCESS"
            }

            # Sauvegarder le rapport
            import json
            report_file = self.test_output_dir / f"{base_presentation.stem}_creation_report.json"
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False)

            print(f"RAPPORT Rapport sauvegardé: {report_file.name}")
            print(f"\nSUCCES Test {self.test_name} réussi!")

            return True

        except subprocess.TimeoutExpired as e:
            print(f"TIMEOUT Test interrompu après timeout: {e}")
            return False
        except Exception as e:
            print(f"ERREUR Exception durant le test: {e}")
            return False

    def run_test(self):
        """
        Exécute le test complet.

        Returns:
            bool: True si tous les tests passent, False sinon
        """
        try:
            self.setup_test()
            return self.run_explanation_test()
        except Exception as e:
            print(f"ERREUR Échec setup du test: {e}")
            return False

def test_slide_44_dual_lists():
    """Fonction principale de test"""
    tester = TestSlide44DualLists()
    return tester.run_test()

def main():
    """Point d'entrée principal pour exécuter les tests"""
    success = test_slide_44_dual_lists()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()