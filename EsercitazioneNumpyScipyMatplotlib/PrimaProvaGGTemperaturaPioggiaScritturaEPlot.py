import pandas as pd
import matplotlib.pyplot as plt

# Lettura del file e trascrizione

df_fromfile = pd.read_csv('Tabella.csv')
print(df_fromfile)

# Creazione del grafico con temperatura e pioggia in funzione del giorno senza errori nello stesso grafico

ascissa = df_fromfile['Giorno']
coordinata1 = df_fromfile['Temperatura']
coordinata2 = df_fromfile['Pioggia']
plt.plot(ascissa, coordinata1, 's-', color='limegreen', label='Temperatura')
plt.plot(ascissa, coordinata2, '*',  color='red', label='Pioggia')
plt.xlabel('Giorno')
plt.ylabel('Temperatura e Pioggia')
plt.legend()
# plt.show()

# Creazione del grafico con temperatura e pioggia in funzione del giorno con errori in 2 grafici diversi

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
#ax[0].plot(ascissa, coordinata1, 's-', color='limegreen')
ax[0].set_title('Grafico Temperatura-Giorni', fontsize=15, color='limegreen')
ax[1].set_title('Grafico Pioggia-Giorno', fontsize=15, color='red')
ax[0].set_xlabel('Giorno')
ax[0].set_ylabel('Temperatura')
ax[1].set_xlabel('Giorno')
ax[1].set_ylabel('Pioggia')
ax[0].tick_params(axis='x', labelsize=14)
ax[0].tick_params(axis='y', labelsize=14)
ax[0].errorbar(ascissa, coordinata1,
               yerr=df_fromfile['Incertezza Tempertura'], fmt='X-', color='limegreen', ecolor='blue')
ax[1].errorbar(ascissa, coordinata2,
               yerr=df_fromfile['Incertezza Pioggia'], fmt='*-', color='red', ecolor='blue')
# plt.show()

# Creazione grafico scatter pioggia-temperatura

xs = df_fromfile['Temperatura']
ysb = df_fromfile['Pioggia']
plt.scatter(xs, ysb, color='royalblue', s=32, label='mm di pioggia')
plt.xlabel('Temperatura', fontsize=16)
plt.ylabel('Pioggia', fontsize=16)
plt.legend(fontsize=14)
# plt.show()
