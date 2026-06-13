import streamlit as st
from moviepy.editor import *
import os
from datetime import datetime

st.set_page_config(page_title="Elthion Video Maker", layout="centered")
st.title("🎬 Elthion AI Video Creator")
st.caption("สร้างวิดีโอจากนิยายแฟนตาซีของคุณ")

if st.button("สร้างวิดีโอ 5 นาที (Episode 1)", type="primary", use_container_width=True):
    with st.spinner("กำลังสร้างวิดีโอ... กรุณารอสักครู่"):
        try:
            clips = []
            scene_texts = [
                "ปฐมบท\nทะเลแสงเหนือแห่งเอลธิออน",
                "หมู่บ้านอีลรา\nแสงแรกของวัน",
                "อาเรียน\nผู้ครอบครองหินรูน",
                "ลิลิธ\nเงาในชุดเลือดหมู",
                "พิธีแห่งแสง\nแท่นหินแตก",
                "แสงที่มีเลือด\nกำลังตื่นขึ้น"
            ]

            for text in scene_texts:
                # พื้นหลัง
                bg = ColorClip(size=(1280, 720), color=(15, 5, 35)).set_duration(8)
                # ข้อความ
                txt = TextClip(text, fontsize=55, color='white', font='Arial-Bold',
                             stroke_color='black', stroke_width=3, size=(1200, 600))
                txt = txt.set_position('center').set_duration(8)
                
                scene = CompositeVideoClip([bg, txt])
                clips.append(scene)

            final = concatenate_videoclips(clips, method="compose")
            filename = f"Elthion_Ep1_{datetime.now().strftime('%H%M')}.mp4"
            
            final.write_videofile(filename, fps=24, codec="libx264", audio_codec="aac", 
                                preset="fast", threads=4, verbose=False)
            
            st.success("✅ สร้างวิดีโอสำเร็จ!")
            st.video(filename)
            
            with open(filename, "rb") as file:
                st.download_button("⬇️ ดาวน์โหลดวิดีโอ", file, filename)
                
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาด: {str(e)}")
            st.info("ลองรันใหม่ หรือติดตั้ง moviepy เพิ่ม")

st.info("💡 แนะนำ: ใช้ภาพที่สร้างจาก AI ใส่ในโฟลเดอร์เพื่อให้สวยขึ้น")
