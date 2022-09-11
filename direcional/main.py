from cgi import print_arguments
from email.mime import image
import statistics
from traceback import print_tb
from tracemalloc import start
from PIL import Image

def getPixelMascara(pixel,i,j,tipo,tamanho,mascara):
    pixels = 0
    a = i-tamanho
    b = j-tamanho
    k = 0
    if tipo == 0:
        for b in range(j-tamanho,j+tamanho+1):
            for a in range(i-tamanho,i+tamanho+1):
                pixels += int(pixel[a,b][0]) * mascara[k]
                k += 1
    if tipo == 1:
        for b in range(j-tamanho,j+tamanho+1):
            for a in range(i-tamanho,i+tamanho+1):
                pixels += int(pixel[a,b][1]) * mascara[k]
                k += 1
    if tipo == 2:
        for b in range(j-tamanho,j+tamanho+1):
            for a in range(i-tamanho,i+tamanho+1):
                pixels += int(pixel[a,b][2]) * mascara[k]
                k += 1 
    if pixels < 0:
        pixels = 0
    if pixels >255:
        pixels = 0
    return pixels


im = Image.open('teste4.jpg','r')

rgb = list(im.getdata())

pixel = im.load()

largura, altura = im.size
tamanho = 1
#tamanho = int(input("Selecione o tamanho da mascara\n"))
direcao = int(input("Selecione a direção\n1-horizontal:\n2-vertical:\n3-+45:\n4--45:\n"))
if direcao == 1:
    mascara = [-0.5,-0.5,-0.5,1,1,1,-0.5,-0.5,-0.5]
elif direcao == 2:
    mascara = [-0.5,1,-0.5,-0.5,1,-0.5,-0.5,1,-0.5]
elif direcao == 3:
    mascara = [-1,-1,2,-1,2,-1,2,-1,-1]
elif direcao == 4:
    mascara = [2,-1,-1,-1,2,-1,-1,-1,2]


saida = Image.new('RGB', (largura,altura),color="black")
media = saida.load()
for i in range(im.size[0]):
    for j in range(im.size[1]):
        if i > (tamanho) and i < (largura - tamanho):
            if j > (tamanho) and j < (altura - tamanho):
                media[i,j] = (int(getPixelMascara(pixel,i,j,0,tamanho,mascara)),
                                int(getPixelMascara(pixel,i,j,1,tamanho,mascara)),
                                int(getPixelMascara(pixel,i,j,2,tamanho,mascara)))
            else:
                media[i,j] = (0,0,0)
        else:
            media[i,j] = (0,0,0)
saida.save('direcional.jpg')