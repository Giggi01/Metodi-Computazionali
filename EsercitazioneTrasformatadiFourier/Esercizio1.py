
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

plt.plot(signal1['time'] , signal1['meas'] , 'o', label = 'Signal 1', color = 'blue')
plt.plot(signal2['time'] , signal2['meas'] , 'v', label='Signal 2', color='darkorange')
plt.plot(signal3['time'] , signal3['meas'] , 's', label='Signal 3', color='green')
plt.xlabel('T [s]')
plt.ylabel('Signal')
plt.legend()
plt.show()

#Calcolo le trasfomate di Fourier per i 3 segnali e le loro frequenze


fftsignal1 = fft.rfft(signal1['meas'].values)
fftsignal2 = fft.rfft(signal2['meas'].values)
fftsignal3 = fft.rfft(signal3['meas'].values)

nyquist = 0.5
freqsignal1 = nyquist*fft.rfftfreq(fftsignal1.size) #d = 1
freqsignal2 = nyquist*fft.rfftfreq(fftsignal2.size) #d = 1
freqsignal3 = nyquist*fft.rfftfreq(fftsignal3.size) #d = 1



#Grafico dello spettro di potenza 

plt.plot(np.absolute(fftsignal1[:fftsignal1.size//2])**2, 'o', markersize=4)
plt.plot(np.absolute(fftsignal2[:fftsignal2.size//2])**2, 'o', markersize=4)
plt.plot(np.absolute(fftsignal3[:fftsignal3.size//2])**2, 'o', markersize=4)
plt.xlabel('Indice')
plt.ylabel('Spettro di Potenza')
plt.xscale('log')
plt.yscale('log')
plt.show()

#Grafico dello spettro di potenza in funzione della frequenza

ax1 = plt.subplot(311)
plt.plot(freqsignal1[:int(fftsignal1.size/2)], np.absolute(fftsignal1[:int(fftsignal1.size/2)])**2, 'o', markersize = 4, color = 'blue')
plt.xscale('log')
plt.yscale('log')
plt.title('Spettro di potenza in funzione della frequenza')
plt.ylabel('$|c_k|^2$')
plt.tick_params('x', labelbottom = False)

ax2 = plt.subplot(312, sharex=ax1)
plt.plot(freqsignal2[:int(fftsignal2.size/2)], np.absolute(fftsignal2[:int(fftsignal2.size/2)])**2, 'o', markersize = 4, color = 'darkorange')
plt.xscale('log')
plt.yscale('log')
plt.ylabel('$|c_k|^2$')
plt.tick_params('x', labelbottom = False)

ax3 = plt.subplot(313, sharex=ax1)
plt.plot(freqsignal3[:int(fftsignal3.size/2)], np.absolute(fftsignal3[:int(fftsignal3.size/2)])**2, 'o', markersize = 4, color = 'green')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenza [Hz]')
plt.ylabel('$|c_k|^2$')
plt.show()

#Calcolo del fit
    
params1, params_covariance1 = optimize.curve_fit(f = funcnoise, xdata = freqsignal1[1:int(fftsignal1.size/2)] , ydata =  np.absolute(fftsignal1[1:int(fftsignal1.size/2)])**2, maxfev = 5000)
yfit1 = funcnoise(freqsignal1[1:int(fftsignal1.size/2)], params1[0], params1[1])

params2, params_covariance2 = optimize.curve_fit(f = funcnoise, xdata = freqsignal2[1:int(fftsignal2.size/2)] , ydata =  np.absolute(fftsignal2[1:int(fftsignal2.size/2)])**2, maxfev = 5000)
yfit2 = funcnoise(freqsignal2[1:int(fftsignal2.size/2)], params2[0], params2[1])

params3, params_covariance3 = optimize.curve_fit(f = funcnoise, xdata = freqsignal3[5:int(fftsignal3.size/2)] , ydata =  np.absolute(fftsignal3[5:int(fftsignal3.size/2)])**2, maxfev = 5000)
yfit3 = funcnoise(freqsignal3[1:int(fftsignal3.size/2)], params3[0], params3[1])

#Grafico del fitt dei tre segnali e identificazione del tipo di segnale

plt.plot(freqsignal1[1:int(fftsignal1.size/2)], np.absolute(fftsignal1[1:int(fftsignal1.size/2)])**2, 'o', color = 'grey')
plt.plot(freqsignal1[1:int(fftsignal1.size/2)], yfit1, '-', color = 'blue')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenza [Hz]')
plt.ylabel('$|c_k|^2$')
plt.show()
print('Beta : ', params1[0])

plt.plot(freqsignal2[1:int(fftsignal2.size/2)], np.absolute(fftsignal2[1:int(fftsignal2.size/2)])**2, 'o', color = 'pink')
plt.plot(freqsignal2[1:int(fftsignal2.size/2)], yfit2, '-', color = 'blue')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenza [Hz]')
plt.ylabel('$|c_k|^2$')
plt.show()
print('Beta : ', params2[0])

plt.plot(freqsignal3[1:int(fftsignal3.size/2)], np.absolute(fftsignal3[1:int(fftsignal3.size/2)])**2, 'o', color = 'red')
plt.plot(freqsignal3[1:int(fftsignal3.size/2)], yfit3, '-', color = 'blue')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenza [Hz]')
plt.ylabel('$|c_k|^2$')
plt.show()
print('Beta : ', params3[0])