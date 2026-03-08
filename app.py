import streamlit as st
import replicate
import os

# Secrets-dən tokeni təhlükəsiz oxuyuruq
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
        with st.spinner("Süni intellekt (ScuNet) işləyir..."):
            try:
                # 422 xətasından qaçmaq üçün ən stabil ScuNet modeli
                output = replicate.run(
                    "cszn/scunet:64f33cc865773173da252033605a9144a1e941f1ca9cc16b714f3b7f637f6a79",
                    input={
                        "image": uploaded_file
                    }
                )
                
                if output:
                    st.image(output, caption="TFTML AI 4K Nəticə", use_container_width=True)
                    st.success("Uğurla tamamlandı!")
                    st.markdown(f"### [📥 Şəkli Yüklə]({output})")
            except Exception as e:
                st.error(f"Xəta baş verdi: {e}")
                
