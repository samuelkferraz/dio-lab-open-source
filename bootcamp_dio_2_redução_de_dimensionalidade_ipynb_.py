# -*- coding: utf-8 -*-
"""Bootcamp DIO // 2. Redução de Dimensionalidade.ipynb.

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fhmKnubaizw605K9Q9ndQVDYpnGrjkCK

O objetivo desse código é criar funções que transformem uma imagem colorida em níveis de cinza e em preto e branco. Faz parte do Bootcamp da DIO, consistindo em um desafio para praticar o conteúdo "Redução de Dimensionalidade".
"""

# Convertendo as matrizes para níveis de cinza

def rgb_to_gray(matriz_rgb):
    altura, largura, _ = matriz_rgb.shape
    matriz_gray = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            r, g, b = matriz_rgb[i, j]
            # Fórmula de conversão: Y = 0.299*R + 0.587*G + 0.114*B
            matriz_gray[i, j] = int(0.299 * r + 0.587 * g + 0.114 * b)

    return matriz_gray

matriz_gray = rgb_to_gray(matriz_rgb)

# Importando as bibliotecas

import requests
from PIL import Image
from io import BytesIO
import numpy as np

# Importando imagem do Github, lendo no código e convertendo para matriz RGB

url = "https://raw.githubusercontent.com/samuelkferraz/datasets-and-files/main/inhotim.JPEG"
response = requests.get(url, stream=True)
response.raw.decode_content = True # Ensure the content is decoded
img = Image.open(BytesIO(response.content))
img = img.convert("RGB")
matriz_rgb = np.array(img)

# Convertendo as matrizes para preto e branco

def binarize_image(matriz_gray, threshold=128):
    altura, largura = matriz_gray.shape
    matriz_bw = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            matriz_bw[i, j] = 255 if matriz_gray[i, j] > threshold else 0

    return matriz_bw

matriz_bw = binarize_image(matriz_gray)

# Voltando as matrizes para formato de imagem e exibindo resultados

img_gray = Image.fromarray(matriz_gray)
img_bw = Image.fromarray(matriz_bw)

img_gray.show()
img_bw.show()