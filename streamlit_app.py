import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Lovable Manus 1.6", layout="wide")
st.title("🧠 Lovable Manus 1.6")
st.markdown("**True Multi-Agent Architecture** | *Private & Secret Files Support in SystemBank*")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    model = st.selectbox(
        "เลือก Model",
        ["gpt-4o-mini", "gpt-4o", "claude-3-5-sonnet-latest"],
        index=0
    )
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    
    st.markdown("---")
    st.caption("ข้อดีของเรา: สามารถใส่ไฟล์ลับ/ไฟล์ส่วนตัวลงใน SystemBank ได้")

# Main area
tab1, tab2 = st.tabs(["Generate App", "SystemBank"])

with tab1:
    prompt = st.text_area(
        "อธิบายแอพที่ต้องการสร้าง (ภาษาไทยหรืออังกฤษก็ได้)",
        height=180,
        placeholder="สร้างเว็บ Todo List แบบ Fullstack ด้วย Next.js + Supabase + Authentication..."
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Generate Full App", type="primary", use_container_width=True):
            if not prompt.strip():
                st.error("กรุณาใส่ prompt")
            else:
                with st.spinner("Multi-Agent กำลังทำงาน... (Planning → Coding → Review + SystemBank)"):
                    try:
                        response = requests.post(
                            "http://127.0.0.1:8000/generate",
                            json={
                                "prompt": prompt,
                                "model": model,
                                "temperature": temperature,
                                "include_systembank": True
                            },
                            timeout=300
                        )
                        result = response.json()
                        
                        if result.get("success"):
                            st.success("✅ สร้างแอพสำเร็จ!")
                            st.subheader("📁 ไฟล์ที่สร้าง")
                            st.json(result.get("files", {}))
                            if result.get("systembank"):
                                st.info("🔐 SystemBank ถูกใช้งาน: " + result["systembank"].get("note", ""))
                        else:
                            st.error(result.get("error", "Unknown error"))
                    except Exception as e:
                        st.error(f"Connection error: {e}")
                        st.info("💡 Tip: Deploy backend แยกบน Railway หรือ Render")

with tab2:
    st.subheader("🔐 SystemBank (Private & Secret Files)")
    st.info("ใส่ไฟล์ลับของคุณที่นี่ เช่น API Keys, Private Components, Custom Patterns")
    
    uploaded_files = st.file_uploader(
        "อัพโหลดไฟล์ส่วนตัว/ลับ", 
        accept_multiple_files=True,
        type=['py', 'js', 'ts', 'json', 'env', 'md', 'txt']
    )
    
    if uploaded_files:
        for file in uploaded_files:
            st.success(f"✅ {file.name} ถูกเก็บใน SystemBank แล้ว (จะถูกส่งให้ Agent)")
    
    system_prompt = st.text_area("SystemBank Instructions (จะถูกใส่ให้ Agent ทุกตัว)", height=150, value="ใช้ไฟล์ลับจาก SystemBank อย่างปลอดภัย")

# Footer
st.markdown("---")
st.caption("Lovable Manus 1.6 — Like Lovable but **stronger on private/secret files & SystemBank**")