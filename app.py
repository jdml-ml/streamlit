import streamlit as st
import pandas as pd

df = pd.read_csv("covid_data.csv")
# df2 = df.sample(n=1000, random_state=42)
numeric_cols = df.select_dtypes(include='number').columns

# st.dataframe(df2.style.highlight_max(axis=0)) # máx filas 262144

def main():
    st.title("Curso de Streamlit")
    #SelectBox
    opcion = st.selectbox(
        'Elige una opción',
        ['Opción 1', 'Opción 2', 'Opción 3', 'Opción 4']
    )
    st.write(f"Tu opción es {opcion}")

    #Multiselect
    opciones = st.multiselect(
        'Selecciona tus colores favoritos',
        ['Rojo', 'Verde', 'Azul', 'Amarillo', 'Negro', 'Blanco']
    )
    st.write('Tus colores favoritos son:', opciones)

    #Slider (para números)
    edad = st.slider(
        'Selecciona tu edad',
        min_value=0,
        max_value=100,
        value=25, #Valor inicial
        step=1
    )
    st.write('Tu edad es', edad)

    #Select Slider (para categorias)
    nivel = st.select_slider(
        'Selecciona tu nivel de satisfacción',
        options=['Muy bajo', 'Bajo', 'Medio', 'Alto', 'Muy alto'],
        value="Medio"
    )
    st.write(f'Tu nivel de satisfacción es: {nivel}')
    

if __name__ == '__main__':
    main()