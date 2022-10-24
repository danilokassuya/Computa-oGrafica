import statistics
from PIL import Image
from numpy import np
im = Image.open('teste4.jpg','r')

rgb = list(im.getdata())

pixel = im.load()

histograma = np.zeros(255,dtype=np.float32)

for i in range(im.size[0]):
    for j in range(im.size[1]):
        k = pixel[i,j][0]
        histograma[k] = histograma[k] + 1

largura, altura = im.size
p = []
for i in range(255):
        p[i][j] = histograma[k]/(altura*largura)


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