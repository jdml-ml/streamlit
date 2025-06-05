import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt
from PyPDF2 import PdfReader

@st.cache_data
def cargar_imagen(image):
    img = Image.open(image)
    return img

def leer_pdf(file):
    pdfReader = PdfReader(file)
    count = len(pdfReader.pages)
    text = ""
    for i in range(count):
        pagina = pdfReader.pages[i]
        text += pagina.extract_text()
    return text

def main():
    st.title("Curso de Streamlit")
    menu = ["Imágenes", "Conjunto de datos", "Archivos de documentos"]
    eleccion = st.sidebar.selectbox("Menú", menu)
    if eleccion == "Imágenes":
        st.header("Imagen")
        archivo = st.file_uploader("Subir imágenes", type=["png", "jpg", "jpeg"])
        if archivo is not None:
            detalle_archivo = {"nombre_archivo": archivo.name,
                            "tipo_archivo": archivo.type,
                            "tamanio_archivo": archivo.size}
            st.write(detalle_archivo)
        
    elif eleccion == "Conjunto de datos":
        st.header("Conjunto de datos")
    elif eleccion == "Archivo de documentos":
        st.header("Archivo de documentos")

if __name__ == '__main__':
    main()