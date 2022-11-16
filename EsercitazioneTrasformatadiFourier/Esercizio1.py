
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import fft

#Lettura dei tre file

signal1 = pd.read_csv('data_sample1.csv')
signal2 = pd.read_csv('data_sample2.csv')
signal3 = pd.read_csv('data_sample3.csv')

print(len(signal1))
print(len(signal2))
print(len(signal3))

#Grafico dei 3 signali in ingresso

plt.plot(signal1['time'] , signal1['meas'] , 'o', label = 'Signal 1', color = 'darkred')
plt.plot(signal2['time'] , signal2['meas'] , 'v', label='Signal 2', color='gold' )
plt.plot(signal3['time'] , signal3['meas'] , 's', label='Signal 3', color='pink' )
plt.xlabel('T [s]')
plt.ylabel('Signal')
plt.legend()
plt.show()

#Calcolo le trasfomate di Fourier per i 3 segnali e le loro frequenze


fftsignal1 = sc.fft.rfft(signal1.values)
print(fftsignal1)
fftsignal2 = sc.fft.rfft(signal2.values)
fftsignal3 = sc.fft.rfft(signal3.values)

freqsignal1 = sc.fft.rfftfreq(len(signal1)) # d = 1
freqsignal2 = sc.fft.rfftfreq(len(signal2)) # d = 1
freqsignal3 = sc.fft.rfftfreq(len(signal3)) # d = 1

print(len(freqsignal1))

#Grafico (primo segnale) dello spettro di potenza


plt.plot(np.absolute(fftsignal1[:fftsignal1.size//2]), 'o', markersize=4)
plt.xscale('log')
plt.yscale('log')
plt.plot()
