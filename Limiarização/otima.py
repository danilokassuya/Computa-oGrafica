from multiprocessing.connection import wait
import statistics
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('teste3.jpg','r').convert('L')

pixel = im.load()

largura, altura = im.size

histograma = np.zeros(256,dtype=np.float32)

for i in range(im.size[0]):
    for j in range(im.size[1]):
        k = pixel[i,j]
        histograma[k] = histograma[k] + 1
plt.bar(list(range(256)),histograma)
#plt.show()

count = 0
total = altura * largura
while count < 256:
    histograma[count] = histograma[count]/total
    count += 1
melhorT = 0
t = 1
p = 1
while t < 256:
    count = 0
    p1 = 0
    p2 = 0
    intensidade1 = 0
    intensidade2 = 0
    while count < t:
        p1 += histograma[count]
        intensidade1 += histograma[count]*count
        count += 1
    while count < 256:
        p2 += histograma[count]
        intensidade2 += histograma[count]*count
        count += 1
    if p1 != 0:
        m1 = (1/p1)*intensidade1
        if p2 != 0:
            m2 = (1/p2)*intensidade2
            mg = intensidade2 + intensidade1
            variancia = p1*pow((m1-mg),2) + p2*pow((m2-mg),2)
            if melhorT < variancia:
                melhorT = variancia
                p = t
    t += 1

saida = Image.new('L', (largura,altura),color="black")
pixel2 = saida.load()
for i in range(im.size[0]):
    for j in range(im.size[1]):
        if pixel[i,j] <= p:
            pixel2[i,j] = 0
        else:
            pixel2[i,j] = 255
saida.save('limiarização.jpg')