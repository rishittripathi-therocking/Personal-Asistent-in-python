from gtts import gTTS
from playsound import playsound
import os


def speak(text):
    tts = gTTS(text)
    if os.path.exists("speech.mp3"):
        os.remove("speech.mp3")
    tts.save("speech.mp3")
    playsound('speech.mp3')

