# Para ejecutar, desde el terminal: streamlit run bonus/bonus.py
import streamlit as st
from converter import convert_image

st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # Abrir la cámara
    camera_image = st.camera_input("Camera")

if camera_image:
    gray_camera_image = convert_image(camera_image)
    st.image(gray_camera_image)

if uploaded_image:
    gray_uploaded_image = convert_image(uploaded_image)
    st.image(gray_uploaded_image)
