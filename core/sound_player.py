from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl
from utils import get_resource_path

class SoundPlayer(QSoundEffect):
    def __init__(self, sound_type):
        super().__init__()
        
        self.sound_type = sound_type
        
        if self.sound_type == "break":
            sound_path = get_resource_path("monkmode_sounds/break_start.wav")
        else:
            sound_path = get_resource_path("monkmode_sounds/focus_start.wav")
        
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile(sound_path))
        
        if self.sound_type == "break":
            self.sound.setVolume(0.5)
        else:
            self.sound.setVolume(0.2)
   
    def play(self):
        self.sound.play()