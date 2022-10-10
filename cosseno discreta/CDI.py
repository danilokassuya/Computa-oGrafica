from locale import normalize
import statistics
from tokenize import Double
from PIL import Image
import numpy as np
import math
import cv2
pixel = cv2.imread('cosseno.jpg',1)
pixel = cv2.cvtColor(pixel, cv2.COLOR_BGR2GRAY)
soma = 0
altura = pixel.shape[0]
largura = pixel.shape[1]
print(largura,altura)
print(pixel)
n = altura
i = 0 
u = 0
v = 0
alfa1 = 1.0/math.sqrt(n)
alfa2 = math.sqrt(2.0/n)
soma = 0
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
                soma += (pixel[u][v] * math.cos(bidi) * math.cos(bidi2) * alfaA * alfaB)
        print(soma)
        media[j][i]= (int(soma))
        soma = 0
cv2.imwrite("invertida.jpg",media)