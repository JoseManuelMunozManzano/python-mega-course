# Paquete Pillow ya instalado al instalar streamlit
from PIL import Image


def convert_image(image):
    # Crear una instancia de Image Pillow
    img = Image.open(image)
    # Convertir la imagen pillow a escala de grises
    return img.convert("L")
