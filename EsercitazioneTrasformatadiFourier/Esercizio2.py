import pandas as pd
import matplotlib.pyplot as plt

#Lettura del file

CopernicusFile = pd.read_csv('copernicus_PG_selected.csv')

print(CopernicusFile)

#Grafico delle inquinanti in funzione del tempo

ax1 = plt.subplot(711)
plt.plot(CopernicusFile['date_old'].values, CopernicusFile['mean_co_ug/m3'].values, 'o', markersize = 4)
plt.title('Inquinanti atmosferiche in funzione del tempo')
plt.ylabel('Monossido di carbonio')
plt.tick_params('x', labelbottom = False)

ax2 = plt.subplot(712, sharex=ax1)
plt.plot(CopernicusFile['date_old'].values, CopernicusFile['mean_nh3_ug/m3'].values, 'o', markersize = 4)
plt.ylabel('Ammoniaca')
plt.tick_params('x', labelbottom = False)

ax3 = plt.subplot(713, sharex=ax1)
plt.plot(CopernicusFile['date_old'].values, CopernicusFile['mean_no2_ug/m3'].values, 'o', markersize = 4)
plt.ylabel('Biossido di azoto')
plt.xlabel('Data')
plt.show()

ax4 = plt.subplot(721)
plt.plot(CopernicusFile['date_old'].values, CopernicusFile['mean_o3_ug/m3'].values, 'o', markersize = 4)
plt.ylabel('Ozono')
plt.tick_params('x', labelbottom = False)
plt.show()

ax5 = plt.subplot(722, sharex=ax4)
plt.plot(CopernicusFile['date_old'].values, CopernicusFile['mean_pm10_ug/m3'].values, 'o', markersize = 4)
plt.ylabel('Particelle di diametro aerodinamico inferiore o uguale ai 10 µm')
plt.tick_params('x', labelbottom = False)
plt.show()

ax6 = plt.subplot(723, sharex=ax4)
plt.plot(CopernicusFile['date_old'].values, CopernicusFile['mean_pm2p5_ug/m3'].values, 'o', markersize = 4)
plt.ylabel('Particelle di diametro aerodinamico inferiore o uguale ai 2.5 µm')
plt.xlabel('Data')
plt.show()

ax7 = plt.subplot(731)
plt.plot(CopernicusFile['date_old'].values, CopernicusFile['mean_so2_ug/m3'].values, 'o', markersize = 4)
plt.xlabel('Data')
plt.ylabel('Anidride solforosa')
plt.show()