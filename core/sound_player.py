from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl
import os

class SoundPlayer(QSoundEffect):
    def __init__(self, sound_type):
        self.sound_type = sound_type
        base_path = os.path.dirname(os.path.abspath(__file__))
        if self.sound_type == "break":
            sound_path = os.path.join(base_path, "..","monkmode_sounds", "break_start.wav")
        else:
            sound_path = os.path.join(base_path, "..","monkmode_sounds", "focus_start.wav")

        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile(os.path.abspath(sound_path)))
        if self.sound_type == "break":
            self.sound.setVolume(0.5)
        else:
            self.sound.setVolume(0.2)
    

    def play(self):
        self.sound.play()