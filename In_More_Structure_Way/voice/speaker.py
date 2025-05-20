import os
from gtts import gTTS
import pygame
import pyttsx3

# Optional: fallback engine
engine = pyttsx3.init()

def speak(text: str, use_gtts=True):
    if use_gtts:
        temp_path = os.path.join(os.getcwd(),"2","voice","temp_jarvis.mp3")
        tts = gTTS(text)
        tts.save(temp_path)

        pygame.mixer.init()
        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
        os.remove(temp_path)
    else:
        engine.say(text)
        engine.runAndWait()
