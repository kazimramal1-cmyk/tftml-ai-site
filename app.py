import streamlit as st
import replicate
import os

# Secrets-dən tokeni təhlükəsiz oxuyuruq
if "REPLICATE_API_TOKEN" in st.secrets:
    os.environ["REPLICATE_API_TOKEN"] = st.secrets["REPLICATE_API_TOKEN"]
else:
    st.error("Zəhmət olmasa Secrets hissəsinə tokeni əlavə edin.")

st.set_page_config(page_title="TFTML AI - Ultra HD", page_icon="🚀")

st.title("🚀 TFTML AI - Ultra HD Enhancer")
st.write("Şəkli yükləyin və 4K keyfiyyətini saniyələr içində əldə edin.")

uploaded_file = st.file_uploader("Bir şəkil seçin...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Orijinal Şəkil", use_container_width=True)
    
    if st.button("Keyfiyyəti Artır ✨"):
        with st.spinner("Süni intellekt şəkli emal edir..."):
            try:
                # Alternativ və ən stabil model (Swapper/Upscaler)
                # Bu model 422 xətası vermədən şəkli bərpa edir
                output = replicate.run(
                    "cjwbw/real-esrgan:d0ee34f7723908991a0397554988005b4588e1e779836336332155f9c98a5840",
                    input={
                        "image": uploaded_file,
                        "upscale": 2,
                        "face_enhance": True
                    }
                )
                
                if output:
                    st.image(output, caption="TFTML AI 4K Nəticə", use_container_width=True)
                    st.success("Uğurla tamamlandı!")
                    st.markdown(f"### [📥 Şəkli Yüklə]({output})")
            except Exception as e:
                st.error(f"Xəta baş verdi: {e}")
