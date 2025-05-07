import numpy as np 
from Jacobiana import Jacobiana
from met_newton import met_newton
from met_new_est import met_newton_estacionario
from met_new_estm import met_newton_estacionario_m
from met_broyden import met_broyden_1
from met_broyden import met_broyden

# c)

def fun3(x):
    f1 = x[0]**2 + x[1]**2 - 2
    f2 = np.exp(x[0]-1) + x[1]**3 - 2 
    f3 = np.array([f1, f2])
    return f3

x_0 = np.array([1.5, 2])

#Metodo de newton
print('met newton')
met_newton(x_0, fun3, 1e-5, 20)
print('-------------')

#metodo de newton estacionario
print('met newton estacionario') 
met_newton_estacionario(x_0, fun3, 1e-5, 20)
print('-------------')

#metodo de newton estacionario
print('met newton estacionario') 
met_newton_estacionario_m(x_0, fun3, 1e-5, 20, 4)
print('-------------')

# falta metodo de broyden
met_broyden(x_0, fun3, 1e-4, 50)