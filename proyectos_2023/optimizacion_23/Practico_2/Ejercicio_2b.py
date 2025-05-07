import numpy as np 
from Jacobiana import Jacobiana
from met_newton import met_newton
from met_new_est import met_newton_estacionario
from met_new_estm import met_newton_estacionario_m
from met_broyden import met_broyden_1
from met_broyden import met_broyden

# b)
def fun2(x):
    f1 = x[0]+x[1]-3
    f2 = x[0]**2 + x[1]**2 - 9 
    f3 = np.array([f1, f2])
    return f3

x_0 = np.array([1, 5])

#Metodo de newton
print('met newton')
met_newton(x_0, fun2, 1e-4, 10)
print('-------------')

#metodo de newton estacionario
print('met newton estacionario') 
met_newton_estacionario(x_0, fun2, 1e-4, 10)
print('-------------')

#metodo de newton estacionario
print('met newton estacionario con parametro m') 
met_newton_estacionario_m(x_0, fun2, 1e-4, 10, 3)
print('-------------')

# falta metodo de broyden
print('met de broyden') 
met_broyden(x_0, fun2, 1e-8, 20)