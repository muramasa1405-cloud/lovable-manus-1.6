import streamlit as st
import requests

st.title("Lovable Manus - AI Assistant")

st.write("Welcome to the app!")

# Example call to FastAPI backend
if st.button("Test Backend"):
    try:
        response = requests.get("http://127.0.0.1:8000")  # Change to actual backend URL later
        st.write(response.text)
    except:
        st.error("Backend not reachable. For Streamlit Cloud, deploy backend separately.")

st.info("Note: For full functionality on Streamlit Cloud, the FastAPI backend should be hosted separately (e.g., on Render, Railway, or Fly.io).")