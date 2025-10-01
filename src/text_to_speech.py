"""
Script simple de synthèse vocale avec ElevenLabs
Génère un fichier audio à partir d'un texte passé en paramètre
"""

import os
import sys
import argparse
from pathlib import Path
import requests

# Configuration par défaut
DEFAULT_VOICE_ID = "93nuHbke4dTER9x2pDwE"  # Voix Sam AI
DEFAULT_MODEL = "eleven_multilingual_v2"  # Modèle multilingue pour l'anglais
DEFAULT_OUTPUT_DIR = "temp_audio"

class TextToSpeech:
    def __init__(self, api_key=None, voice_id=DEFAULT_VOICE_ID, model=DEFAULT_MODEL):
        # Utiliser la même clé par défaut que audio_generator.py
        self.api_key = api_key or os.getenv("ELEVENLABS_API_KEY", "sk_4e1f345f6f99fe90a9e703a4d1fe9f02402000ac412a4876")
        self.voice_id = voice_id
        self.model = model
        self.base_url = "https://api.elevenlabs.io/v1"

        if not self.api_key:
            raise ValueError("Clé API ElevenLabs requise via ELEVENLABS_API_KEY ou paramètre")

    def generate_audio(self, text, output_file):
        """Génère un fichier audio à partir du texte"""
        print(f"Génération audio avec voix Sam AI...")
        print(f"Texte: {text[:100]}{'...' if len(text) > 100 else ''}")

        # Configuration de la requête
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
                "stability": 0.7,
                "similarity_boost": 0.8,
                "style": 0.6,
                "use_speaker_boost": True
            },
            "language_code": "en"  # Force la génération en anglais
        }

        try:
            # Faire la requête
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()

            # Sauvegarder le fichier audio
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, 'wb') as f:
                f.write(response.content)

            print(f"[OK] Audio généré avec succès: {output_path}")
            print(f"Taille: {len(response.content)} bytes")
            return str(output_path)

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Erreur lors de la génération audio: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"Détails: {e.response.text}")
            raise
        except Exception as e:
            print(f"[ERROR] Erreur inattendue: {e}")
            raise

def main():
    """Point d'entrée principal"""
    parser = argparse.ArgumentParser(
        description="Génère un fichier audio à partir d'un texte avec ElevenLabs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python text_to_speech.py "Bonjour tout le monde!"
  python text_to_speech.py "Un texte plus long..." --output mon_audio.mp3
  python text_to_speech.py "Test" --voice autre_voice_id --model eleven_multilingual_v2
        """
    )

    parser.add_argument(
        "text",
        help="Texte à convertir en audio"
    )

    parser.add_argument(
        "--output", "-o",
        help="Fichier de sortie (défaut: texte_audio.mp3)",
        default=None
    )

    parser.add_argument(
        "--voice", "-v",
        help=f"ID de la voix ElevenLabs (défaut: {DEFAULT_VOICE_ID} - Sam AI)",
        default=DEFAULT_VOICE_ID
    )

    parser.add_argument(
        "--model", "-m",
        help=f"Modèle ElevenLabs (défaut: {DEFAULT_MODEL} pour l'anglais)",
        default=DEFAULT_MODEL
    )

    parser.add_argument(
        "--api-key", "-k",
        help="Clé API ElevenLabs (ou utilisez ELEVENLABS_API_KEY)",
        default=None
    )

    args = parser.parse_args()

    # Déterminer le fichier de sortie
    if args.output:
        output_file = args.output
    else:
        # Générer un nom basé sur les premiers mots du texte
        safe_text = "".join(c for c in args.text[:30] if c.isalnum() or c.isspace()).strip()
        safe_text = "_".join(safe_text.split()[:5])
        if not safe_text:
            safe_text = "texte_audio"
        output_file = f"{DEFAULT_OUTPUT_DIR}/{safe_text}.mp3"

    print("=== Générateur Audio ElevenLabs (Anglais) ===")
    print(f"Texte: {args.text}")
    print(f"Voix: {args.voice}")
    print(f"Modèle: {args.model}")
    print(f"Langue: Anglais (en)")
    print(f"Sortie: {output_file}")
    print()

    try:
        # Créer le générateur et générer l'audio
        tts = TextToSpeech(
            api_key=args.api_key,
            voice_id=args.voice,
            model=args.model
        )

        result_file = tts.generate_audio(args.text, output_file)

        print(f"\n[SUCCESS] Génération terminée avec succès!")
        print(f"Fichier créé: {result_file}")

    except Exception as e:
        print(f"\n[ERROR] Erreur: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()