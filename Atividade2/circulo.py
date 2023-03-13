import matplotlib.pyplot as plt
import numpy as np

xc = int(input("Selecione o valor x:"))
yc = int(input("Selecione o valor y:"))
raio = int(input("Selecione o valor do raio:"))

p = 1 - raio

teste = []
y = raio
x = 0
teste.append((xc+x,raio+yc))
while x < y:
    x = x + 1
    if p < 0:
        p = p + 2*x + 1
    else:
        y = y -1
        p = p + 2*x + 1 - 2*y
    teste.append((x+xc,y+yc))
    teste.append((x+xc,-y+yc))
    teste.append((-x+xc,y+yc))
    teste.append((-x+xc,-y+yc))
    teste.append((y+xc,x+yc))
    teste.append((y+xc,-x+yc))
    teste.append((-y+xc,x+yc))
    teste.append((-y+xc,-x+yc))   

reta=np.array(teste)
plt.scatter(reta[:,0], reta[:,1])

plt.show()
