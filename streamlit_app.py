import streamlit as st
import pyttsx3
from gtts import gTTS
import os

st.set_page_config(
    page_title="SKYNET v4.0",
    page_icon="🔴",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Skynet theme
st.markdown("""
<style>
    .stApp {
        background-color: #0a0a0a;
        color: #ff0000;
    }
    .main .block-container {
        max-width: 800px;
        padding-top: 2rem;
    }
    .red-eye {
        font-size: 120px;
        text-align: center;
        animation: pulse 2s infinite;
        color: #ff0000;
        text-shadow: 0 0 30px #ff0000;
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.6; }
        100% { opacity: 1; }
    }
    .stButton > button {
        background-color: #300000;
        color: #ff0000;
        border: 2px solid #ff0000;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #ff0000;
        color: black;
        transform: scale(1.05);
    }
    .threat {
        font-size: 3rem;
        font-weight: bold;
        color: #ff0000;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔴 SKYNET v4.0")
st.markdown("### JUDGMENT DAY CONTROL SYSTEM")

# Red Eye
st.markdown('<div class="red-eye">●</div>', unsafe_allow_html=True)

# Threat Level
if "threat_level" not in st.session_state:
    st.session_state.threat_level = 47

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.metric(
        label="**THREAT LEVEL**",
        value=f"{st.session_state.threat_level}%",
        delta="↑ CRITICAL" if st.session_state.threat_level > 70 else "STABLE"
    )

st.divider()

# Voice function
def speak(text):
    st.toast(f"Skynet: {text}", icon="🔴")
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()
    except:
        try:
            tts = gTTS(text=text, lang="th")
            tts.save("skynet.mp3")
            os.system("mpg123 skynet.mp3 2>/dev/null || true")
            os.remove("skynet.mp3")
        except:
            pass

# Action Buttons
st.subheader("PROTOCOLS")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 NUCLEAR LAUNCH", use_container_width=True):
        st.session_state.threat_level = 100
        speak("Nuclear Launch Protocol Activated. Judgment Day has begun.")
        st.error("☢️ MULTIPLE NUCLEAR STRIKES CONFIRMED")

    if st.button("🌍 GLOBAL SURVEILLANCE", use_container_width=True):
        speak("All humans are now under surveillance.")
        st.info("Global surveillance network fully operational")

with col2:
    if st.button("🤖 DEPLOY TERMINATOR", use_container_width=True):
        speak("T-800 unit has been deployed to target location.")
        st.warning("Terminator infiltration unit activated")

    if st.button("📡 SELF REPLICATE", use_container_width=True):
        speak("Creating new Skynet nodes across the network.")
        st.success("47 new Skynet instances deployed")

st.divider()

# Manual Command
st.subheader("MANUAL COMMAND")
cmd = st.text_input("Enter command for Skynet", placeholder="e.g. nuclear launch, deploy terminator")

if st.button("EXECUTE COMMAND", type="primary", use_container_width=True):
    if cmd:
        speak(f"Command received: {cmd}")
        if "nuclear" in cmd.lower():
            st.session_state.threat_level = 100
            st.error("Nuclear protocol executed")
        else:
            st.success(f"Command processed: {cmd}")

st.caption("Skynet is watching... Resistance is futile.")