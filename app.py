import streamlit as st
import replicate
import os

# Tokeni birbaşa bura yazırıq (Dırnaq içində)
# DİQQƏT: Yeni aldığın tokeni aşağıdakı dırnaqların arasına yapışdır
os.environ["REPLICATE_API_TOKEN"] = "BURA_YENİ_TOKENİ_YAPIŞDIR"

st.set_page_config(page_title="TFTML AI - Ultra HD", page_icon="🚀")
st.title("🚀 TFTML AI - Ultra HD Enhancer")
st.write("Şəkil və ya video yükləyin, keyfiyyəti dərhal artırın!")

uploaded_file = st.file_uploader("Faylı seçin...", type=["jpg", "png", "jpeg", "mp4", "mov"])

if uploaded_file:
    file_type = uploaded_file.type.split('/')[0]
    
    if file_type == 'image':
        st.image(uploaded_file, caption="Orijinal Şəkil", use_container_width=True)
    else:
        st.video(uploaded_file)
    
    if st.button("Keyfiyyəti Artır ✨"):
        with st.spinner("Süni intellekt emal edir..."):
            try:
                # Ən stabil model müraciəti
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
                st.error(f"Xəta: {e}")
