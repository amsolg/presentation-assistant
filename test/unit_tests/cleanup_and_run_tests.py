#!/usr/bin/env python3
"""
Script de nettoyage et d'exécution des tests unitaires
- Supprime récursivement tous les dossiers nommés "output" dans test/unit_tests
- Exécute tous les scripts nommés "run_test" trouvés récursivement
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def find_and_remove_output_dirs(base_path):
    """
    Trouve et supprime récursivement tous les dossiers nommés 'output'

    Args:
        base_path (Path): Chemin de base pour la recherche

    Returns:
        list: Liste des dossiers supprimés
    """
    removed_dirs = []

    for root, dirs, files in os.walk(base_path):
        # Créer une copie de la liste pour éviter les modifications pendant l'itération
        dirs_to_check = dirs.copy()
        for dir_name in dirs_to_check:
            if dir_name == "output":
                output_path = Path(root) / dir_name
                try:
                    shutil.rmtree(output_path)
                    removed_dirs.append(str(output_path))
                    print(f"[REMOVED] {output_path}")
                    # Retirer le dossier de la liste pour éviter de descendre dedans
                    dirs.remove(dir_name)
                except Exception as e:
                    print(f"[ERROR] Suppression de {output_path}: {e}")

    return removed_dirs


def find_run_test_scripts(base_path):
    """
    Trouve récursivement tous les scripts nommés 'run_test'

    Args:
        base_path (Path): Chemin de base pour la recherche

    Returns:
        list: Liste des chemins vers les scripts run_test
    """
    run_test_scripts = []

    for root, dirs, files in os.walk(base_path):
        for file_name in files:
            if file_name.startswith("run_test") and file_name.endswith(".py"):
                script_path = Path(root) / file_name
                run_test_scripts.append(script_path)

    return sorted(run_test_scripts)


def run_test_script(script_path):
    """
    Exécute un script de test et retourne le résultat

    Args:
        script_path (Path): Chemin vers le script à exécuter

    Returns:
        tuple: (success: bool, output: str, error: str)
    """
    try:
        # Changer vers le répertoire du script pour l'exécution
        original_cwd = os.getcwd()
        script_dir = script_path.parent
        os.chdir(script_dir)

        # Exécuter le script
        result = subprocess.run(
            [sys.executable, script_path.name],
            capture_output=True,
            text=True,
            timeout=120  # Timeout de 2 minutes par test
        )

        # Revenir au répertoire original
        os.chdir(original_cwd)

        success = result.returncode == 0
        return success, result.stdout, result.stderr

    except subprocess.TimeoutExpired:
        os.chdir(original_cwd)
        return False, "", "Timeout: Le script a pris plus de 2 minutes à s'exécuter"
    except Exception as e:
        os.chdir(original_cwd)
        return False, "", f"Erreur lors de l'exécution: {str(e)}"


def main():
    """Fonction principale"""
    print("[CLEAN] Script de nettoyage et d'exécution des tests unitaires")
    print("=" * 60)

    # Définir le chemin de base
    script_dir = Path(__file__).parent
    base_path = script_dir

    print(f"[PATH] Répertoire de base: {base_path}")
    print()

    # Étape 1: Nettoyer les dossiers output
    print("[STEP 1] Suppression des dossiers 'output'")
    print("-" * 40)

    removed_dirs = find_and_remove_output_dirs(base_path)

    if removed_dirs:
        print(f"[OK] {len(removed_dirs)} dossier(s) 'output' supprimé(s)")
    else:
        print("[INFO] Aucun dossier 'output' trouvé")

    print()

    # Étape 2: Trouver et exécuter les scripts de test
    print("[STEP 2] Exécution des scripts de test")
    print("-" * 40)

    test_scripts = find_run_test_scripts(base_path)

    if not test_scripts:
        print("[INFO] Aucun script 'run_test' trouvé")
        return

    print(f"[FOUND] {len(test_scripts)} script(s) de test trouvé(s)")
    print()

    # Statistiques de test
    total_tests = len(test_scripts)
    successful_tests = 0
    failed_tests = 0
    test_results = []

    # Exécuter chaque script de test
    for i, script_path in enumerate(test_scripts, 1):
        relative_path = script_path.relative_to(base_path)
        print(f"[{i}/{total_tests}] [RUN] Exécution: {relative_path}")

        success, stdout, stderr = run_test_script(script_path)

        if success:
            print(f"[{i}/{total_tests}] [SUCCESS] {relative_path}")
            successful_tests += 1
        else:
            print(f"[{i}/{total_tests}] [FAIL] {relative_path}")
            if stderr:
                print(f"    Erreur: {stderr.strip()}")
            failed_tests += 1

        test_results.append({
            'script': relative_path,
            'success': success,
            'stdout': stdout,
            'stderr': stderr
        })

        print()

    # Résumé final
    print("[SUMMARY] Résumé des tests")
    print("=" * 60)
    print(f"Total des tests: {total_tests}")
    print(f"[SUCCESS] {successful_tests} tests réussis")
    print(f"[FAIL] {failed_tests} tests échoués")
    print(f"[RATE] Taux de réussite: {(successful_tests/total_tests)*100:.1f}%")

    if failed_tests > 0:
        print()
        print("[FAILED] Tests en échec:")
        for result in test_results:
            if not result['success']:
                print(f"  - {result['script']}")
                if result['stderr']:
                    print(f"    Erreur: {result['stderr'].strip()}")

    print()
    print("[DONE] Nettoyage et exécution des tests terminés!")

    # Code de sortie basé sur les résultats
    sys.exit(0 if failed_tests == 0 else 1)


if __name__ == "__main__":
    main()