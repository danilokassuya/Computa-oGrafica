from multiprocessing.resource_sharer import stop
from socket import SOMAXCONN
import statistics
from tokenize import Double
from PIL import Image
import numpy as np
import math
import cv2

pixel = cv2.imread('teste5.jpg',1)
pixel = cv2.cvtColor(pixel, cv2.COLOR_BGR2GRAY)
soma = 0
altura = pixel.shape[0]
largura = pixel.shape[1]
soma = 0

media = np.zeros((altura,largura), np.uint8)
array = [[0 for x in range(largura)] for y in range(altura)] 
for u in range(altura):
    for v in range(largura):
        for i in range(altura):
            for j in range(largura):
                bidi = ((2*i) + 1)*math.pi*u/(2*altura)
                bidi2 = ((2*j) + 1)*math.pi*v/(2*largura)
                soma += ((pixel[i][j]) * math.cos(bidi) * math.cos(bidi2))
        if u == 0:
            alfa  = 1.0/math.sqrt(altura)
        else:
            alfa = math.sqrt(2.0/altura)
        soma *= alfa
        if v == 0:
            alfa  = 1.0/math.sqrt(largura)
        else:
            alfa = math.sqrt(2.0/largura)
        soma *= alfa
        array[u][v] = soma
        if soma < 0: 
            soma = 0
        if soma > 255:
            soma = 1
        media[u][v] = soma
        soma = 0
cv2.imwrite("cosseno.jpg",media)

soma = 0
i = 0 
u = 0
v = 0
media = np.zeros((altura,largura,3), np.uint8)
for i in range(altura):
    for j in range(largura):
        for u in range(altura):
            for v in range(largura):
                bidi = float(((2*i) + 1)*math.pi*u/(2*altura))
                bidi2 = float(((2*j) + 1)*math.pi*v/(2*largura))
                if u == 0:
                    alfaA  = 1.0/math.sqrt(altura)
                else:
                    alfaA = math.sqrt(2.0/altura)
                if v == 0:
                    alfaB = 1.0/math.sqrt(largura)
                else:
                    alfaB = math.sqrt(2.0/largura)
                soma += (array[u][v] * math.cos(bidi) * math.cos(bidi2) * alfaA * alfaB)
        media[i][j]= (int(soma))
        soma = 0
cv2.imwrite("invertida.jpg",media)
