import streamlit as st
import requests
import os

st.set_page_config(page_title="Lovable Manus", layout="wide")
st.title("🤖 Lovable Manus 1.6")
st.markdown("### AI Assistant with FastAPI Backend")

# Configuration
BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.sidebar.info(f"Backend: {BASE_URL}")

# Test connection
if st.button("🔍 Test Backend Connection"):
    try:
        r = requests.get(f"{BASE_URL}/health", timeout=5)
        if r.status_code == 200:
            st.success("✅ Backend is running!")
            st.json(r.json())
        else:
            st.warning(f"Backend responded with status {r.status_code}")
    except Exception as e:
        st.error(f"Cannot connect to backend: {str(e)}")
        st.info("💡 Tip: Deploy your FastAPI backend separately and set BACKEND_URL in Streamlit Secrets.")

st.divider()

st.subheader("Chat Interface")
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("พิมพ์ข้อความที่นี่..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        r = requests.post(f"{BASE_URL}/chat", json={"message": prompt}, timeout=30)
        if r.status_code == 200:
            reply = r.json().get("reply", "No response")
            st.session_state.messages.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.markdown(reply)
        else:
            st.error("Backend error")
    except:
        st.error("Cannot reach backend. Please deploy backend separately.")

st.caption("Streamlit Cloud Frontend - Backend ต้อง deploy แยก")