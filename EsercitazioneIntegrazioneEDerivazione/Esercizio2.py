import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy import integrate

#Definizione di alcune variabili

x0 = 0.1*4.5**6
xx = np.arange(-5, 5.05, 0.1)
dx = 0.1
k = 0.1
y0 = 4.5
massa = 5
print(len(xx))

#Grafico iniziale del potenziale

plt.plot(xx, k*xx**6, color='limegreen')
plt.axvline(color = 'k', linewidth = 0.5)
plt.xlabel('x')
plt.ylabel('V(x)')
plt.plot(y0 , x0 , 'o', markersize = 12, color = 'tomato')
plt.show()

#Definisco la funzione V(x)

#def vx(x):
    #pot = 0.1*x**6
    #return pot

#Creo un array di velocita al quadrato

velocity = (np.gradient(xx))**2

#Definisco la funzione di V(x0)

#def vx0(massa, vel, potenziale):
    #pot0 = ((0.5)*massa*vel)+potenziale
    #return pot0

#Definisco l'integranda

def integ(x, m, vel):
    pot = 0.1*x**6
    pot0 = ((0.5)*m*vel)+pot
    int = (pot0 - pot)**(-1/2)

#Calcolo l'integrale

periodo = np.array([])
for i in range(len(xx)):
    periodo = np.append(periodo, sc.integrate.simpson(integ(xx, massa, velocity)[:i],dx = dx))
    print(periodo)
