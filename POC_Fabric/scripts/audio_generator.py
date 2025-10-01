#!/usr/bin/env python3
"""
Script pour générer l'audio des présentations POC_Fabric avec ElevenLabs
Utilise la voix Sam AI pour convertir les speaker_notes en audio
Adapté pour les slides POC Microsoft Fabric
"""

import json
import os
import sys
import requests
from pathlib import Path
import argparse
from typing import List, Dict, Optional


class ElevenLabsAudioGenerator:
    """Générateur audio utilisant l'API ElevenLabs avec la voix Sam AI"""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('ELEVENLABS_API_KEY') or "sk_4e1f345f6f99fe90a9e703a4d1fe9f02402000ac412a4876"
        if not self.api_key:
            raise ValueError("API key ElevenLabs non trouvée. Définir ELEVENLABS_API_KEY ou passer en paramètre")

        # Configuration Sam AI - voix énergique et enthousiaste
        self.voice_id = "93nuHbke4dTER9x2pDwE"  # Voix Sam AI
        self.model = "eleven_turbo_v2_5"  # Eleven Turbo v2.5 pour latence optimale
        self.base_url = "https://api.elevenlabs.io/v1"

    def generate_audio(self, text: str, output_path: str) -> bool:
        """
        Génère l'audio pour un texte donné et sauvegarde dans output_path
        Optimisé pour la personnalité enthousiaste de Sam

        Args:
            text: Texte à convertir en audio
            output_path: Chemin de sortie pour le fichier audio

        Returns:
            bool: True si succès, False sinon
        """
        url = f"{self.base_url}/text-to-speech/{self.voice_id}"

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }

        # Configuration voix optimisée pour Sam AI - enthousiasme et énergie
        data = {
            "text": text,
            "model_id": self.model,
            "voice_settings": {
                "stability": 0.7,  # Équilibre créativité/cohérence pour Sam
                "similarity_boost": 0.8,  # Fidélité à la voix clonée Sam
                "style": 0.6,  # Expressivité élevée pour l'enthousiasme de Sam
                "use_speaker_boost": True  # Amélioration qualité vocale
            }
        }

        try:
            response = requests.post(url, json=data, headers=headers)

            # Vérifier si erreur de crédit insuffisant
            if response.status_code == 402:
                print(f"[ERREUR] Crédit insuffisant pour générer l'audio")
                print(f"         Vérifiez votre solde ElevenLabs")
                return False

            # Autres erreurs d'API
            if response.status_code != 200:
                error_msg = "Erreur inconnue"
                try:
                    error_data = response.json()
                    error_msg = error_data.get('detail', {}).get('message', error_msg)
                except:
                    error_msg = f"Status {response.status_code}: {response.text}"

                print(f"[ERREUR] API ElevenLabs: {error_msg}")
                return False

            # Sauvegarder l'audio
            with open(output_path, 'wb') as f:
                f.write(response.content)

            print(f"[OK] Audio généré: {output_path}")
            return True

        except requests.exceptions.RequestException as e:
            print(f"[ERREUR] Réseau: {e}")
            return False
        except Exception as e:
            print(f"[ERREUR] Inattendue: {e}")
            return False


def process_single_slide(json_file_path: str, generator: ElevenLabsAudioGenerator, output_dir: Path = None) -> bool:
    """
    Traite un fichier JSON de slide pour générer l'audio

    Args:
        json_file_path: Chemin vers le fichier JSON
        generator: Instance du générateur audio
        output_dir: Répertoire de sortie pour les audios (optionnel)

    Returns:
        bool: True si l'audio a été généré avec succès
    """
    json_path = Path(json_file_path)

    if not json_path.exists():
        print(f"[ERREUR] Fichier JSON non trouvé: {json_file_path}")
        return False

    # Charger le JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            slide_data = json.load(f)
    except Exception as e:
        print(f"[ERREUR] Chargement du JSON: {e}")
        return False

    # Déterminer le répertoire de sortie
    if output_dir is None:
        output_dir = json_path.parent.parent / "audio"
        output_dir.mkdir(exist_ok=True)

    slide_number = slide_data.get('slide_number', 'unknown')
    slide_title = slide_data.get('slide_title', 'Untitled')

    success = True

    # Traiter chaque scène
    scenes = slide_data.get('scenes', [])
    if not scenes:
        print(f"[INFO] Slide {slide_number}: Aucune scène trouvée")
        return True

    for scene in scenes:
        scene_id = scene.get('scene_id', 'unknown')
        speaker_notes = scene.get('speaker_notes', '')

        if not speaker_notes or speaker_notes.strip() == "":
            print(f"[INFO] Slide {slide_number}, Scène {scene_id}: Pas de speaker_notes")
            continue

        # Générer le nom du fichier audio
        audio_filename = f"slide_{slide_number:02d}_scene_{scene_id}.mp3"
        audio_path = output_dir / audio_filename

        print(f"[PROCESSING] Slide {slide_number} ({slide_title[:30]}...) - Scène {scene_id}")
        print(f"             Texte: {speaker_notes[:80]}{'...' if len(speaker_notes) > 80 else ''}")

        # Générer l'audio
        if not generator.generate_audio(speaker_notes, str(audio_path)):
            print(f"[ERREUR] Échec génération audio pour slide {slide_number}, scène {scene_id}")
            success = False

    return success


