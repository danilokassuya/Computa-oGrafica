import statistics
from tokenize import Double
from PIL import Image
import numpy as np
import math
#define alfa(x,a1,a2) ((x==0) ? (a1) : (a2))

im = Image.open('teste.jpg','r')

rgb = list(im.getdata())

pixel = im.load()
soma = 0
largura, altura = im.size
n = altura
i = 0 
u = 0
v = 0
alfa1 = 1.0/math.sqrt(n)
alfa2 = math.sqrt(2.0/n)
soma = 0
for a in range(largura):
    for b in range(altura):
        for i in range(largura):
            for j in range(altura):
                bidi = float((2*i) + 1)
                bidi2 = float((2*j) + 1)
                soma += pixel[i,j][0] * math.cos(bidi) * math.cos(bidi2)
        if u == 0:
            alfa  = alfa1
        else:
            alfa = alfa2
        soma *= alfa
        if v == 0:
            alfa  = alfa1
        else:
            alfa = alfa2
        soma *= alfa
        print(soma)