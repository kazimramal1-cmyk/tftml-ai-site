import streamlit as st
import replicate
import os

# Secrets-dən tokeni oxuyuruq
if "REPLICATE_API_TOKEN" in st.secrets:
    os.environ["REPLICATE_API_TOKEN"] = st.secrets["REPLICATE_API_TOKEN"]
else:
    st.error("API Token tapılmadı. Secrets hissəsini yoxlayın.")

st.set_page_config(page_title="TFTML AI - Ultra HD", page_icon="🚀")

st.title("🚀 TFTML AI - Ultra HD Enhancer")
st.write("Şəkli yükləyin və süni intellektlə keyfiyyəti artırın.")

uploaded_file = st.file_uploader("Şəkil seçin...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Orijinal Şəkil", use_container_width=True)
    
    if st.button("Keyfiyyəti Artır ✨"):
        with st.spinner("Süni intellekt emal edir..."):
            try:
                # BU SƏTİR 422 XƏTASINI DÜZƏLDİR:
                # Real-ESRGAN-ın ən stabil və aktiv versiyası budur:
                model_id = "nightmareai/real-esrgan:42fed1c4974141d04715c6970bb2c1125604b2c380f9abc094b6d53153406f2e"
                
                output = replicate.run(
                    model_id,
                    input={
                        "image": uploaded_file,
                        "upscale": 2,
                        "face_enhance": True
                    }
                )
                
                if output:
                    st.image(output, caption="TFTML AI Nəticəsi", use_container_width=True)
                    st.success("Hazırdır!")
                    st.markdown(f"### [📥 Şəkli Yüklə]({output})")
            except Exception as e:
                st.error(f"Texniki problem: {e}")