def process_slide_range(start: int, end: int, scripts_dir: Path, api_key: str = None) -> bool:
    """
    Traite une plage de slides pour générer les audios

    Args:
        start: Numéro de la première slide
        end: Numéro de la dernière slide
        scripts_dir: Répertoire contenant les fichiers JSON
        api_key: Clé API ElevenLabs (optionnel)

    Returns:
        bool: True si tous les audios ont été générés avec succès
    """
    # Initialiser le générateur audio
    try:
        generator = ElevenLabsAudioGenerator(api_key)
    except ValueError as e:
        print(f"[ERREUR] {e}")
        return False

    # Créer le dossier audio s'il n'existe pas
    audio_dir = scripts_dir.parent / "audio"
    audio_dir.mkdir(exist_ok=True)

    success_count = 0
    failed_slides = []

    for slide_num in range(start, end + 1):
        json_file = scripts_dir / f"slide_{slide_num:02d}.json"

        if not json_file.exists():
            print(f"[WARNING] Slide {slide_num}: Fichier non trouvé, ignoré")
            continue

        if process_single_slide(str(json_file), generator, audio_dir):
            success_count += 1
        else:
            failed_slides.append(slide_num)

    # Résumé
    total_processed = (end - start + 1)
    print(f"\n{'='*60}")
    print(f"RÉSUMÉ DE GÉNÉRATION AUDIO - POC FABRIC")
    print(f"{'='*60}")
    print(f"Plage traitée: Slides {start} à {end}")
    print(f"Slides avec audio généré: {success_count}/{total_processed}")

    if failed_slides:
        print(f"Slides avec échecs: {', '.join(map(str, failed_slides))}")

    return len(failed_slides) == 0


def main():
    """Point d'entrée principal du script POC_Fabric"""
    parser = argparse.ArgumentParser(
        description="Génère l'audio des speaker_notes pour POC_Fabric avec Sam AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python audio_generator.py                      # Génère l'audio pour toutes les slides
  python audio_generator.py --slides 2-11        # Génère l'audio pour les slides 2 à 11
  python audio_generator.py --slide 5            # Génère l'audio pour la slide 5 seulement
  python audio_generator.py slide_05.json        # Génère l'audio pour un fichier JSON spécifique
        """
    )

    parser.add_argument(
        'json_file',
        nargs='?',
        help='Fichier JSON spécifique à traiter (optionnel)'
    )

    parser.add_argument(
        '--slides',
        help='Plage de slides à traiter (ex: "2-11")'
    )

    parser.add_argument(
        '--slide',
        type=int,
        help='Numéro de slide unique à traiter'
    )

    parser.add_argument(
        '--api-key',
        help='Clé API ElevenLabs (utilise ELEVENLABS_API_KEY si non spécifié)'
    )

    parser.add_argument(
        '--scripts-dir',
        default='.',
        help='Répertoire contenant les fichiers JSON (défaut: répertoire courant)'
    )

    args = parser.parse_args()

    print("="*60)
    print("GÉNÉRATEUR AUDIO SAM AI - POC MICROSOFT FABRIC")
    print("="*60)
    print(f"Voix: Sam AI (enthousiaste et énergique)")
    print(f"Modèle: eleven_turbo_v2_5 (latence optimale)")
    print(f"Personnalité: Passionné de technologie avec énergie contagieuse")
    print()

    scripts_dir = Path(args.scripts_dir)

    # Cas 1: Fichier JSON spécifique fourni
    if args.json_file:
        try:
            generator = ElevenLabsAudioGenerator(args.api_key)
            success = process_single_slide(args.json_file, generator)
        except ValueError as e:
            print(f"[ERREUR] {e}")
            sys.exit(1)

    # Cas 2: Plage de slides spécifiée
    elif args.slides:
        try:
            if '-' in args.slides:
                start, end = map(int, args.slides.split('-'))
            else:
                start = end = int(args.slides)

            success = process_slide_range(start, end, scripts_dir, args.api_key)
        except ValueError:
            print(f"[ERREUR] Format de plage invalide: {args.slides}")
            print("         Utilisez le format '2-11' ou '5'")
            sys.exit(1)

    # Cas 3: Slide unique spécifiée
    elif args.slide:
        success = process_slide_range(args.slide, args.slide, scripts_dir, args.api_key)

    # Cas 4: Traiter toutes les slides disponibles
    else:
        # Détecter toutes les slides disponibles
        slide_files = sorted(scripts_dir.glob("slide_*.json"))
        if not slide_files:
            print(f"[ERREUR] Aucun fichier slide_*.json trouvé dans {scripts_dir}")
            sys.exit(1)

        # Extraire les numéros de slides
        slide_numbers = []
        for f in slide_files:
            try:
                num = int(f.stem.split('_')[1])
                slide_numbers.append(num)
            except (ValueError, IndexError):
                continue

        if slide_numbers:
            start = min(slide_numbers)
            end = max(slide_numbers)
            print(f"[INFO] Détection automatique: Slides {start} à {end}")
            success = process_slide_range(start, end, scripts_dir, args.api_key)
        else:
            print("[ERREUR] Aucune slide valide détectée")
            success = False

    if success:
        print("\n[SUCCESS] Génération audio terminée avec succès!")
        print("          Sam AI a transmis tout son enthousiasme dans les narrations!")
        sys.exit(0)
    else:
        print("\n[ÉCHEC] Certains audios n'ont pas pu être générés")
        sys.exit(1)


if __name__ == "__main__":
    main()