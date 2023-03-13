import matplotlib.pyplot as plt
import numpy as np

x = int(input("Selecione o valor x1:"))
y = int(input("Selecione o valor y1:"))
x2 = int(input("Selecione o valor x2:"))
y2 = int(input("Selecione o valor y2:"))

dx = x2 - x
dy = y2 - y
p = 2*dy - dx

teste = []
teste.append((x,y))

while x != x2 and y != y2:
    if p < 0:
        x =  x + 1
        p = p + 2*dy
    else:
        x = x + 1
        y = y + 1
        p = p + 2*dy - 2*dx
    teste.append((x,y))

reta=np.array(teste)
plt.scatter(reta[:,0], reta[:,1])

plt.show()