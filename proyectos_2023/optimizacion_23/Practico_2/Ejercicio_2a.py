import numpy as np 
from Jacobiana import Jacobiana
from met_newton import met_newton
from met_new_est import met_newton_estacionario
from met_new_estm import met_newton_estacionario_m
from met_broyden import met_broyden

# a)
def fun1(x):
    f1 = (x[0]+3)*(x[1]**3 - 7)+18
    f2 = np.sin(x[1] * np.exp(x[0])-1)
    f3 = np.array([float(f1), float(f2)])
    return f3

x_0 = np.array([-0.5, 1.4])

x_str = np.array([0, 1])

#Metodo de newton
print('met newton')
x_sol1 = met_newton(x_0, fun1, 2, 1e-8, 10, sol1 = False, sol2=True)
n = len(x_sol1)
print('| iteraciones | error | tasa de convergencia |')
print('-----------------------------------------------')
for i in range(n-1):
    print(f'| {i} | {np.linalg.norm(x_sol1[i] - x_str, 2)}| {np.linalg.norm(x_sol1[i+1] - x_str, 2)/np.linalg.norm(x_sol1[i] - x_str, 2)} |')
    print('-----------------------------------------------')

#metodo de newton estacionario
#print('met newton estacionario') 
#met_newton_estacionario(x_0, fun1, 1e-4, 10)
#print('-------------')

#metodo de newton estacionario
#print('met newton estacionario con parametro m') 
#met_newton_estacionario_m(x_0, fun1, 1e-4, 10, 3)
#print('-------------')

# falta metodo de broyden

#met_broyden(x_0, fun1, 1e-8, 50)