
'''Paquetes necesarios a usar'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

'''Colores a usar similares a los de visualPDE'''

Vegcolors = [(0.80, 0.58, 0.34), (0.97, 0.89, 0.62), (0.51, 0.63, 0.27),
             (0.38, 0.51, 0.22), (0.31, 0.40, 0.21), (0.21, 0.32, 0.20)]
VegMap = LinearSegmentedColormap.from_list('AridVeg', Vegcolors, N=100)

'''Esquema Forward de la primera derivada respecto de x'''
def Dx(U, delta_x):

    U_right = np.roll(U, -1, axis=1)  # U[i+1,j] a derecha de U[i, j] ---> j esta fijo
    U_central = U                       # U[i,j]  centrada
    Dx_U = (U_right-U_central)/delta_x           # (U[i+1,j]-U[i,j])/delta_x
    return  Dx_U


'''Esquema Central de la segunda derivada respecto de x e y'''
def DDxy(U, delta_x, delta_y):

    U_left = np.roll(U, 1, axis=1)  # U[i-1,j] a izquierda de U[i, j] ---> j esta fijo

    U_right = np.roll(U, -1, axis=1) # U[i+1,j] a derecha de U[i, j] ---> j esta fijo

    U_top = np.roll(U, 1, axis=0) # U[i,j+1] arriba de U[i,j] ---> i esta fijo

    U_bottom = np.roll(U, -1, axis=0) # U[i,j+1] debajo de U[i,j] ---> i esta fijo

    U_central = U     # U[i,j]  centrada

    DDxy_U = (U_left - 2 * U_central + U_right)/(delta_x**2) + (U_bottom -2*U_central +U_top)/(delta_y**2) # (U[i-1,j] - 2 * U[i,j] + U[i-1,j])/(dx**2) + (U[i,j-1]- 2 * U[i,j]  + U[i,j+1])/(dy**2)

    return DDxy_U


'''Parametros'''

a        = 1.5     # Tasa de lluvia
m        = 0.45    # Tasa de mortalidad
v        = 60.0   # La advección descendente de w
dw       = 1.0     # La constante de difusion w
dn       = 1.0     # La constante de difusion n


'''Klausmeier model'''

def simulation_klausmeier(a, m, v):

  num_nodos = 100 # Cantidad de nodos para x e y (malla en 2D)
  long_xy = 100.0 # Longitud del dominio (cuadrado)
  delta_x = long_xy/num_nodos # paso espacial
  delta_y = long_xy/num_nodos # paso espacial

  #Condiciones iniciales
  W_0 = np.zeros((num_nodos, num_nodos))+1.0
  N_0 = (np.random.rand(num_nodos, num_nodos)<0.05)*1.0 + 1.0

  time_max = 50.0 # Tiempo maximo
  delta_t = 0.001  # paso de tiempo
  num_plot = 17    # numeros de plots a graficar

  # Generamos los frames para plotear las simulaciones
  fig, axes = plt.subplots(4, 4, figsize=(12, 12))

  # Numero maximo de iteraciones
  iter_max = int(time_max / delta_t)

  # Vamos a plotear algunos frame entonces definimos un paso de plot
  step_plot = iter_max // num_plot

  # Empezamos a iterar
  for idx in range(int(time_max / delta_t)):

    # Metodo de Euler
    W = W_0 + delta_t * ( a - W_0 - W_0*N_0*N_0 + v*Dx(W_0, delta_x) + dw*DDxy(W_0, delta_x, delta_y))
    N = N_0 + delta_t * ( W_0*N_0*N_0 - m*N_0 + dn * DDxy(N_0, delta_x, delta_y))

    # Rescribimos para la siguiente iteracion
    W_0 = W
    N_0 = N

    # Si se satisface las condiciones ploteamos
    if idx % step_plot == 0 and idx < ((num_plot-1) * step_plot):
      ax = axes.flat[idx // step_plot]
      ax.imshow(N, cmap=VegMap,interpolation='bilinear', extent=[0, 1, 0, 1])
      ax.set_axis_off()
      ax.set_title(f'$t={idx * delta_t:.2f} s$')
  
  plt.tight_layout()
  plt.show()

simulation_klausmeier(a, m, v)