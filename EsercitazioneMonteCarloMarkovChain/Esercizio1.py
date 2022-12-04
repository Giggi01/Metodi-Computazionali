import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Lettura del file

dati = pd.read_csv('absorption_line.csv')

#Grafico dei dati 

plt.erorrbar(dati['E'].values, dati['f'].values, xerr = dati['ferr'].values, fmt = 'o')
plt.xlabel('E')
plt.ylabel('f(E)')
plt.show()