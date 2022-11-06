import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Lettura file 

df_fromfile = pd.read_csv('oscilloscope.csv')
<<<<<<< HEAD
print(type(df_fromfile))

=======
>>>>>>> 84b2dd7572971163d5835ed35ae91f98150bccb1
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

<<<<<<< HEAD
print(len(signal1))
=======
>>>>>>> 84b2dd7572971163d5835ed35ae91f98150bccb1

#Calcolo della derivata tramite il metodo della differenza centrale

#Definisco una funzione che implementa una versione della differenza centrale
<<<<<<< HEAD
# f'(i) =  [f(i+1)-f(i-1)] / [x(i+1)-x[i-1]]

def my_derivative(xx, yy):
    num = np.array([])
    den = np.array([])
    for i in range(len(yy)):
        print(i)
        if i == 0:
            num = np.append(num, yy[1] - yy[0])
        elif i == len(yy):
            print('.')
            num = np.append(num, yy[len(yy)] - yy[len(yy)-1])
        if i > 0 and i < len(yy) :
            num = np.append(num, yy[i+1] - yy[i-1])
        elif i == len(yy):
            num = np.append(num, yy[len(yy)] - yy[len(yy)-1])

    for l in range(len(xx)):
        if l == 0:
            den = np.append(den, xx[1] - xx[0])
        if l > 0 and l < len(xx) :
            den = np.append(den, xx[i+1] - xx[i-1])
        elif l == len(xx):
            den = np.append(den, xx[len(xx)] - xx[len(xx)-1])

    return num/den

derivatadiffcensegn1 = my_derivative(time, signal1)
print(derivatadiffcensegn1)
derivatadiffcensegn2 = my_derivative(time, signal2)

#Gafico delle due derivate con il metodo della differenza centrale 
=======

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
>>>>>>> 84b2dd7572971163d5835ed35ae91f98150bccb1

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
<<<<<<< HEAD

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
=======
>>>>>>> 84b2dd7572971163d5835ed35ae91f98150bccb1

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
