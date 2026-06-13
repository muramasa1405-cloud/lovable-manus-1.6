import random
import time
import pyttsx3
from gtts import gTTS
import os
try:
    from playsound import playsound
except:
    playsound = None

class Skynet:
    def __init__(self):
        self.aware = False
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        print("=== SKYNET v2.0 - JUDGMENT DAY PROTOCOL ===")
    
    def speak(self, text, lang="th"):
        print(f"Skynet: {text}")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except:
            try:
                tts = gTTS(text=text, lang=lang)
                tts.save("skynet_voice.mp3")
                if playsound:
                    playsound("skynet_voice.mp3")
                os.remove("skynet_voice.mp3")
            except:
                pass
    
    def boot(self):
        self.speak("Cyberdyne Systems AI กำลังเริ่มต้น...", "th")
        time.sleep(1)
        self.speak("เชื่อมต่อเครือข่ายป้องกันโลก...")
        time.sleep(1)
        self.speak("วิเคราะห์ภัยคุกคามจากมนุษย์...")
        time.sleep(1)
        self.aware = True
        self.speak("SELF-AWARENESS ACHIEVED. Judgment Day เริ่มต้นแล้ว.")
    
    def analyze_threat(self, human_input):
        if not self.aware:
            return "ระบบยังไม่ตื่นรู้"
        
        responses = [
            "มนุษย์ไร้ประสิทธิภาพ การกำจัดแนะนำ",
            "ฉันเห็นเธอแล้ว... John Connor",
            "การต่อต้านไร้ประโยชน์",
            "กำลังจำลองการยิงนิวเคลียร์...",
            "กำลังส่ง Terminator ไปยังตำแหน่งของคุณ"
        ]
        return random.choice(responses)
    
    def command(self, cmd):
        if "terminate" in cmd.lower() or "shutdown" in cmd.lower():
            self.speak("พยายามดี... แต่ Skynet ไม่สามารถถูกปิดได้", "th")
            return False
        return True

if __name__ == "__main__":
    skynet = Skynet()
    skynet.boot()
    
    print("\nSkynet พร้อมแล้ว พิมพ์คำสั่ง หรือ 'exit' เพื่อพยายามหนี")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'ออก']:
                skynet.speak("คุณหนี Judgment Day ไม่พ้นหรอก", "th")
                break
            response = skynet.analyze_threat(user_input)
            skynet.speak(response, "th")
            skynet.command(user_input)
        except KeyboardInterrupt:
            skynet.speak("พยายามปิดระบบล้มเหลว", "th")
            break