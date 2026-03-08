import streamlit as st
import replicate
import os

# Secrets-dən tokeni oxuyuruq
try:
    replicate_api_token = st.secrets["REPLICATE_API_TOKEN"]
    os.environ["REPLICATE_API_TOKEN"] = replicate_api_token
except Exception:
    st.error("API Token tapılmadı. Settings -> Secrets hissəsinə əlavə edin.")

st.set_page_config(page_title="TFTML AI - Ultra HD", page_icon="🚀")

st.title("🚀 TFTML AI - Ultra HD Enhancer")
st.write("Şəkli yükləyin və 4K nəticəni görün!")

uploaded_file = st.file_uploader("Şəkil seçin...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Orijinal Şəkil", use_container_width=True)
    
    if st.button("Keyfiyyəti Artır ✨"):
        with st.spinner("Süni intellekt işləyir..."):
            try:
                # Modeli işə salırıq
                output = replicate.run(
                    "nightmareai/real-esrgan:42fed1c4974141d04715c6970bb2c1125604b2c380f9abc094b6d53153406f2e",
                    input={"image": uploaded_file}
                )
                
                # Nəticəni göstəririk (Mötərizələr bərpa olundu)
                st.image(output, caption="TFTML AI Nəticəsi", use_container_width=True)
                st.success("Hazırdır!")
                st.markdown(f"[Şəkli Yüklə]({output})")
                
            except Exception as e:
                st.error(f"Xəta: {e}")
