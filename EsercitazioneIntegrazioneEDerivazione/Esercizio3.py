import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Lettura file 

df_fromfile = pd.read_csv('oscilloscope.csv')
time = df_fromfile['time']
signal1 = df_fromfile['signal1']
signal2 = df_fromfile['signal2']

#Creazione grafico segnale 1

ax = time

ay = signal1

fig = plt.figure()
plt.plot(ax, ay ,'-', color = 'limegreen', label = 'Segnale 1')
plt.xlabel('Time')
plt.ylabel('Signal 1')
fig.suptitle('Grafico Segnale1-Tempo', fontsize = 20)
plt.legend()
plt.grid(True)
plt.show()

#Creazione grafico segnale 2

ax = time

ay = signal2

fig = plt.figure()
plt.plot(ax, ay ,'-', color = 'red', label = 'Segnale 2')
plt.xlabel('Time')
plt.ylabel('Signal 2')
fig.suptitle('Grafico Segnale2-Tempo', fontsize = 20)
plt.legend()
plt.grid(True)
plt.show()


#Calcolo della derivata tramite il metodo della differenza centrale

#Definisco una funzione che implementa una versione della differenza centrale

# f'(i) =  [f(i+nh)-f(i-nh)] / [x(i+nh)-x[i-nh]]

timearray = time.to_numpy()
signal1array = signal1.to_numpy()
signal2array = signal2.to_numpy()

def my_derivative(xx, yy, nh):
    dd = yy[nh:] - yy[:-nh]
    hh = xx[nh:] - xx[:-nh]
    for ih in range(int(nh/2)):
        dd = np.append(yy[nh-ih-1]-yy[0], dd)
        dd = np.append(dd, yy[-1]-yy[-(nh-ih)])
    
        hh = np.append(xx[nh-ih-1]-xx[0], hh)
        hh = np.append(hh, xx[-1]-xx[-(nh-ih)])
    
    return dd/hh

derivatadiffcensegn1 = my_derivative(timearray, signal1array, 20) #n=20
derivatadiffcensegn2 = my_derivative(timearray, signal2array, 20) #n=20


#Grafico delle due derivate con il metodo della differenza centrale 

print('Grafico delle derivate dei due seganli tramite il metodo della differenza centrale')

fig,ax = plt.subplots(1,2, figsize=(12,6) )

ax[0].plot(time, derivatadiffcensegn1, '-', color='limegreen')
ax[1].plot(time, derivatadiffcensegn2, '-',  color='red'  )

ax[0].set_title('Grafico Derivata Segnale1', fontsize=15, color='limegreen',)
ax[1].set_title('Grafico Derivata Segnale2', fontsize=15, color='red',)

ax[0].set_xlabel('Time')
ax[0].set_ylabel('Derivated Signal 1')

ax[1].set_xlabel('Time')
ax[1].set_ylabel('Derivated Signal 2')

ax[0].grid(True)
ax[1].grid(True)

plt.show()

#Calcolo della derivata tramite il metodo gradient di numpy

npgrad_sig1 = np.gradient(signal1, time)
npgrad_sig2 = np.gradient(signal2, time)

#Grafico delle due derivate dei segnali con il metodo numpy.gradient

print('Grafico delle derivate dei due seganli tramite il metodo numpy.gradient')

fig,ax = plt.subplots(1,2, figsize=(12,6) )

ax[0].plot(time, npgrad_sig1, '-', color='limegreen')
ax[1].plot(time, npgrad_sig2, '-',  color='red'  )

ax[0].set_title('Grafico Derivata Segnale1', fontsize=15, color='limegreen',)
ax[1].set_title('Grafico Derivata Segnale2', fontsize=15, color='red',)

ax[0].set_xlabel('Time')
ax[0].set_ylabel('Derivated Signal 1')

ax[1].set_xlabel('Time')
ax[1].set_ylabel('Derivated Signal 2')

ax[0].grid(True)
ax[1].grid(True)

plt.show()