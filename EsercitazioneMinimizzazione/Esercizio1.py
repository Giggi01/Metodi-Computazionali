import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import optimize


def esercizio1():

    #Definisco una funzione lognormale

    def lognormale(xx, sigma, mu, h):
             lognorm = ((h)*(math.e)**(-((np.log(xx)-mu)**2)/(2*sigma**2)))/(xx**sigma**(2*math.pi)**(1/2))
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
    plt.errorbar(x, y, yerr = erry, fmt = 'o', ecolor = 'blue')
    plt.xlabel('X')
    plt.xscale('log')
    plt.ylabel('Y')
    plt.show()

    #Fit per trovare i parametri
    
    
    pstart = np.array([209, 120])

    params, params_covariance, params_h = optimize.curve_fit(lognormale, x, y , pstart, sigma = erry, absolute_sigma = True)

    #Controllo risultato fit

    yottimizzata = lognormale(x, params[0], params[1], pstart)
    figure = plt.figure()
    figure.suptitle('Grafico con curva di approssimazione dei dati', fontsize = 20)
    plt.errorbar(x, y, yerr = erry, color = 'royalblue', fmt = 'o', label = 'Dati')
    plt.xscale('log')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(x, yottimizzata, color = 'darkorange', label = 'Fit Dati')
    plt.legend()
    plt.show()
    print('Params: ', params)
    print('Params_Cov: ' , params_covariance)
    print('Errori params: ', np.sqrt(params_covariance.diagonal()))

    


if __name__ == "__main__":
    esercizio1()
