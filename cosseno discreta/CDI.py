from locale import normalize
import statistics
from tokenize import Double
from PIL import Image
import numpy as np
import math
im = Image.open('cosseno.jpg','r')

#pixel = im.load()
pixel = ([ 461, -168 , -14 ,  30 , -31 ,   8 ,   1,   -2],
 [-194  , -1 ,  38 ,   4 ,   6  ,  3  ,  5 ,  -5],
 [  32  , 43,   10 , -22  , 15  ,-10  , -5 ,   4],
 [  -2 , -27  , -1   , 0  , -2  ,  7  ,  4  , -3],
 [   2 ,  11 ,   0  ,  1 ,   4  , -4 ,   1  , -2],
 [   0  , -3  ,  2  ,  2  ,  0  , -2  ,  0  ,  2],
 [  -9  ,  6  ,  4 ,  -8  ,  7 ,  -1  , -6   , 7],
 [   8  , -1 ,  -3 ,   1 ,   2  ,  3  , -1 ,  -1])
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
                bidi = float(((2*i) + 1)*math.pi*u/(2*largura))
                bidi2 = float(((2*j) + 1)*math.pi*v/(2*altura))
                if u == 0:
                    alfaA  = 1.0/math.sqrt(largura)
                else:
                    alfaA = math.sqrt(2.0/largura)
                if v == 0:
                    alfaB = 1.0/math.sqrt(altura)
                else:
                    alfaB = math.sqrt(2.0/altura)
                soma += (pixel[u][v] * math.cos(bidi) * math.cos(bidi2) * alfaA * alfaB)
        print(int(soma))
        media[i,j] = (int(soma))
        soma = 0
saida.save('invertida.jpg')