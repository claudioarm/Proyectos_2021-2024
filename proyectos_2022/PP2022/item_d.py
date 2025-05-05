from random import uniform
import numpy as np 
import matplotlib.pyplot as plt 
  
n = 10**4
 
x_uniform = np.random.uniform(0, 1, n)

y_uniform = np.random.uniform(0, 1, n)

plt.plot(x_uniform, y_uniform, '*')
plt.xlabel('numeros aleatorios en x')
plt.ylabel('numeros aleatorios en y')
plt.title('nube de puntos')
 
plt.show()



plt.hist2d(x_uniform, y_uniform, bins = (10,10))
  
plt.xlabel('Valores x')
plt.ylabel('Valores y')
plt.title('Histograma Bidimensional')
plt.colorbar()
plt.show()