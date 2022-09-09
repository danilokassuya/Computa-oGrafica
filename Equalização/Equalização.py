from calendar import c
import cmath
from re import M, X
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

im = Image.open('teste.jpg','r')
rgb = list(im.getdata())

pixel = im.load()

histograma1 = np.zeros(255,dtype=np.float32)

histograma2 = np.zeros(255,dtype=np.float32)

histograma3 = np.zeros(255,dtype=np.float32)
total = 0
for i in range(im.size[0]):
    for j in range(im.size[1]):
        k = pixel[i,j][0]
        histograma1[k] = histograma1[k] + 1
        k = pixel[i,j][1]
        histograma2[k] = histograma2[k] + 1
        k = pixel[i,j][2]
        histograma3[k] = histograma3[k] + 1
largura, altura = im.size
total = largura*altura
print(total)
k=0
while k < 255:
    histograma1[k] = histograma1[k]/total
    histograma2[k] = histograma2[k]/total
    histograma3[k] = histograma3[k]/total   
    k +=1
plt.bar(list(range(255)),histograma1)
k = 1
acumulado = float(0)
while k < 255:
    histograma1[k] = histograma1[k] + histograma1[k-1]
    histograma2[k] = histograma2[k] + histograma2[k-1]
    histograma3[k] = histograma3[k] + histograma3[k-1]
    k += 1
print(histograma1)