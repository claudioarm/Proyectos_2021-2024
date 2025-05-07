import numpy as np 
from Jacobiana import Jacobiana
from met_newton import met_newton
from met_new_est import met_newton_estacionario
from met_new_estm import met_newton_estacionario_m
from met_broyden import met_broyden_1
from met_broyden import met_broyden
# d)

def fun4(x):
    f1 = 10*(x[1] + x[0]**2)
    f2 = 1 - x[0] 
    f3 = np.array([f1, f2])
    return f3

x_0 = np.array([-1.2, 1])

#Metodo de newton
print('met newton')
met_newton(x_0, fun4, 1e-2, 10)
print('-------------')

#metodo de newton estacionario
print('met newton estacionario') 
met_newton_estacionario(x_0, fun4, 1e-2, 10)
print('-------------')

#metodo de newton estacionario
print('met newton estacionario') 
met_newton_estacionario_m(x_0, fun4, 1e-2, 10, 2)
print('-------------')

# falta metodo de broyden

met_broyden(x_0, fun4, 1e-8, 50)

#llega al minimo en (1, -1)