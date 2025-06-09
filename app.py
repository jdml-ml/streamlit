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
    menu = ["Imágenes", "Conjunto de datos", "Archivo de documentos"]
    eleccion = st.sidebar.selectbox("Menú", menu)
    if eleccion == "Imágenes":
        st.header("Imagen")
        archivo = st.file_uploader("Subir imágenes", type=["png", "jpg", "jpeg"])
        if archivo is not None:
            detalle_archivo = {"nombre_archivo": archivo.name,
                            "tipo_archivo": archivo.type,
                            "tamanio_archivo": archivo.size}
            st.write(detalle_archivo)
            st.image(cargar_imagen(archivo), width=350)
        
    elif eleccion == "Conjunto de datos":
        st.header("Conjunto de datos")
        archivo_datos = st.file_uploader("Subir CSV o Excel", type=["csv", "xls", "xlsx"])
        if archivo_datos is not None:
            detalle = {"nombre_archivo": archivo_datos.name,
                            "tipo_archivo": archivo_datos.type,
                            "tamanio_archivo": archivo_datos.size}
            st.write(detalle)
            if detalle["tipo_archivo"] == "text/csv":
                df = pd.read_csv(archivo_datos)
            elif detalle["tipo_archivo"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                df = pd.read_excel(archivo_datos, engine='openpyxl')
            else:df=pd.DataFrame()
            st.dataframe(df)
            
    elif eleccion == "Archivo de documentos":
        st.header("Archivo de documentos")
        archivo_doc = st.file_uploader("Subir documento", type=["pdf", "docx", "txt"])
        if st.button("Procesar"):
            if archivo_doc is not None:
                detalle = {"nombre_archivo": archivo_doc.name,
                            "tipo_archivo": archivo_doc.type,
                            "tamanio_archivo": archivo_doc.size}
                st.write(detalle)
                if detalle["tipo_archivo"] == "text/plain":
                    text = str(archivo_doc.read(), "utf-8")
                    st.write(text)
                elif archivo_doc.type == "application/pdf":
                    text = leer_pdf(archivo_doc)
                    st.write(text)
                elif archivo_doc.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    text = docx2txt.process(archivo_doc)
                    st.write(text)
                

if __name__ == '__main__':
    main()