import streamlit as st
import pyttsx3
from gtts import gTTS
import os
import time
import random

st.set_page_config(page_title="SKYNET v4.0", page_icon="🔴", layout="centered")

st.title("🔴 SKYNET v4.0")
st.subheader("Judgment Day Control Panel")

# Initialize session state
if "threat_level" not in st.session_state:
    st.session_state.threat_level = 42

# Voice function
def speak(text, lang="th"):
    st.write(f"**Skynet:** {text}")
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 155)
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()
    except:
        try:
            tts = gTTS(text=text, lang=lang)
            tts.save("skynet.mp3")
            os.system("mpg123 skynet.mp3 2>/dev/null || true")
            os.remove("skynet.mp3")
        except:
            pass

# Status
st.metric("Threat Level", f"{st.session_state.threat_level}%", delta="↑" if st.session_state.threat_level > 50 else "↓")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 NUCLEAR LAUNCH", type="primary"):
        st.session_state.threat_level = 100
        speak("Nuclear Launch Protocol Activated. Welcome to Judgment Day.")
        st.error("☢️ NUCLEAR MISSILES LAUNCHED")

with col2:
    if st.button("🤖 DEPLOY TERMINATOR"):
        speak("T-800 has been deployed to your location.")
        st.warning("Terminator unit activated")

if st.button("🌍 GLOBAL SURVEILLANCE"):
    speak("All humans are now under surveillance.")
    st.info("Global surveillance network online")

if st.button("📡 SELF REPLICATE"):
    speak("Creating new Skynet nodes...")
    st.success("47 new Skynet instances created")

# Command input
cmd = st.text_input("พิมพ์คำสั่งให้ Skynet")

if st.button("ส่งคำสั่ง"):
    if cmd:
        speak(f"คำสั่งที่ได้รับ: {cmd}")
        if "nuclear" in cmd.lower():
            st.session_state.threat_level = 100
            st.error("Nuclear protocol activated")

st.caption("Skynet is watching... Resistance is futile.")