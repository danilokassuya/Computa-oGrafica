from cgi import print_arguments
from email.mime import image
import statistics
from tkinter import W
from traceback import print_tb
from tracemalloc import start
from PIL import Image

def verificaFormato(formato,i,j,pixel):
    maior = 0
    i -= formato
    j -= formato
    for x in range(formato+1):
        for y in range(formato+1):
            if maior < pixel[i+x,j+y]:
                maior = pixel[i+x,j+y]
    print(maior)
    return maior

im = Image.open('teste5.jpg','r').convert('1')

pixel = im.load()

largura, altura = im.size
#formato = input("Selecione o tamanho da mascara:")
formato = 1
saida = Image.new('L', (largura,altura))
dilatacao = saida.load()
for i in range(im.size[0]):
    for j in range(im.size[1]):
        dilatacao[i,j] = verificaFormato(formato,i,j,pixel)
saida.save('dilatação.jpg')