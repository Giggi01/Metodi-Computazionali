import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import reco as rc

###PASSO 1###

#Lettura di tutti i file (moduli)

datimodulo0 = pd.read_csv('hit_times_M0.csv')
datimodulo1 = pd.read_csv('hit_times_M1.csv')
datimodulo2 = pd.read_csv('hit_times_M2.csv')
datimodulo3 = pd.read_csv('hit_times_M3.csv')

#Istrogramma dei tempi per il modulo 0

timemodulo0 = datimodulo0['hit_time'].values
plt.hist(timemodulo0, bins = 45)
plt.ylabel('$Events$')
plt.grid(True)
plt.show()

#Istogramma delle differenze dei tempi fra Hit consecutivi del modulo 0

deltat = np.diff(timemodulo0)
mask0 = deltat > 0.0
logdt = np.log10(deltat[mask0])
plt.hist(logdt, bins = 100)
plt.xlabel('$\Delta$time')
plt.ylabel('$Events$')
plt.grid(True)
plt.show()

###PASSO 3###

#Definizione di una funzione che crea un array di reco.Hit

def arrrecohit(datimodulo):
    arrRHit = np.array([])
    for i in range(len(datimodulo['hit_time'])):
        arrRHit = np.append(arrRHit, rc.Hit(datimodulo['mod_id'][i], datimodulo['det_id'][i], datimodulo['hit_time'][i]))
    return arrRHit

#Creo un array di reco.Hit per ogni modulo (4), richimando la funzione arrrechit per ogni modulo

arrRH0 = arrrecohit(datimodulo0)
arrRH1 = arrrecohit(datimodulo1)
arrRH2 = arrrecohit(datimodulo2)
arrRH3 = arrrecohit(datimodulo3)

#Fondo tutti e 4 gli array in uno unico

arrRH = np.array([])
arrRH = np.append(arrRH, arrRH0)
arrRH = np.append(arrRH, arrRH1)
arrRH = np.append(arrRH, arrRH2)
arrRH = np.append(arrRH, arrRH3)

#Utilizzo il metodo numpy.sort per ordinare cronologicamente l'array di tutti gli Hit

sortarrRH = np.sort(arrRH)

#Calcolo i deltat per Hit consecutivi

arrRHdeltat = np.diff(sortarrRH)
arrRHdeltat = arrRHdeltat.astype(int)
mask0 = arrRHdeltat > 0.0
loghitdt = np.log10(arrRHdeltat[mask0])

#Creo l'istogramma per dt di Hit consecutivi

plt.hist(loghitdt, 60)
plt.xlabel('$log_10$$\Delta$time')
plt.ylabel('$Events$')
#plt.xscale('log')
plt.grid(True)
plt.show()

###PASSO 4###

#
