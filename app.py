import streamlit as st
import replicate
import os

# Professional yanaşma: Tokeni birbaşa koda yazmırıq, Streamlit Secrets-dən oxuyuruq
try:
    replicate_api_token = st.secrets["REPLICATE_API_TOKEN"]
    os.environ["REPLICATE_API_TOKEN"] = replicate_api_token
except Exception:
    st.error("Xəta: API Token tapılmadı. Zəhmət olmasa Streamlit Secrets hissəsinə tokeni əlavə edin.")

# Saytın təmiz və professional dizaynı
st.set_page_config(page_title="TFTML AI - Ultra HD", page_icon="🚀", layout="centered")

st.title("🚀 TFTML AI - Ultra HD Enhancer")
st.markdown("---")
st.write("Bulanıq şəkli yükləyin və süni intellekt vasitəsilə 1 saniyədə 4K keyfiyyətini görün.")

# Şəkil yükləmə bölməsi
uploaded_file = st.file_uploader("Şəkil seçin (JPG, PNG, JPEG)...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Orijinal şəkli göstər
    st.image(uploaded_file, caption="Orijinal Şəkil", use_container_width=True)
    
    if st.button("Keyfiyyəti Artır ✨"):
        with st.spinner("Bulud GPU serverləri işləyir..."):
            try:
                # Replicate serverlərində Real-ESRGAN modelini işə salırıq
                output = replicate.run(
                    "nightmareai/real-esrgan:42fed1c4974141d04715c6970bb2c1125604b2c380f9abc094b6d53153406f2e",
                    input={"image": uploaded_file}
                )
                
                # Nəticəni göstər
                st.markdown("### ✨ 4K Nəticə")
                st.image(output, caption="TFTML AI tərəfindən bərpa olundu", use_
