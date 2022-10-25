import numpy as np
import pandas as pd

# Creazione Dati

giorni = np.arange(1, 31, 1)
temperature = (np.random.normal(loc=25.5, scale=7.6, size=30).astype(float))
temperatureerr = 7.6*np.ones(30)
pioggiamm = (np.random.normal(loc=2.3, scale=0.6, size=30).astype(float))
pioggiammerr = 0.6*np.ones(30)

# Creazione Tabelle

line1 = giorni
line2 = temperature
line3 = temperatureerr
line4 = pioggiamm
line5 = pioggiammerr

Tabella = pd.DataFrame(columns=['Giorno', 'Temperatura',
                       'Incertezza Tempertura', 'Pioggia', 'Incertezza Pioggia'])
Tabella['Giorno'] = line1
Tabella['Temperatura'] = line2
Tabella['Incertezza Tempertura'] = line3
Tabella['Pioggia'] = line4
Tabella['Incertezza Pioggia'] = line5

# Salvataggio Tabella Pandas

Tabella.to_csv('Tabella.csv', index=False)
