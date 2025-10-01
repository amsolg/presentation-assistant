#!/usr/bin/env python3
"""
Script pour générer l'audio des présentations avec ElevenLabs
Utilise la voix Felix Tabarnak pour convertir les speaker_notes en audio
"""

import json
import os
import sys
import requests
from pathlib import Path
import argparse


class ElevenLabsAudioGenerator:
    """Générateur audio utilisant l'API ElevenLabs"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('ELEVENLABS_API_KEY') or "sk_4e1f345f6f99fe90a9e703a4d1fe9f02402000ac412a4876"
        if not self.api_key:
            raise ValueError("API key ElevenLabs non trouvée. Définir ELEVENLABS_API_KEY ou passer en paramètre")
        
        self.voice_id = "93nuHbke4dTER9x2pDwE"  # Nouvelle voix
        self.model = "eleven_turbo_v2_5"  # Eleven Turbo v2.5
        self.base_url = "https://api.elevenlabs.io/v1"
    
    def generate_audio(self, text: str, output_path: str) -> bool:
        """
        Génère l'audio pour un texte donné et sauvegarde dans output_path
        
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
        
        data = {
            "text": text,
            "model_id": self.model,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.8,
                "style": 0.6,
                "use_speaker_boost": True
            }
        }
        
        try:
            response = requests.post(url, json=data, headers=headers)
            
            # Vérifier si erreur de crédit insuffisant
            if response.status_code == 402:
                print(f"ERREUR: Credit insuffisant pour generer l'audio")
                print(f"   Verifiez votre solde ElevenLabs")
                return False
            
            # Autres erreurs d'API
            if response.status_code != 200:
                error_msg = "Erreur inconnue"
                try:
                    error_data = response.json()
                    error_msg = error_data.get('detail', {}).get('message', error_msg)
                except:
                    error_msg = f"Status {response.status_code}: {response.text}"
                
                print(f"ERREUR API ElevenLabs: {error_msg}")
                return False
            
            # Sauvegarder l'audio
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            print(f"Audio genere: {output_path}")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"ERREUR de reseau: {e}")
            return False
        except Exception as e:
            print(f"ERREUR inattendue: {e}")
            return False


def process_json_file(json_file_path: str, api_key: str = None) -> bool:
    """
    Traite un fichier JSON pour générer l'audio de toutes les scènes
    
    Args:
        json_file_path: Chemin vers le fichier JSON
        api_key: Clé API ElevenLabs (optionnel)
        
    Returns:
        bool: True si tous les audios ont été générés avec succès
    """
    json_path = Path(json_file_path)
    
    if not json_path.exists():
        print(f"ERREUR: Fichier JSON non trouve: {json_file_path}")
        return False
    
    # Charger le JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            slide_data = json.load(f)
    except Exception as e:
        print(f"ERREUR lors du chargement du JSON: {e}")
        return False
    
    # Initialiser le générateur audio
    try:
        generator = ElevenLabsAudioGenerator(api_key)
    except ValueError as e:
        print(f"{e}")
        return False
    
    # Obtenir le nom du fichier sans extension pour nommer les audios
    json_name = json_path.stem
    output_dir = json_path.parent
    
    success_count = 0
    total_scenes = 0
    
    # Traiter chaque scène
    scenes = slide_data.get('scenes', [])
    if not scenes:
        print("Aucune scene trouvee dans le fichier JSON")
        return True
    
    print(f"Traitement de {len(scenes)} scene(s) dans {json_path.name}")
    
    for scene in scenes:
        scene_id = scene.get('scene_id', 'unknown')
        speaker_notes = scene.get('speaker_notes', '')
        
        if not speaker_notes:
            print(f"Scene {scene_id}: Pas de speaker_notes, ignoree")
            continue
        
        total_scenes += 1
        
        # Générer le nom du fichier audio
        audio_filename = f"{json_name}_{scene_id}.mp3"
        audio_path = output_dir / audio_filename
        
        print(f"Generation audio pour scene {scene_id}...")
        print(f"   Texte: {speaker_notes[:100]}{'...' if len(speaker_notes) > 100 else ''}")
        
        # Générer l'audio
        if generator.generate_audio(speaker_notes, str(audio_path)):
            success_count += 1
        else:
            print(f"Echec generation audio pour scene {scene_id}")
    
    # Résumé
    print(f"\nRESUME:")
    print(f"   Scenes traitees: {total_scenes}")
    print(f"   Audios generes avec succes: {success_count}")
    print(f"   Echecs: {total_scenes - success_count}")
    
    return success_count == total_scenes


def main():
    """Point d'entrée principal du script"""
    parser = argparse.ArgumentParser(
        description="Génère l'audio des speaker_notes d'un fichier JSON avec ElevenLabs"
    )
    parser.add_argument(
        'json_file', 
        help='Chemin vers le fichier JSON à traiter'
    )
    parser.add_argument(
        '--api-key', 
        help='Clé API ElevenLabs (utilise ELEVENLABS_API_KEY si non spécifié)'
    )
    
    args = parser.parse_args()
    
    print("GENERATEUR AUDIO ELEVENLABS")
    print("=" * 50)
    print(f"Fichier JSON: {args.json_file}")
    print(f"Voix: Nouvelle voix (93nuHbke4dTER9x2pDwE)")
    print(f"Modele: eleven_turbo_v2_5")
    print()
    
    success = process_json_file(args.json_file, args.api_key)
    
    if success:
        print("\nSUCCES: Tous les audios ont ete generes!")
        sys.exit(0)
    else:
        print("\nECHEC: Certains audios n'ont pas pu etre generes")
        sys.exit(1)


if __name__ == "__main__":
    main()