import streamlit as st
import requests
import os
from typing import Optional

st.set_page_config(page_title="Lovable Manus 1.6", layout="wide")
st.title("🦾 Lovable Manus 1.6")
st.subheader("True Multi-Agent App Generator")

st.markdown("---")

col1, col2 = st.columns([3,1])

with col1:
    prompt = st.text_area(
        "Describe the app you want to build (ภาษาไทยได้)",
        height=200,
        placeholder="สร้างเว็บแอพ Todo List ด้วย Next.js + Tailwind + Supabase..."
    )

with col2:
    model = st.selectbox(
        "เลือก Model",
        ["gpt-4o-mini", "gpt-4o", "claude-3-5-sonnet"],
        index=0
    )

if st.button("🚀 Generate App", type="primary", use_container_width=True):
    if not prompt.strip():
        st.error("กรุณาใส่ prompt")
    else:
        with st.spinner("กำลังรัน Multi-Agent System... (อาจใช้เวลา 30-90 วินาที)"):
            try:
                # Call backend (change URL if you deploy backend separately)
                backend_url = os.getenv("BACKEND_URL", "http://localhost:8000")
                response = requests.post(
                    f"{backend_url}/generate",
                    json={"prompt": prompt, "model": model},
                    timeout=180
                )
                
                if response.status_code == 200:
                    data = response.json()
                    if data.get("success"):
                        st.success("✅ Generation Complete!")
                        st.json(data.get("result", {}))
                    else:
                        st.error(data.get("message", "Unknown error"))
                else:
                    st.error(f"Backend error: {response.text}")
            except Exception as e:
                st.error(f"Connection error: {str(e)}")
                st.info("💡 Hint: Deploy backend separately on Railway/Render and set BACKEND_URL")

st.markdown("---")
st.caption("Backend: FastAPI + Multi-Agent (LangGraph stub) | Frontend: Streamlit")
