import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import math

scalar = 2.0

#Funzione del random walker

def runwalk(s, passi):
    walkx = [0.0]
    walky = [0.0]
    for i in range(0, passi-1, 1):
        phi = np.random.uniform(low = 0.0,  high = 2*math.pi, size = 1)
        dx = s*math.cos(phi)
        dy = s*math.sin(phi)
        walkx.append(walkx[i]+dx)
        walky.append(walky[i]+dy)
    return walkx, walky

#Grafico 2D delle posizioni di 5 random walker per 1000 passi.

for i in range(0, 5, 1):
    random = runwalk(scalar, 1000)
    randomx = random[0]
    randomy = random[1]
    plt.plot(randomx, randomy, '-', label = 'RunWalker')
plt.xlabel('Passi X')
plt.ylabel('Passi Y')
plt.legend()
plt.show()


#Grafico 2D della posizione di 1000 random walker dopo 10, 100 e 1000 passi.

for i in range(0, 1000, 1):
    random = runwalk(scalar, 1000)
    randomx = random[0]
    randomy = random[1]
    plt.plot(randomx[9], randomy[9], 'o', color = 'red', label = '10imo passo')
    plt.plot(randomx[99], randomy[99], 'o', color = 'blue', label = '100imo passo')
    plt.plot(randomx[999], randomy[999], 'o', color = 'green', label = '1000imo passo')
plt.xlabel('Passi X')
plt.ylabel('Passi Y')
plt.show()
