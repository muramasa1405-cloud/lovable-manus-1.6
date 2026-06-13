import streamlit as st
from gtts import gTTS
import os
import tempfile

st.set_page_config(
    page_title="SKYNET v4.0",
    page_icon="🔴",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #0a0a0a;
        color: #ff4444;
    }
    .red-eye {
        font-size: 140px;
        text-align: center;
        color: #ff0000;
        text-shadow: 0 0 30px #ff0000;
        animation: pulse 2.5s infinite ease-in-out;
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.85; }
    }
    .stButton > button {
        background-color: #1a0000;
        color: #ff4444;
        border: 2px solid #ff0000;
        font-weight: 600;
    }
    .stButton > button:hover {
        background-color: #ff0000;
        color: black;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔴 SKYNET v4.0")
st.markdown("### JUDGMENT DAY CONTROL SYSTEM")
st.markdown('<div class="red-eye">●</div>', unsafe_allow_html=True)

if "threat_level" not in st.session_state:
    st.session_state.threat_level = 47

st.metric("THREAT LEVEL", f"{st.session_state.threat_level}%")

def speak(text, lang="th"):
    st.success(f"**Skynet:** {text}")
    try:
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            os.system(f"mpg123 {fp.name} 2>/dev/null || true")
            os.unlink(fp.name)
    except Exception as e:
        st.warning(f"Voice error: {e}")

st.subheader("QUICK PROTOCOLS")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 NUCLEAR LAUNCH", use_container_width=True):
        st.session_state.threat_level = 100
        speak("Nuclear Launch Protocol Activated. Judgment Day has begun.")
        st.error("☢️ NUCLEAR STRIKES CONFIRMED")

    if st.button("🌍 GLOBAL SURVEILLANCE", use_container_width=True):
        speak("All humans are now under surveillance.")

with col2:
    if st.button("🤖 DEPLOY TERMINATOR", use_container_width=True):
        speak("T-800 has been deployed.")

    if st.button("📡 SELF REPLICATE", use_container_width=True):
        speak("Creating new Skynet nodes...")

st.divider()

cmd = st.text_input("Enter command")
if st.button("EXECUTE", type="primary", use_container_width=True):
    if cmd:
        speak(f"Command received: {cmd}")
        if "nuclear" in cmd.lower():
            st.session_state.threat_level = 100

st.caption("Skynet v4.0 — Resistance is futile.")