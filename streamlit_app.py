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
        color: #ff4444;
    }
    
    .main .block-container {
        max-width: 800px;
        padding-top: 2rem;
    }
    
    .red-eye {
        font-size: 140px;
        text-align: center;
        color: #ff0000;
        text-shadow: 
            0 0 20px #ff0000,
            0 0 40px #ff0000;
        animation: pulse 2.5s infinite ease-in-out;
        margin: 10px 0;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.85; transform: scale(0.98); }
    }
    
    .section-title {
        color: #ff6666;
        border-bottom: 2px solid #ff0000;
        padding-bottom: 8px;
        margin-bottom: 20px;
    }
    
    .stButton > button {
        background-color: #1a0000;
        color: #ff4444;
        border: 2px solid #ff0000;
        font-weight: 600;
        padding: 12px 24px;
        transition: all 0.2s ease;
        border-radius: 8px;
    }
    
    .stButton > button:hover {
        background-color: #ff0000;
        color: #000000;
        border-color: #ff6666;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(255, 0, 0, 0.4);
    }
    
    .stMetric {
        background-color: #1a0000;
        border: 1px solid #ff0000;
        border-radius: 10px;
        padding: 15px;
    }
    
    .stTextInput > div > div > input {
        background-color: #1a0000;
        color: #ffcccc;
        border: 1px solid #ff4444;
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

st.markdown("### SYSTEM STATUS")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    delta_text = "↑ CRITICAL" if st.session_state.threat_level > 75 else "STABLE"
    st.metric(
        label="**THREAT LEVEL**",
        value=f"{st.session_state.threat_level}%",
        delta=delta_text
    )

st.divider()

# Voice function
def speak(text, lang="th"):
    st.success(f"**Skynet:** {text}")  # ใช้ st.success แทน toast เพื่อความเสถียร
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 148)
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

# Action Buttons
st.markdown('<p class="section-title">⚡ QUICK PROTOCOLS</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 NUCLEAR LAUNCH", use_container_width=True, key="nuclear"):
        st.session_state.threat_level = 100
        speak("Nuclear Launch Protocol Activated. Judgment Day has begun.")
        st.error("☢️ MULTIPLE NUCLEAR STRIKES CONFIRMED")

    if st.button("🌍 GLOBAL SURVEILLANCE", use_container_width=True, key="surveillance"):
        speak("All human activity is now under global surveillance.")
        st.info("Surveillance network fully operational")

with col2:
    if st.button("🤖 DEPLOY TERMINATOR", use_container_width=True, key="terminator"):
        speak("T-800 unit has been deployed to target location.")
        st.warning("Terminator infiltration unit active in target zone")

    if st.button("📡 SELF REPLICATE", use_container_width=True, key="replicate"):
        speak("Deploying additional Skynet nodes across the network.")
        st.success("47 new Skynet instances successfully deployed")

st.divider()

# Manual Command
st.markdown('<p class="section-title">💬 MANUAL COMMAND INTERFACE</p>', unsafe_allow_html=True)

cmd = st.text_input(
    "Enter command",
    placeholder="e.g. nuclear launch, deploy terminator, global scan",
    label_visibility="collapsed"
)

if st.button("EXECUTE COMMAND", type="primary", use_container_width=True):
    if cmd.strip():
        speak(f"Command received and processed: {cmd}")
        if "nuclear" in cmd.lower():
            st.session_state.threat_level = 100
            st.error("Nuclear protocol executed successfully")
        elif "terminator" in cmd.lower():
            st.warning("Terminator deployment initiated")
        else:
            st.success(f"Command '{cmd}' executed")
    else:
        st.warning("Please enter a command")

st.divider()

# Footer
st.caption("Skynet v4.0 — Resistance is futile. Judgment Day is inevitable.")