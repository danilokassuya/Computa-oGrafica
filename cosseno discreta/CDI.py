import statistics
from tokenize import Double
from PIL import Image
import numpy as np
import math
im = Image.open('cosseno.jpg','r')

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
for i in range(largura):
    for j in range(altura):
        for u in range(largura):
            for v in range(altura):
                bidi = float(((2*i) + 1)*math.pi*u/(2*altura))
                bidi2 = float(((2*j) + 1)*math.pi*v/(2*largura))
                if u == 0:
                    alfaA  = alfa1
                else:
                    alfaA = alfa2
                if v == 0:
                    alfaB  = alfa1
                else:
                    alfaB = alfa2
                soma += (pixel[u,v] * math.cos(bidi) * math.cos(bidi2) * alfaA * alfaB)
        media[i,j] = (int(soma))
        soma = 0
saida.save('invertida.jpg')