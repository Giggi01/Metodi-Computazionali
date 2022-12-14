import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import reco as rc

#Definizione di una funzione che crea un array di reco.Hit

def arrrecohit(datimodulo):
    arrRHit = np.array([])
    for i in range(len(datimodulo['hit_time'])):
        arrRHit = np.append(arrRHit, rc.Hit(datimodulo['mod_id'][i], datimodulo['det_id'][i], datimodulo['hit_time'][i]))
    return arrRHit

###PASSO 1###

#Lettura di tutti i file (moduli)

datimodulo0 = pd.read_csv('hit_times_M0.csv')
datimodulo1 = pd.read_csv('hit_times_M1.csv')
datimodulo2 = pd.read_csv('hit_times_M2.csv')
datimodulo3 = pd.read_csv('hit_times_M3.csv')

#Istrogramma dei tempi per il modulo 0

timemodulo0 = datimodulo0['hit_time'].values
print((len(timemodulo0)))
plt.hist(timemodulo0, bins = 100)
plt.xlabel('$times$')
plt.ylabel('$Events$')
plt.show()

#Istogramma delle differenze dei tempi fra Hit consecutivi del modulo 0

deltat = np.diff(timemodulo0)
mask0 = deltat > 0
logdt = np.log(deltat[mask0])
plt.hist(logdt, bins = 100)
plt.xlabel('$\Delta$time')
plt.ylabel('$Events$')
plt.show()

###PASSO 3###

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

#Faccio un bubble sort per mettere in ordine cronologico tutti gli array reco.Hit


