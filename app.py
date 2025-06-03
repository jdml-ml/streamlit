import streamlit as st
import pandas as pd

df = pd.read_csv("covid_data.csv")
# df2 = df.sample(n=1000, random_state=42)
numeric_cols = df.select_dtypes(include='number').columns

# st.dataframe(df2.style.highlight_max(axis=0)) # máx filas 262144

def main():
    st.title("Curso de Streamlit")
    st.header("Dataframe:")
    st.dataframe(df)
    # st.dataframe(df.style.highlight_min(axis=0, subset=numeric_cols))
    # st.text(df.dtypes)
    # st.dataframe(df.style.highlight_max(axis=0)) # máx filas 262144
    # st.table(df) #solo para tablas pequeñas
    st.json({"clave": "valor"}) #formato JSON
    ### Visualizar código python
    codigo = """
                def saludar():
                    print("Hola")
            """
    st.code(codigo, language="python")
    

if __name__ == '__main__':
    main()