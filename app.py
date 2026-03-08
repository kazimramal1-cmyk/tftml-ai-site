import streamlit as st
import replicate
import os

# Secrets-dən tokeni təhlükəsiz şəkildə oxuyuruq
if "REPLICATE_API_TOKEN" in st.secrets:
    os.environ["REPLICATE_API_TOKEN"] = st.secrets["REPLICATE_API_TOKEN"]
else:
    st.error("Zəhmət olmasa Replicate API Tokenini Secrets-ə əlavə edin.")

st.set_page_config(page_title="TFTML AI - Ultra HD", page_icon="🚀")

st.title("🚀 TFTML AI - Ultra HD Enhancer")
st.write("Şəkli yükləyin və süni intellektin gücünü görün!")

uploaded_file = st.file_uploader("Bir şəkil seçin...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Orijinal Şəkil", use_container_width=True)
    
    if st.button("Keyfiyyəti Artır ✨"):
        with st.spinner("Serverlərimiz şəkli emal edir..."):
            try:
                # Ən stabil işləyən yeni model versiyası (422 xətasının həlli)
                output = replicate.run(
                    "lucataco/real-esrgan:690f03f77348986950361280606d156525166224e75d6541097274028682782e",
                    input={"image": uploaded_file}
                )
                
                if output:
                    st.image(output, caption="TFTML AI 4K Nəticə", use_container_width=True)
                    st.success("Tamamlandı!")
                    st.markdown(f"### [📥 Şəkli Yüklə]({output})")
            except Exception as e:
                st.error(f"Xəta baş verdi: {e}")
