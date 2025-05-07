import numpy as np 
from Jacobiana import Jacobiana
from met_newton import met_newton
from met_new_est import met_newton_estacionario
from met_new_estm import met_newton_estacionario_m
from met_broyden import met_broyden

# e)

def fun5(x):
    f = np.zeros(10)
    f[0] = (3-2*x[0])*x[0] - 2*x[1] + 1
    for i in range(1,8):
        f[i] = (3-2*x[i])*x[i] -x[i-1]- 2*x[i+1] + 1
    f[9] = (3-2*x[9])*x[9] - 2*x[8] + 1
    return f

x_0 = -np.ones(10)

#Metodo de newton
print('met newton')
met_newton(x_0, fun5, 1e-2, 10)
print('-------------')

#metodo de newton estacionario
print('met newton estacionario') 
met_newton_estacionario(x_0, fun5, 1e-2, 10)
print('-------------')

#metodo de newton estacionario
print('met newton estacionario') 
met_newton_estacionario_m(x_0, fun5, 1e-2, 10, 2)
print('-------------')

# falta metodo de broyden