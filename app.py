import streamlit as st
import pandas as pd
from PIL import Image

def main():
    st.title("Curso de Streamlit")
    img = Image.open("Julia.png")
    st.image(img, use_container_width=True)
    st.write("Tomada de: PantheraLeo1359531, CC0, via Wikimedia Commons")
    # Imagen aleatoria de internet
    st.image("https://picsum.photos/1920")

    # with open("tu_video.mp4", 'rb') as video_file:
    #     st.video(video_file.read(), start_time=0)

    # with open("tu_audio.mp3", 'rb') as audio_file:
    #     st.audio(audio_file.read(), start_time=0)
    

if __name__ == '__main__':
    main()