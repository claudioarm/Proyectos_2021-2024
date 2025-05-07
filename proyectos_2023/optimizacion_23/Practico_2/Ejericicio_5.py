import numpy as np 
from met_newton import met_newton 

# Ejercicio 5) a)

def camfun_a(x):
    f1 = 3*x[0] - np.cos(x[1])*x[2]- 0.5
    f2 = np.exp(-x[0]*x[1])+20*x[2]+ np.divide(10*np.pi - 3, 3)
    f3 = x[0]**2 - 81*(x[1]+ 0.1)**2 + np.sin(x[2]) + 1.06
    f4 = np.array([f1, f2, f3])
    return f4

x_0a = np.array([0.1, 0.1, -0.1])

#met_newton(x_0, camfun, 1e-8, 20)

# Ejercicio 5) b)

def camfun_b(x):
    f1 = 3*x[0] - np.cos(x[1])*x[2]- 0.5
    f2 = np.exp(-x[0]*x[1])+20*x[2]+ np.divide(10*np.pi - 3, 3)
    f3 = x[0]**2 - 625*x[1]**2 - np.divide(1,4)
    f4 = np.array([f1, f2, f3])
    return f4

x_0b = np.array([1, 1, -1])

met_newton(x_0b, camfun_b, 1e-8, 50)