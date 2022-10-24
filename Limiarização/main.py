from multiprocessing.connection import wait
import statistics
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('teste2.png','r').convert('L')

pixel = im.load()

largura, altura = im.size

histograma = np.zeros(256,dtype=np.float32)

for i in range(im.size[0]):
    for j in range(im.size[1]):
        k = pixel[i,j]
        histograma[k] = histograma[k] + 1
plt.bar(list(range(256)),histograma)
#plt.show()
p = 128
t = 0
while p != t:
    count = 0
    t = p
    total1 = 0
    intensidade1 = 0
    total2 = 0
    intensidade2 = 0
    while count < t:
        total1 += histograma[count]
        intensidade1 += histograma[count]*count
        count += 1
    while count < 256:
        total2 += histograma[count]
        intensidade2 += histograma[count]*count
        count += 1
    a = intensidade1/total1
    b = intensidade2/total2
    p = (a+b)/2
    p = round(p,0)

saida = Image.new('L', (largura,altura),color="black")
pixel2 = saida.load()
for i in range(im.size[0]):
    for j in range(im.size[1]):
        if pixel[i,j] <= p:
            pixel2[i,j] = 0
        else:
            pixel2[i,j] = 255
saida.save('limiarização.jpg')