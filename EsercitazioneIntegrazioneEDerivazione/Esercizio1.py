import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Lettura file 

df_fromfile = pd.read_csv('vel_vs_time.csv')
#df_fromfile

#Creazione grafico velocita in funzione del tempo

ax = df_fromfile['t']

ay = df_fromfile['v']


plt.plot(ax,ay)
plt.xlabel('Time')
plt.ylabel('Space')

plt.show()
