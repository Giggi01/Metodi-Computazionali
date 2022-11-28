import matplotlib.pyplot as plt
import scipy as sc
import numpy as np
import math

def func_sin(x):
    fsin = (1/4)*np.sin(x/2)
    return fsin

x = np.arange(0, 2*math.pi, 0.001)

plt.plot(x, func_sin(x), color = 'orange')
plt.show()

#Numero di valori estartti per generare la distribuzione
sample = 100000

# Genero numeri random con la tecnica di hit or miss a partire da nsample (100k) valori estratti
xhm = np.random.uniform(low=0, high=2*math.pi, size=sample)  # Nsample valori di x (0-5)
yhm = np.random.random(sample)  

maskhm = yhm <= func_sin(xhm)
xdistq = xhm[maskhm]

# Istogramma dei valori x selezionati
plt.hist(xdistq, bins=100, range=(0,2*math.pi), color='lightgreen')
plt.show()


def cum_sin(x):

    #Maschere per intervalli di x

    yy = np.zeros(len(x))
    mask1   = (x >= 0  ) & ( x <= (1/2)*math.pi )
    mask2   = (x >= (1/2)*math.pi  ) & ( x <= math.pi)
    mask3   = (x >= math.pi) & ( x <= (3/2)*math.pi )
    mask4   = (x >= (3/2)*math.pi  ) & ( x <= 2*math.pi )

    #Calcolo valore cumulativa per diversi intervalli di x

    yy[mask1]   = -2*np.cos(x/2)[mask1]
    yy[mask2]   = ((-(np.sqrt(2))/(4)) + (1/2)) - 2*np.cos(x/2)[mask2] - (1/4)*np.sin(x/2)[mask2]*(math.pi/2)
    yy[mask3]   = ((-(np.sqrt(2))/(4)) + (1/2)) + ((np.sqrt(2))/4) - 2*np.cos(x/2)[mask3] - (1/4)*np.sin(x/2)[mask3]*(math.pi)
    yy[mask4]   = ((-(np.sqrt(2))/(4)) + (1/2)) + ((np.sqrt(2))/4) + ((np.sqrt(2))/4) - 2*np.cos(x/2)[mask4] - (1/4)*np.sin(x/2)[mask3]*((3*math.pi)/2)

    #Normalizzazione a 1

    norm1 = ((-(np.sqrt(2))/(4)) + (1/2)) + ((np.sqrt(2))/4) + ((np.sqrt(2))/4) + ((1/2)-((np.sqrt(2)/4)))

    return yy/norm1

#Grafico funzione sinusoide e della sua cumulativa nell'intervallo (0,2pigreco)

xx = np.arange(0, 2*math.pi, 0.0001)
plt.plot(xx, cum_sin(xx), color='orange')
plt.grid()
plt.xlabel('x')
plt.ylabel('c(x)')
plt.show()

#Inversa della cumulativa

def inv_cum_sin(y):

    norm = ((-(math.sqrt(2))/(4)) + (1/2)) + ((math.sqrt(2))/4) + ((math.sqrt(2))/4) + ((1/2)-((math.sqrt(2)/4)))
    cstep1 = (-(math.sqrt(2))/(4)) 
    cstep2 = (-(math.sqrt(2))/(4)) + (1/2) + ((math.sqrt(2))/4)
    cstep3 = ((-(math.sqrt(2))/(4)) + (1/2)) + ((math.sqrt(2))/4) + ((math.sqrt(2))/4)
    cstep4 = norm

    mask1   = (y >= 0          ) & (y <  cstep1/norm)
    mask2   = (y >= cstep1/norm) & (y <  cstep2/norm)
    mask3   = (y >= cstep2/norm) & (y <  cstep3/norm)
    mask4   = (y >= cstep3/norm) & (y <= cstep4/norm)

    xx = np.zeros(len(y))

    xx[mask1] =  y[mask1]*norm         /(1/4)*np.sin(y/2)[mask1]  
    xx[mask2] = ((y[mask2]*norm-cstep1)/(1/4)*np.sin(y/2)[mask2]  + (math.pi/2))
    xx[mask3] = ((y[mask3]*norm-cstep2)/(1/4)*np.sin(y/2)[mask3]     + math.pi)
    xx[mask4] = ((y[mask4]*norm-cstep3)/(1/4)*np.sin(y/2)[mask4]     + (3*math.pi/2) )

    return xx

#Grafico invesra cumulativa della funzione sinusoide nell'intervallo (0,2pigreco)

yc  = np.arange(0,1, 0.001)
xc  = inv_cum_sin(yc)
plt.plot(yc, xc, color='darkcyan')
plt.grid()
plt.xlabel('y')
plt.ylabel('$c^{-1}$(y)')
plt.show()

#Riproduco distribuzione con 10k eventi

#Valori y distribuiti uniformemnte in )0-1)
yrndq = np.random.random(sample)

# valori x da cumulativa inversa
xrndq = inv_cum_sin(yrndq)

fig, ax = plt.subplots(1,2, figsize=(11,5))
ax[0].hist(yrndq, bins=100, range=(0,1), color='cyan',   ec='darkcyan')
ax[0].set_title('Distribuzione y Cumulativa')
ax[0].set_xlabel('y cumulativa')

ax[1].hist(xrndq, bins=100, range=(0,5), color='orange', ec='darkorange')
ax[1].set_title('Distribuzione secondo la funzione sinusoide')
ax[1].set_xlabel('x')
plt.show()