from calendar import c
import cmath
from re import M, X
from PIL import Image

im = Image.open('test.jpg','r')
rgb = list(im.getdata())

pixel = im.load()

for i in range(im.size[0]):
    for j in range(im.size[1]):
        c = 1 - (pixel[i,j][0]/255) 
        m = 1 - (pixel[i,j][1]/255) 
        y = 1 - (pixel[i,j][2]/255)
        k = min(c,m,y)
        c = (c-k)/(1-k)
        m = (m-k)/(1-k)
        y = (y-k)/(1-k) 
        c = int(c*255)
        m = int(m*255)
        y = int(y*255) 
        pixel[i,j] = (c,m,y)

im.save('cmy.jpg')
for i in range(im.size[0]):
    for j in range(im.size[1]):
        r = pixel[0,0][0]
        g = pixel[0,0][1]
        b = pixel[0,0][2]
        if b <= g:
            h = cmath.cos((((r-g)+(r-b))/2)/((r-g)**2)+((r-b)*(g-b))*1/2)**-1
        else:
            h = 360 - cmath.cos((((r-g)+(r-b))/2)/((r-g)**2)+((r-b)*(g-b))*1/2)**-1
        s = 1 - 3*min(r,g,b)/(r+g+b)
        i = (r+g+b)/3
im.save('hsi.jpg')