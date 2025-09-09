

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import time


def pixel(matrix_img, kernel):
    soma = 0

    altura = len(matrix_img)
    comprimento = len(matrix_img[0])

    for linha in range(altura):
        for coluna in range(comprimento):
            soma += matrix_img[linha][coluna] * kernel[linha][coluna]

    return soma

def convolucao(img_path, kernel):

    tempo_inicial = time.time()

    img = np.array(Image.open(img_path).convert('RGB'))

    altura_image = img.shape[0]
    comprimento_image = img.shape[1]
    altura_kernel = len(kernel)
    comprimento_kernel = len(kernel[0])

    index_linha = 0
    index_coluna = 0

    matrix_resultante = []
    linha = []
    while True:

        matrix_image_spliced = img[index_linha:altura_kernel + index_linha, index_coluna:comprimento_kernel + index_coluna]
        linha.append(pixel(matrix_image_spliced, kernel))
        index_coluna += 1

        if index_coluna + comprimento_kernel > comprimento_image:
            index_coluna = 0
            index_linha += 1
            matrix_resultante.append(linha)
            linha = []

        if index_linha + altura_kernel > altura_image:
            break


    tempo_final = time.time()
    tempo_total = str(tempo_final - tempo_inicial)


    plt.imshow(matrix_resultante)
    plt.text(1, 60, tempo_total, fontfamily= 'sans-serif' ,size= 'large' ,color= 'yellow')

    plt.title('Imagem Convolucionada')
    plt.show()


    return 0

#kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
#convolucao('/home/luda/PycharmProjects/ComputacaoGrafica/atitus1.png', kernel)
#
