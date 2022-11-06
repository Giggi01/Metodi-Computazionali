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