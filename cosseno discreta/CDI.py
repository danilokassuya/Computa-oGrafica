import statistics
from tokenize import Double
from PIL import Image, ImageOps
import numpy as np
import math
#define alfa(x,a1,a2) ((x==0) ? (a1) : (a2))
im = Image.open('cosseno.jpg','r')
im = ImageOps.grayscale(im)
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
soma1 = 0
soma2 = 0
soma3 = 0
saida = Image.new('grayscale', (largura,altura),color="black")
media = saida.load()
for u in range(largura):
    for v in range(altura):
        for i in range(largura):
            for j in range(altura):
                bidi = float(((2*i) + 1)*math.pi*u/(2*altura))
                bidi2 = float(((2*j) + 1)*math.pi*v/(2*largura))
                soma1 += (pixel[i,j][0] * math.cos(bidi) * math.cos(bidi2))
                soma2 += (pixel[i,j][1] * math.cos(bidi) * math.cos(bidi2))
                soma3 += (pixel[i,j][2] * math.cos(bidi) * math.cos(bidi2))
                print(bidi,bidi2)
                if u == 0:
                    alfa  = alfa1
                else:
                    alfa = alfa2
                soma1 *= alfa
                soma2 *= alfa
                soma3 *= alfa
                if v == 0:
                    alfa  = alfa1
                else:
                    alfa = alfa2
                soma1 *= alfa
                soma2 *= alfa
                soma3 *= alfa
        media[u,v] = (int(soma1),int(soma2),int(soma3))
        soma = 0
saida.save('invertida.jpg')