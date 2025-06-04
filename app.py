import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt
from PyPDF2 import PdfReader

st.set_page_config(page_title="Mi App Streamlit", page_icon="smile", layout="wide", initial_sidebar_state="collapsed")

df = pd.read_csv("covid_data.csv")

def main():
    st.title("Curso de Streamlit")
    st.sidebar.header("Navegación")

if __name__ == '__main__':
    main()