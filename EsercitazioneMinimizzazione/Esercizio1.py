import pandas as pd
import matplotlib.pyplot as plt

letturafile = pd.read_csv('fit_data.csv')

#Grafico dei file (x-y)

ax = letturafile['x']

ay = letturafile['y']

fig = plt.figure()
plt.plot(ax, ay ,'o-', color = 'limegreen', label = 'Y')
plt.xlabel('X')
plt.ylabel('Y')
fig.suptitle('Grafico X-Y', fontsize = 20)
plt.legend()
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import optimize


def esercizio1():

    #Definisco una funzione lognormale

    def lognormale(xx, sigma, mu, A):
             lognorm = (A)*((math.e)**(-((np.log(xx)-mu)**2)/(2*sigma**2)))/(xx**sigma**((2*math.pi)**(1/2)))
             return lognorm
         
    #Lettura del file

    letturafile = pd.read_csv('fit_data.csv')

    x = letturafile['x'].values
    y = letturafile['y'].values
    
    #Creo un array di logaritmi di x
    
    logaritmox = np.log(x)    

    #Creazione del grafico con asse logaritmico

    fig = plt.figure()
    plt.plot(x,y, 'o', color = 'limegreen', label = 'Y')
    plt.xlabel('X')
    plt.ylabel('Y')
    fig.suptitle('Grafico Y-log(x)', fontsize = 20)
    plt.xscale('log')
    plt.legend()
    plt.grid(True)
    plt.show()

    #Creazione del grafico con asse logaritmico con errore poissoniano su y

    #Definisco l'errore di y
    
    erry = np.sqrt(y)


    figure = plt.figure()
    figure.suptitle('Grafico Y-log(x) con errore', fontsize = 20)
    plt.errorbar(x, y, yerr = erry, fmt = 'o', ecolor = 'blue', label = 'Y')
    plt.xlabel('X')
    plt.xscale('log')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

    #Fit per trovare i parametri , calcolo del chi-quadrato e dei gradi di liberta
    
    params, params_covariance = optimize.curve_fit(f = lognormale, xdata = x, ydata = y , sigma = erry, absolute_sigma = True, maxfev = 5000)
    yfit = lognormale(x, params[0], params[1], params[2])
    chi2 = np.sum((yfit- y)**2/y)
    ndof = len(x)-len(params)

    #Controllo risultato fit

    yottimizzata = lognormale(x, params[0], params[1], params[2])
    figure = plt.figure()
    figure.suptitle('Fitted Graphic', fontsize = 20)
    plt.errorbar(x, y, yerr = erry, color = 'royalblue', fmt = 'o', label = 'Dati')
    plt.xscale('log')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(x, yottimizzata, color = 'darkorange', label = 'Fit Dati')
    plt.legend()
    plt.grid(True)
    plt.show()
    print('Sigma   = {:3.0f} +- {:1.0f}'.format(params[0], math.sqrt(params_covariance[0,0])) ) 
    print('Mu = {:3.1f} +- {:1.1f}'.format(params[1], math.sqrt(params_covariance[1,1])) )
    print('A = {:3.2f} +- {:1.2f}'.format(params[2], math.sqrt(params_covariance[2,2])) )
    print('Chi 2 = {:3.3f}'.format(chi2) )
    print('Gradi di liberta = {:3.3f} '.format(ndof) )
    print('Chi2 / Gradi di liberta = {:3.3f} '.format(chi2/ndof) )


    


if __name__ == "__main__":
    esercizio1()
