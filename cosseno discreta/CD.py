from socket import SOMAXCONN
import statistics
from tokenize import Double
from PIL import Image
import numpy as np
import math
import cv2
#define alfa(x,a1,a2) ((x==0) ? (a1) : (a2))
im = Image.open('teste5.jpg','r').convert('L')
im = cv2.imread
im.save("greyscale.jpg")
rgb = list(im.getdata())

#pixel = im.load()
pixel = ((16,  11,  10,  16,  24,  40,  51,  61),
  (12,  12,  14,  19,  26,  58,  60,  55),
  (14,  13,  16,  24,  40,  57,  69,  56),
  (14,  17,  22,  29,  51,  87,  80,  62),
  (18,  22,  37,  56,  68, 109, 103,  77),
  (24,  35,  55,  64,  81, 104, 113,  92),
  (49,  64,  78,  87, 103, 121, 120, 101),
  (72,  92,  95,  98, 112, 100, 103,  99))
soma = 0
#largura, altura = im.size
largura = 8
altura = 8
print(largura,altura)
n = altura
i = 0 
u = 0
v = 0
soma = 0
saida = Image.new('L', (largura,altura),color="black")
media = saida.load()
for u in range(largura):
    for v in range(altura):
        for i in range(largura):
            for j in range(altura):
                bidi = ((2*i) + 1)*math.pi*u/(2*largura)
                bidi2 = ((2*j) + 1)*math.pi*v/(2*altura)
                soma += ((pixel[i][j]) * math.cos(bidi) * math.cos(bidi2))
        if u == 0:
            alfa  = 1.0/math.sqrt(largura)
        else:
            alfa = math.sqrt(2.0/largura)
        soma *= alfa
        if v == 0:
            alfa  = 1.0/math.sqrt(altura)
        else:
            alfa = math.sqrt(2.0/altura)
        soma *= alfa
        print(int(soma))
        media[u,v] = int(soma)
        print(media[u,v])
        soma = 0
saida.save('cosseno.tif')