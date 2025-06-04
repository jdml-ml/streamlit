import streamlit as st

st.set_page_config(page_title="Mi App Streamlit", page_icon="smile", layout="wide", initial_sidebar_state="collapsed")

def main():
    st.title("Curso de Streamlit")
    st.sidebar.header("Navegación")
    

if __name__ == '__main__':
    main()