import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy import integrate

#Lettura file 

df_fromfile = pd.read_csv('vel_vs_time.csv')
#df_fromfile

#Creazione grafico velocita in funzione del tempo

ax = df_fromfile['t']

ay = df_fromfile['v']

fig = plt.figure()
plt.plot(ax, ay ,'o-', color = 'limegreen', label = 'Velocita')
plt.xlabel('Time')
plt.ylabel('Velocity')
fig.suptitle('Grafico Velocita-Tempo', fontsize = 20)
plt.legend()
plt.grid(True)
plt.show()

#Calcolo dell'integrale su tutto il tempo

distanza_tot = sc.integrate.simpson(ax, ay)
print('La distanza totale percorsa è: ', distanza_tot)

#Definisco l'array delle distanze calcolate con il metodo scipy.integrate.simpson tramite un ciclo for

distanza = np.array([])
for i in range(len(ax)):
    distanza = np.append(distanza, sc.integrate.simpson(ay[:i+1], ax[:i+1]))
#print(distanza)

#Creazione del grafico distanza-tempo
fig = plt.figure()
plt.plot(distanza, ax, 'o-', color = 'red', label = 'Distanza')
plt.xlabel('Time')
plt.ylabel('Distance')
fig.suptitle('Grafico Distanza-Tempo', fontsize = 20)
plt.legend()
plt.grid(True)
plt.show()

