import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Lettura file 

df_fromfile = pd.read_csv('oscilloscope.csv')
#df_fromfile

#Creazione grafico segnale 1

ax = df_fromfile['time']

ay = df_fromfile['signal1']

fig = plt.figure()
plt.plot(ax, ay ,'o-', color = 'limegreen', label = 'Segnale 1')
plt.xlabel('Time')
plt.ylabel('Signal 1')
fig.suptitle('Grafico Segnale1-Tempo', fontsize = 20)
plt.legend()
plt.grid(True)
plt.show()

#Creazione grafico segnale 2

ax = df_fromfile['time']

ay = df_fromfile['signal2']

fig = plt.figure()
plt.plot(ax, ay ,'s-', color = 'red', label = 'Segnale 2')
plt.xlabel('Time')
plt.ylabel('Signal 2')
fig.suptitle('Grafico Segnale2-Tempo', fontsize = 20)
plt.legend()
plt.grid(True)
plt.show()

#Calcolo della derivata tramite il metodo gradient di numpy

time = df_fromfile['time']
signal1 = df_fromfile['signal1']
signal2 = df_fromfile['signal2']

npgrad_sig1 = np.gradient(signal1, time)
npgrad_sig2 = np.gradient(signal2, time)

#Grafico delle due derivate dei segnali

fig,ax = plt.subplots(1,2, figsize=(12,6) )

ax[0].plot(time, npgrad_sig1, 's-', color='limegreen')
ax[1].plot(time, npgrad_sig2, '*',  color='red'  )

ax[0].set_title('Grafico Derivata Segnale1', fontsize=15, color='limegreen',)
ax[1].set_title('Grafico Derivata Segnale2', fontsize=15, color='red',)

ax[0].set_xlabel('Time')
ax[0].set_ylabel('Derivated Signal 1')

ax[1].set_xlabel('Time')
ax[1].set_ylabel('Derivated Signal 2')

ax[0].grid(True)
ax[1].grid(True)

#ax[0].tick_params(axis='x', labelsize=14)
#ax[0].tick_params(axis='y', labelsize=14)

plt.show()