import streamlit as st
import pandas as pd
from PIL import Image

def main():
    st.title("Curso de Streamlit")
    #Captura de inputs
    nombre = st.text_input("Ingresa tu nombre")

    mensaje = st.text_area("Ingresa tu mensaje", height=100)

    numero = st.number_input("Ingresa un número", 1.0, 25.0, step=1.0) # min, max

    cita = st.date_input("Selecciona una fecha")

    hora = st.time_input("Selecciona la hora")

    color = st.color_picker("Selecciona un color")
    

if __name__ == '__main__':
    main()