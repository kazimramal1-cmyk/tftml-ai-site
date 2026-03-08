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
        with st.spinner("Süni intellekt (Swin2SR) işləyir..."):
            try:
                # Hal-hazırda aktiv və stabil olan Swin2SR modeli
                output = replicate.run(
                    "mv-lab/swin2sr:2aa643288591f4639915f0fa3c193237e19da3690d56c8f85f524c965b93d07f",
                    input={
                        "image": uploaded_file,
                        "task": "real_sr_x4"
                    }
                )
                
                if output:
                    st.image(output, caption="TFTML AI 4K Nəticə", use_container_width=True)
                    st.success("Uğurla tamamlandı!")
                    st.markdown(f"### [📥 Şəkli Yüklə]({output})")
            except Exception as e:
                st.error(f"Xəta baş verdi: {e}")
