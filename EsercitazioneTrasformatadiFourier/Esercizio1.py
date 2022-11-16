
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import fft
from scipy import optimize

#Definisco la funzione che determina la relazione tra spettro di potenza e frequenza

def funcnoise(f, beta, A):
    spettro = A*(1/f**(beta))
    return spettro


#Lettura dei tre file

signal1 = pd.read_csv('data_sample1.csv')
signal2 = pd.read_csv('data_sample2.csv')
signal3 = pd.read_csv('data_sample3.csv')

#Grafico dei 3 signali in ingresso

plt.plot(signal1['time'] , signal1['meas'] , 'o', label = 'Signal 1', color = 'green')
plt.plot(signal2['time'] , signal2['meas'] , 'v', label='Signal 2', color='gold')
plt.plot(signal3['time'] , signal3['meas'] , 's', label='Signal 3', color='blue')
plt.xlabel('T [s]')
plt.ylabel('Signal')
plt.legend()
plt.show()

#Calcolo le trasfomate di Fourier per i 3 segnali e le loro frequenze


fftsignal1 = fft.rfft(signal1['meas'].values)
print(len(fftsignal1))
fftsignal2 = fft.rfft(signal2['meas'].values)
fftsignal3 = fft.rfft(signal3['meas'].values)

snyquist = 0.5
freqsignal1 = snyquist*fft.rfftfreq(fftsignal1.size) #d = 1
print(len(freqsignal1))
freqsignal2 = snyquist*fft.rfftfreq(fftsignal2.size) #d = 1
freqsignal3= snyquist*fft.rfftfreq(fftsignal2.size) #d = 1



#Grafico dello spettro di potenza 

plt.plot(np.absolute(fftsignal1[:fftsignal1.size//2])**2, 'o', markersize=4)
plt.plot(np.absolute(fftsignal2[:fftsignal2.size//2])**2, 'o', markersize=4)
plt.plot(np.absolute(fftsignal3[:fftsignal3.size//2])**2, 'o', markersize=4)
plt.xlabel('Indice')
plt.ylabel('Spettro di Potenza')
plt.xscale('log')
plt.yscale('log')
plt.show()

#Grafico dello spettro di potenza della prima in funzione della frequenza

plt.plot(freqsignal1[:int(fftsignal1.size/2)], np.absolute(fftsignal1[:int(fftsignal1.size/2)])**2, 'o', markersize = 4, color = 'blue')
plt.xlabel('Frequenza [Hz]')
plt.ylabel('Spettro di potenza $|c_k|^2$')
plt.xscale('log')
plt.yscale('log')
plt.show()

#Grafico dello spettro di potenza del secondo segnale in funzione della frequenza

plt.plot(freqsignal2[:int(fftsignal2.size/2)], np.absolute(fftsignal2[:int(fftsignal2.size/2)])**2, 'o', markersize = 4, color = 'orange')
plt.xlabel('Frequenza [Hz]')
plt.ylabel('Spettro di potenza $|c_k|^2$')
plt.xscale('log')
plt.yscale('log')
plt.show()

#Grafico dello spettro di potenza del terzo segnale in funzione della frequenza

plt.plot(freqsignal3[:int(fftsignal3.size/2)], np.absolute(fftsignal3[:int(fftsignal3.size/2)])**2, 'o', markersize = 4, color = 'green')
plt.xlabel('Frequenza [Hz]')
plt.ylabel('Spettro di potenza $|c_k|^2$')
plt.xscale('log')
plt.yscale('log')
plt.show()

#Fit e grafico fittato dello spettro di potenza del primo segnale
    
params, params_covariance = optimize.curve_fit(f = funcnoise, xdata = freqsignal1[1:int(fftsignal1.size/2)] , ydata =  np.absolute(fftsignal1[1:int(fftsignal1.size/2)])**2, maxfev = 5000)
print(params[0], params[1])
yfit = funcnoise(freqsignal1[1:int(fftsignal1.size/2)], params[0], params[1])

plt.plot(freqsignal1[1:int(fftsignal1.size/2)], np.absolute(fftsignal1[1:int(fftsignal1.size/2)])**2, 'o', markersize = 4)
plt.plot(freqsignal1[1:int(fftsignal1.size/2)], yfit, '-', markersize = 4)
plt.xlabel('Frequenza [Hz]')
plt.ylabel('Spettro di potenza $|c_k|^2$')
plt.xscale('log')
plt.yscale('log')
plt.show()

