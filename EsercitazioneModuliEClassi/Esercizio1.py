import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import reco as rc

#Lettura del file (Modulo 0)

datimodulo0 = pd.read_csv('hit_times_M0.csv')

#Istrogramma dei tempi per il modulo 0

timemodulo0 = datimodulo0['hit_time'].values
print((len(timemodulo0)))
plt.hist(timemodulo0, bins = 100)
plt.xlabel('$times$')
plt.show()

#Istogramma delle differenze dei tempi fra Hit consecutivi del modulo 0

deltat = np.diff(timemodulo0)
mask0 = deltat > 0
logdt = np.log(deltat[mask0])
plt.hist(logdt, bins = 100)
plt.xlabel('$\Delta$time')
plt.show()


