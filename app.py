import streamlit as st

def main():
    st.title("Curso de Streamlit")
    st.header("Esto es un encabezado")
    # Formateo de texto con variables
    var = "Juan"
    st.text(f"Hola {var}, esto es un texto")
    st.markdown("## Markdown --> h2")
    
    st.success("Éxito")
    st.warning("Esto es una advertencia")
    st.info("Esto es información")
    st.error("Esto es un error")
    
    st.exception("Esto es una excepción")

if __name__ == '__main__':
    main()