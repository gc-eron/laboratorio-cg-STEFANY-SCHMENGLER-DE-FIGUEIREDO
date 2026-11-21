import cv2
import numpy as np
import streamlit as st
from PIL import Image
st.title("Trabalho prático")
foto = Image.open("imagens/foto.png")
img = np.array(foto)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
altura, largura = img.shape[0], img.shape[1]

# 1. Saturação
st.header("1. Saturação")
col1, col2 = st.columns(2)
fator = col1.slider("Saturação", 0.0, 2.0, 1.5)
s = hsv[:, :, 1].astype(float)
s = s * fator
s = np.clip(s, 0, 255)
hsv_s = hsv.copy()
hsv_s[:, :, 1] = s
col1.image(img, caption="original")
col2.image(cv2.cvtColor(hsv_s, cv2.COLOR_HSV2RGB), caption="saturação")

# 2. Brilho
st.header("2. Brilho")
col1, col2 = st.columns(2)
fator_v = col1.slider("Brilho", 0.0, 2.0, 1.5)
v = hsv[:, :, 2].astype(float)
v = v * fator_v
v = np.clip(v, 0, 255)
hsv_v = hsv.copy()
hsv_v[:, :, 2] = v
col1.image(img, caption="original")
col2.image(cv2.cvtColor(hsv_v, cv2.COLOR_HSV2RGB), caption="brilho")

# 4. Tons de cinza
st.header("4. Tons de cinza")
col1, col2 = st.columns(2)
media = img.mean(axis=2).astype(np.uint8)
col1.image(media, caption="média")
peso_r = col2.slider("Peso do R", 0.0, 1.0, 0.299)
peso_g = col2.slider("Peso do G", 0.0, 1.0, 0.587)
peso_b = col2.slider("Peso do B", 0.0, 1.0, 0.114)
ponderada = peso_r * img[:, :, 0] + peso_g * img[:, :, 1] + peso_b * img[:, :, 2]
ponderada = np.clip(ponderada, 0, 255).astype(np.uint8)
col2.image(ponderada, caption="média ponderada")

# 7. Inspetor de pixel
st.header("7. Inspetor de pixel")
col1, col2 = st.columns(2)
linha = col1.slider("Linha", 5, altura - 6, altura // 2)
coluna = col1.slider("Coluna", 5, largura - 6, largura // 2)
marcada = img.copy()
marcada[linha - 5:linha + 6, :] = (255, 0, 0)
marcada[:, coluna - 5:coluna + 6] = (255, 0, 0)
col1.image(marcada, caption="pixel marcado")
col2.text(f"RGB: {img[linha, coluna]}")
col2.text(f"HSV: {hsv[linha, coluna]}")
vizinhanca = img[linha - 5:linha + 6, coluna - 5:coluna + 6]
col2.image(vizinhanca.repeat(30, axis=0).repeat(30, axis=1), caption="vizinhança ampliada")

# 8. Negativo
st.header("8. Negativo")
col1, col2 = st.columns(2)
col1.image(img, caption="original")
col2.image(255 - img, caption="negativo")

# 13. Máscara de cor
st.header("13. Máscara de cor")
col1, col2 = st.columns(2, vertical_alignment="bottom")
h_min, h_max = col1.slider("Faixa de H", 0, 179, (140, 179))
mascara = cv2.inRange(hsv, (h_min, 60, 40), (h_max, 255, 255))
col1.image(img, caption="original")
col2.image(mascara, caption="máscara")