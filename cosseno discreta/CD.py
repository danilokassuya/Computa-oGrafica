import statistics
from tokenize import Double
from PIL import Image
import numpy as np
import math
#define alfa(x,a1,a2) ((x==0) ? (a1) : (a2))
im = Image.open('teste3.jpg','r').convert('L')
im.save("greyscale.jpg")
rgb = list(im.getdata())

pixel = im.load()
soma = 0
largura, altura = im.size
print(largura,altura)
n = altura
i = 0 
u = 0
v = 0
alfa1 = 1.0/math.sqrt(n)
alfa2 = math.sqrt(2.0/n)
soma = 0
saida = Image.new('L', (largura,altura),color="black")
media = saida.load()
for u in range(largura):
    for v in range(altura):
        for i in range(largura):
            for j in range(altura):
                bidi = float(((2*i) + 1)*math.pi*u/(2*altura))
                bidi2 = float(((2*j) + 1)*math.pi*v/(2*largura))
                soma += (pixel[i,j] * math.cos(bidi) * math.cos(bidi2))
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
        media[u,v] = int(soma)
        soma = 0
saida.save('cosseno.jpg')