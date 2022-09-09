from email.mime import image
import statistics
from PIL import Image

im = Image.open('teste2.jpg','r')

rgb = list(im.getdata())

pixel = im.load()

mediana = pixel

largura, altura = im.size
##Mascara de tamnaho 1
mascara = 2
##Mediana
for i in range(im.size[0]):
    for j in range(im.size[1]):
        if i > 0 and j < (altura - mascara):
            if j > 0 and i < (largura - mascara):
                mediana[i,j] = (statistics.median([pixel[i,j][0],pixel[i+1,j][0],pixel[i,j+1][0],pixel[i+1,j+1][0],
                                pixel[i-1,j-1][0],pixel[i+1,j-1][0],pixel[i-1,j+1][0],pixel[i-1,j][0],pixel[i,j-1][0]]),
                                statistics.median([pixel[i,j][1],pixel[i+1,j][1],pixel[i,j+1][1],pixel[i+1,j+1][1],
                                pixel[i-1,j-1][1],pixel[i+1,j-1][1],pixel[i-1,j+1][1],pixel[i-1,j][1],pixel[i,j-1][1]]),
                                statistics.median([pixel[i,j][2],pixel[i+1,j][2],pixel[i,j+1][2],pixel[i+1,j+1][2],
                                    pixel[i-1,j-1][2],pixel[i+1,j-1][2],pixel[i-1,j+1][2],pixel[i-1,j][2],pixel[i,j-1][2]]))
            else:
                mediana[i,j] = (255,255,255)
        else:
            mediana[i,j] = (255,255,255)
    for j in range(im.size[1]):
        pixel[i,j] = mediana[i,j]
im.save('mediana.jpg')

pixel = im.load()

media = pixel

for i in range(im.size[0]):
    for j in range(im.size[1]):
        if i > 0 and j < (altura - mascara):
            if j > 0 and i < (largura - mascara):
                media[i,j] = (statistics.mean([pixel[i,j][0],pixel[i+1,j][0],pixel[i,j+1][0],pixel[i+1,j+1][0],
                                pixel[i-1,j-1][0],pixel[i+1,j-1][0],pixel[i-1,j+1][0],pixel[i-1,j][0],pixel[i,j-1][0]]),
                                statistics.mean([pixel[i,j][1],pixel[i+1,j][1],pixel[i,j+1][1],pixel[i+1,j+1][1],
                                pixel[i-1,j-1][1],pixel[i+1,j-1][1],pixel[i-1,j+1][1],pixel[i-1,j][1],pixel[i,j-1][1]]),
                                statistics.mean([pixel[i,j][2],pixel[i+1,j][2],pixel[i,j+1][2],pixel[i+1,j+1][2],
                                    pixel[i-1,j-1][2],pixel[i+1,j-1][2],pixel[i-1,j+1][2],pixel[i-1,j][2],pixel[i,j-1][2]]))
            else:
                media[i,j] = (255,255,255)
        else:
            media[i,j] = (255,255,255)
    for j in range(im.size[1]):
        pixel[i,j] = media[i,j]
im.save('media.jpg')