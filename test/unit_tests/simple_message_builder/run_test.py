#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de lancement des tests pour simple_message_builder
Exécute tous les tests de configuration JSON pour ce module.
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime

def find_test_configs():
    """Trouve tous les fichiers de configuration de test"""
    test_dir = Path(__file__).parent
    configs = []

    for root, dirs, files in os.walk(test_dir):
        for file in files:
            if file == 'presentation_schema.json':
                config_path = Path(root) / file
                configs.append(config_path)

    return sorted(configs)

def run_presentation_builder_test(config_path: Path):
    """
    Exécute un test avec presentation_builder.py

    Args:
        config_path: Chemin vers le fichier de configuration

    Returns:
        tuple: (success: bool, output: str)
    """
    try:
        # Chemin vers presentation_builder.py
        script_dir = Path(__file__).parent.parent.parent.parent
        builder_script = script_dir / "presentation_builder" / "presentation_builder.py"

        if not builder_script.exists():
            return False, f"presentation_builder.py non trouvé: {builder_script}"

        # Commande d'exécution
        cmd = [sys.executable, str(builder_script), str(config_path)]

        # Exécuter
        result = subprocess.run(
            cmd,
            cwd=str(builder_script.parent),
            capture_output=True,
            text=True,
            timeout=120
        )

        success = result.returncode == 0
        output = f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"

        return success, output

    except subprocess.TimeoutExpired:
        return False, "Timeout: Test trop long"
    except Exception as e:
        return False, f"Erreur: {e}"

def main():
    """Fonction principale"""
    print(f"=== TESTS UNITAIRES - SIMPLE_MESSAGE_BUILDER ===")
    print(f"Architecture JSON 2025")
    print("=" * 60)

    # Trouver toutes les configurations de test
    test_configs = find_test_configs()

    if not test_configs:
        print("[ERROR] Aucune configuration de test trouvée")
        return 1

    print(f"Configurations trouvées: {len(test_configs)}")
    for config in test_configs:
        relative_path = config.relative_to(Path(__file__).parent)
        print(f"  - {relative_path}")
    print()

    # Exécuter chaque test
    total_tests = len(test_configs)
    successful_tests = 0
    failed_tests = 0
    test_results = []

    for i, config_path in enumerate(test_configs, 1):
        relative_path = config_path.relative_to(Path(__file__).parent)
        print(f"[{i}/{total_tests}] Test: {relative_path}")

        # Lire la configuration pour afficher les détails
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)

            presentation_name = config_data.get('presentation_name', 'N/A')
            slides_count = len(config_data.get('slides', []))
            expected_slides = slides_count + 2  # +1 titre +1 fermeture

            print(f"   Nom: {presentation_name}")
            print(f"   Slides de contenu: {slides_count}")
            print(f"   Total attendu: {expected_slides} slides")

        except Exception as e:
            print(f"   [WARNING] Erreur lecture config: {e}")

        # Exécuter le test
        success, output = run_presentation_builder_test(config_path)

        if success:
            print(f"   [SUCCESS] Test réussi")
            successful_tests += 1
        else:
            print(f"   [FAIL] Test échoué")
            print(f"   {output[:200]}...")  # Afficher les premiers 200 caractères
            failed_tests += 1

        test_results.append({
            'config': str(relative_path),
            'success': success,
            'output': output
        })

        print()

    # Rapport final
    print("=" * 60)
    print("RAPPORT FINAL")
    print("=" * 60)
    print(f"Total des tests: {total_tests}")
    print(f"Succès: {successful_tests}")
    print(f"Échecs: {failed_tests}")
    success_rate = (successful_tests / total_tests * 100) if total_tests > 0 else 0
    print(f"Taux de réussite: {success_rate:.1f}%")

    if failed_tests > 0:
        print("\nTests en échec:")
        for result in test_results:
            if not result['success']:
                print(f"  - {result['config']}")

    # Sauvegarder le rapport
    try:
        output_dir = Path(__file__).parent / "output"
        output_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = output_dir / f"test_simple_message_builder_{timestamp}_report.json"

        report_data = {
            "timestamp": datetime.now().isoformat(),
            "module": "simple_message_builder",
            "total_tests": total_tests,
            "successful_tests": successful_tests,
            "failed_tests": failed_tests,
            "success_rate": success_rate,
            "test_results": test_results
        }

        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, ensure_ascii=False, indent=2)

        print(f"\nRapport sauvegardé: {report_path}")

    except Exception as e:
        print(f"\n[WARNING] Erreur sauvegarde rapport: {e}")

    return 0 if failed_tests == 0 else 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
