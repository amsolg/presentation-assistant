"""
Script d'automatisation de présentation PowerPoint avec narration audio synchronisée
Ouvre PowerPoint, lance la présentation et joue les fichiers MP3 en séquence
"""

import os
import time
import subprocess
import pygame
import keyboard
from pathlib import Path
import glob
try:
    import win32com.client
    from win32com.client import Dispatch
    POWERPOINT_AVAILABLE = True
except ImportError:
    print("ATTENTION: pywin32 non disponible, utilisation du mode alternatif")
    POWERPOINT_AVAILABLE = False


class PowerPointPresenter:
    def __init__(self, presentation_path, audio_folder):
        self.presentation_path = Path(presentation_path).resolve()
        self.audio_folder = Path(audio_folder).resolve()
        self.powerpoint_app = None
        self.presentation = None
        
        # Initialiser pygame pour la lecture audio
        pygame.mixer.init()
        
    def get_audio_files(self):
        """Récupère les fichiers MP3 triés par numéro (01-52)"""
        pattern = str(self.audio_folder / "slide_*.mp3")
        audio_files = glob.glob(pattern)
        
        # Trier par numéro de slide
        audio_files.sort(key=lambda x: int(Path(x).stem.split('_')[1]))
        
        print(f"Fichiers audio trouvés: {len(audio_files)}")
        for i, file in enumerate(audio_files[:5]):  # Afficher les 5 premiers
            print(f"  {i+1}: {Path(file).name}")
        if len(audio_files) > 5:
            print(f"  ... et {len(audio_files)-5} autres")
            
        return audio_files
    
    def open_powerpoint(self):
        """Ouvre PowerPoint et charge la présentation"""
        print(f"Ouverture de PowerPoint avec: {self.presentation_path}")
        
        if POWERPOINT_AVAILABLE:
            try:
                # Créer une instance de PowerPoint
                self.powerpoint_app = Dispatch("PowerPoint.Application")
                self.powerpoint_app.Visible = True
                
                # Ouvrir la présentation
                self.presentation = self.powerpoint_app.Presentations.Open(str(self.presentation_path))
                print("Présentation ouverte avec succès")
                
                # Attendre que PowerPoint soit prêt
                time.sleep(2)
                return
                
            except Exception as e:
                print(f"Erreur avec COM: {e}")
        
        # Mode alternatif: ouvrir avec subprocess
        print("Ouverture de PowerPoint en mode alternatif...")
        try:
            subprocess.Popen([str(self.presentation_path)], shell=True)
            time.sleep(5)  # Attendre que PowerPoint s'ouvre
            print("PowerPoint ouvert en mode alternatif")
        except Exception as e:
            print(f"Erreur lors de l'ouverture: {e}")
            raise
    
    def start_slideshow(self):
        """Démarre le mode présentation avec F5"""
        print("Démarrage du mode présentation...")
        
        if POWERPOINT_AVAILABLE and self.presentation:
            try:
                # Démarrer le diaporama via COM
                self.presentation.SlideShowSettings.Run()
                print("Mode présentation démarré via COM")
                time.sleep(3)
                return
            except Exception as e:
                print(f"Erreur avec COM: {e}")
        
        # Fallback: utiliser F5 directement
        print("Démarrage avec F5...")
        keyboard.press_and_release('f5')
        time.sleep(3)
    
    def play_audio_file(self, audio_file):
        """Joue un fichier audio et attend la fin"""
        print(f"Lecture de: {Path(audio_file).name}")
        
        try:
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            
            # Attendre que l'audio se termine
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
                
            print(f"Fin de lecture: {Path(audio_file).name}")
            
        except Exception as e:
            print(f"Erreur lors de la lecture audio: {e}")
            # Attendre un délai par défaut si l'audio ne peut pas être lu
            time.sleep(5)
    
    def next_slide(self):
        """Avance à la slide suivante"""
        print("Passage à la slide suivante...")
        
        try:
            # Utiliser la flèche droite pour avancer
            keyboard.press_and_release('right')
            time.sleep(1.0)  # Attendre 1 seconde après le changement de slide
            
        except Exception as e:
            print(f"Erreur lors du changement de slide: {e}")
    
    def run_presentation(self):
        """Exécute la présentation complète avec audio synchronisé"""
        try:
            # 1. Récupérer les fichiers audio
            audio_files = self.get_audio_files()
            
            if not audio_files:
                print("Aucun fichier audio trouvé!")
                return
            
            # 2. Attendre que l'utilisateur ouvre PowerPoint manuellement
            print("Veuillez ouvrir PowerPoint et la présentation manuellement...")
            print("Attente de 5 secondes avant de démarrer...")
            time.sleep(5)
            
            # 3. La présentation doit déjà être en mode diaporama
            print("La présentation doit déjà être en mode diaporama...")
            time.sleep(3)
            
            print(f"\nDémarrage de la présentation avec {len(audio_files)} slides...")
            print("Appuyez sur 'q' pour quitter à tout moment")
            
            # 4. Jouer chaque audio et avancer les slides
            for i, audio_file in enumerate(audio_files):
                # Vérifier si l'utilisateur veut quitter
                if keyboard.is_pressed('q'):
                    print("\nArrêt demandé par l'utilisateur")
                    break
                
                print(f"\n--- Slide {i+1}/{len(audio_files)} ---")
                
                # Jouer l'audio
                self.play_audio_file(audio_file)
                
                # Avancer à la slide suivante (sauf pour la dernière)
                if i < len(audio_files) - 1:
                    self.next_slide()
                else:
                    print("Présentation terminée!")
            
        except KeyboardInterrupt:
            print("\nPrésentation interrompue par l'utilisateur")
        except Exception as e:
            print(f"Erreur durant la présentation: {e}")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Nettoie les ressources"""
        try:
            pygame.mixer.quit()
            
            if self.presentation:
                # Fermer la présentation si elle est ouverte
                try:
                    self.presentation.Close()
                except:
                    pass
            
            if self.powerpoint_app:
                # Quitter PowerPoint si nécessaire
                try:
                    self.powerpoint_app.Quit()
                except:
                    pass
                    
        except Exception as e:
            print(f"Erreur lors du nettoyage: {e}")


def main():
    """Point d'entrée principal"""
    # Chemins relatifs au script
    script_dir = Path(__file__).parent.parent
    presentation_path = script_dir / "DVaaS" / "DVaaS.pptx"
    audio_folder = script_dir / "DVaaS" / "scripts"
    
    print("=== PowerPoint Presenter avec Audio ===")
    print(f"Présentation: {presentation_path}")
    print(f"Dossier audio: {audio_folder}")
    
    # Vérifications
    if not presentation_path.exists():
        print(f"ERREUR: Présentation non trouvée: {presentation_path}")
        return
    
    if not audio_folder.exists():
        print(f"ERREUR: Dossier audio non trouvé: {audio_folder}")
        return
    
    # Créer et lancer le présentateur
    presenter = PowerPointPresenter(presentation_path, audio_folder)
    presenter.run_presentation()


if __name__ == "__main__":
    main()