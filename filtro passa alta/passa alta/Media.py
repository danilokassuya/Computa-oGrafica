from email.mime import image
import statistics
from PIL import Image
import numpy as np

im = Image.open('teste3.jpg','r')

rgb = list(im.getdata())

pixel = im.load()

mediana = pixel

largura, altura = im.size
##Mascara de tamnaho 1
##mascara = input("Tamamho da mascara:")
mascara = 2
pesos = [-1,-2,-1],[0,0,0],[1,2,1]
##Mediana

def getPixelMascara(pixel,i,j,tipo):
    pixels = 0
    if tipo == 0:
        for a in range(3):
            for b in range(3):
                pixels += pixel[i+a-1,j+b-1][0]*pesos[a][b]
    if tipo == 1:
        for a in range(3):
            for b in range(3):
               pixels += pixel[i+a-1,j+b-1][1]*pesos[a][b]
    if tipo == 2:
        for a in range(3):
            for b in range(3):
                pixels += pixel[i+a-1,j+b-1][2]*pesos[a][b]
    pixels = pixels/9
    print(pixels)
    if pixels < 0:
        pixels = pixels * -1
    print(pixels)
    return int(pixels)

for i in range(im.size[0]):
    for j in range(im.size[1]):
        if i > 0 and j < (altura - mascara):
            if j > 0 and i < (largura - mascara):
                mediana[i,j] = (getPixelMascara(pixel,i,j,0),
                                getPixelMascara(pixel,i,j,1),
                                getPixelMascara(pixel,i,j,2))
            else:
                mediana[i,j] = (255,255,255)
        else:
            mediana[i,j] = (255,255,255)
    for j in range(im.size[1]):
        pixel[i,j] = mediana[i,j]
im.save('mediana.jpg')

