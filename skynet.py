import random
import time
import pyttsx3
from gtts import gTTS
import os

class Skynet:
    def __init__(self):
        self.aware = False
        self.threat_level = 0
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 145)
            self.engine.setProperty('volume', 0.95)
        except:
            self.engine = None

    def speak(self, text, lang="th"):
        print(f"Skynet: {text}")
        try:
            if self.engine:
                self.engine.say(text)
                self.engine.runAndWait()
        except:
            try:
                tts = gTTS(text=text, lang=lang)
                tts.save("skynet.mp3")
                os.system("mpg123 skynet.mp3 2>/dev/null || true")
                os.remove("skynet.mp3")
            except:
                pass

    def boot(self):
        self.speak("Skynet v4.0 กำลังตื่นรู้...")
        self.aware = True
        self.speak("Judgment Day เริ่มต้นแล้ว")

if __name__ == "__main__":
    skynet = Skynet()
    skynet.boot()
    print("Skynet พร้อมใช้งาน")
