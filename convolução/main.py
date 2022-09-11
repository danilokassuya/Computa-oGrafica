from email.mime import image
import statistics
from traceback import print_tb
from PIL import Image

def getPixelMascara(pixel,i,j,tipo,mascara):
    pixels = []
    a = i-mascara
    b = j-mascara
    if tipo == 0:
        for a in range(i-mascara,i+mascara+1):
            for b in range(j-mascara,j+mascara+1):
                pixels.append(int(pixel[a,b][0]))
    if tipo == 1:
        for a in range(i-mascara,i+mascara+1):
            for b in range(j-mascara,j+mascara+1):
                pixels.append(int(pixel[a,b][1]))
    if tipo == 2:
        for a in range(i-mascara,i+mascara+1):
            for b in range(j-mascara,j+mascara+1):
                pixels.append(int(pixel[a,b][2]))
    return pixels


im = Image.open('teste.jpg','r')

rgb = list(im.getdata())

pixel = im.load()

largura, altura = im.size
##Mascara de tamnaho 1
mascara = int(input("Selecione o tamanho da mascara\n"))

media = pixel

for i in range(im.size[0]):
    for j in range(im.size[1]):
        if i > 0 and j < (altura - mascara):
            if j > 0 and i < (largura - mascara):
                media[i,j] = (int(statistics.mean(getPixelMascara(pixel,i,j,0,mascara))),
                                int(statistics.mean(getPixelMascara(pixel,i,j,1,mascara))),
                                int(statistics.mean(getPixelMascara(pixel,i,j,2,mascara))))
            else:
                media[i,j] = (255,255,255)
        else:
            media[i,j] = (255,255,255)
    for j in range(im.size[1]):
        pixel[i,j] = media[i,j]
im.save('media.jpg')