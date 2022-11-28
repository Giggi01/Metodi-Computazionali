import matplotlib.pyplot as plt
import scipy as sc

#Hit or miss con funzione sinusoide

def probsin(x):
    fsin = (1/4)*sin(x/2)
    return fsin

xx = np.random.uniform(low = 0.0,  high = 2*math.pi, size = 1000)

probsin(xx)

plt(xx, probsin(xx))
plt.show()