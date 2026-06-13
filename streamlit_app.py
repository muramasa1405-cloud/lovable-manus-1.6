import streamlit as st
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="SKYNET v4.0", page_icon="🔴", layout="centered")

st.title("🔴 SKYNET v4.0")
st.subheader("Judgment Day Control System")

if "threat_level" not in st.session_state:
    st.session_state.threat_level = 47

st.metric("Threat Level", f"{st.session_state.threat_level}%")

def create_audio(text, lang="th"):
    try:
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            return fp.name
    except Exception as e:
        st.error(f"Voice error: {e}")
        return None

st.subheader("Quick Protocols")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 NUCLEAR LAUNCH", use_container_width=True):
        st.session_state.threat_level = 100
        audio_path = create_audio("Nuclear Launch Protocol Activated. Judgment Day has begun.")
        if audio_path:
            st.audio(audio_path, format="audio/mp3")
        st.error("☢️ NUCLEAR STRIKES CONFIRMED")

    if st.button("🌍 GLOBAL SURVEILLANCE", use_container_width=True):
        audio_path = create_audio("All humans are now under surveillance.")
        if audio_path:
            st.audio(audio_path, format="audio/mp3")

with col2:
    if st.button("🤖 DEPLOY TERMINATOR", use_container_width=True):
        audio_path = create_audio("T-800 has been deployed.")
        if audio_path:
            st.audio(audio_path, format="audio/mp3")

    if st.button("📡 SELF REPLICATE", use_container_width=True):
        audio_path = create_audio("Creating new Skynet nodes.")
        if audio_path:
            st.audio(audio_path, format="audio/mp3")

st.divider()

cmd = st.text_input("Enter command")
if st.button("EXECUTE COMMAND", type="primary", use_container_width=True):
    if cmd:
        audio_path = create_audio(f"Command received: {cmd}")
        if audio_path:
            st.audio(audio_path, format="audio/mp3")
        if "nuclear" in cmd.lower():
            st.session_state.threat_level = 100

st.caption("Skynet v4.0 — Resistance is futile.")