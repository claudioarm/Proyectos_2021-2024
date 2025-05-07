
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)

X, Y = np.meshgrid(x,y)

Z = (X-1)**2 * Y

fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection = '3d')

ax.plot_surface(X,Y, Z, cmap = 'viridis')

plt.show()

