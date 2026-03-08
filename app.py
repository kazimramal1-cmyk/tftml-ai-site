import streamlit as st
import replicate
import os

# 1. Secrets-dən tokeni təhlükəsiz oxuyuruq
if "REPLICATE_API_TOKEN" in st.secrets:
    os.environ["REPLICATE_API_TOKEN"] = st.secrets["REPLICATE_API_TOKEN"]
else:
    st.error("Zəhmət olmasa Replicate API Tokenini Secrets-ə əlavə edin.")

# 2. Səhifə nizamlamaları
st.set_page_config(page_title="TFTML AI - Ultra HD", page_icon="🚀")
st.title("🚀 TFTML AI - Ultra HD Enhancer")
st.write("Şəkil və ya qısa video yükləyin, süni intellekt keyfiyyəti artırsın!")

# 3. Fayl yükləmə bölməsi
uploaded_file = st.file_uploader("Faylı seçin...", type=["jpg", "png", "jpeg", "mp4", "mov"])

if uploaded_file:
    # Faylın növünü yoxlayırıq (Şəkil və ya Video)
    file_type = uploaded_file.type.split('/')[0]
    
    if file_type == 'image':
        st.image(uploaded_file, caption="Orijinal Şəkil", use_container_width=True)
    else:
        st.video(uploaded_file)
    
    # 4. Emal düyməsi
    if st.button("Keyfiyyəti Artır ✨"):
        with st.spinner("Süni intellekt emal edir (bu bir az vaxt ala bilər)..."):
            try:
                # 422 xətasını həll etmək üçün versiya ID-si olmadan birbaşa model adını yazırıq
                # Bu, Replicate-in avtomatik ən son stabil versiyanı seçməsini təmin edir
                output = replicate.run(
                    "nightmareai/real-esrgan",
                    input={
                        "image": uploaded_file,
                        "upscale": 2,
                        "face_enhance": True
                    }
                )
                
                if output:
                    if file_type == 'image':
                        st.image(output, caption="TFTML AI Nəticəsi", use_container_width=True)
                    else:
                        st.video(output)
                        
                    st.success("Uğurla tamamlandı!")
                    st.markdown(f"### [📥 Nəticəni Yüklə]({output})")
                    
            except Exception as e:
                # Əgər hələ də 422 xətası gəlirsə, bu Replicate limitinin bitməsidir
                st.error(f"Texniki problem baş verdi: {e}")
                st.info("Qeyd: Əgər '422' xətası görürsünüzsə, Replicate pulsuz limitiniz bitmiş ola bilər.")
