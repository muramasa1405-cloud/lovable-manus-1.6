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
            # ปรับแต่งเสียงให้ดีขึ้น
            self.engine.setProperty('rate', 155)          # ความเร็วในการพูด (ยิ่ง 120-200)
            self.engine.setProperty('volume', 1.0)        # เสียงดัง (สูงสุด 1.0)
            
            # พยายามเลือก voice ที่ดีที่สุด (Linux มักใช้ espeak)
            voices = self.engine.getProperty('voices')
            for voice in voices:
                if 'thai' in voice.name.lower() or 'th' in voice.id.lower():
                    self.engine.setProperty('voice', voice.id)
                    break
        except Exception as e:
            print(f"Voice init error: {e}")
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
