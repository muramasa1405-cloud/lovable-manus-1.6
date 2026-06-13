import streamlit as st
from moviepy.editor import *
import os
from datetime import datetime

st.set_page_config(page_title="Elthion AI Video Creator", layout="centered")
st.title("🎥 Elthion AI Video Generator")
st.subheader("สร้างวิดีโอจากนิยายของคุณ")

# ตั้งค่าความยาว
minutes = st.slider("ความยาววิดีโอ (นาที)", 3, 10, 5)

if st.button("🚀 สร้างวิดีโอ Episode 1", type="primary"):
    with st.spinner("กำลังสร้างวิดีโอ... อาจใช้เวลา 1-3 นาที"):
        try:
            # สร้างคลิปง่าย ๆ
            clips = []
            texts = [
                "ปฐมบท\nทะเลแสงเหนือแห่งเอลธิออน",
                "อาเรียน\nเด็กหนุ่มผู้ครอบครองหินรูน",
                "เสียงจากโลกที่ไม่มีใครเคยได้ยิน",
                "ลิลิธ\nเงาในชุดเลือดหมู",
                "พิธีแห่งแสง\nแท่นหินแตก",
                "แสงของเจ้า... ได้เลือดแล้ว"
            ]
            
            for text in texts:
                txt_clip = TextClip(text, fontsize=60, color='white', font='Arial-Bold', 
                                  stroke_color='black', stroke_width=3, size=(1280, 720))
                bg = ColorClip(size=(1280, 720), color=(10, 5, 30)).set_duration(8)
                scene = CompositeVideoClip([bg, txt_clip.set_position('center')]).set_duration(8)
                clips.append(scene)
            
            final_video = concatenate_videoclips(clips, method="compose")
            filename = f"Elthion_Episode_1_{datetime.now().strftime('%H%M')}.mp4"
            final_video.write_videofile(filename, fps=24, codec="libx264", audio_codec="aac")
            
            st.success(f"✅ สร้างสำเร็จ! ไฟล์: {filename}")
            st.video(filename)
            
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาด: {e}")

st.info("💡 วิธีใช้งาน: วางภาพที่สร้างจาก AI ลงในโฟลเดอร์ แล้วพัฒนาแอปนี้ต่อได้")
