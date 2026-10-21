import numpy as np
import streamlit as st

def ampliar(imagem, k=40):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

bandeira = np.zeros((12, 18, 3), dtype=np.uint8)
bandeira[0:4, :18] = (0, 0, 0)
bandeira[4:8, :18] = (221, 0, 0)
bandeira[8:12, :18] = (255, 206, 0)

st.image(ampliar(bandeira))

st.write("ich bin kein roboter, ich bin deutscher!")