import numpy as np
import math
from met_newton import met_newton
math.log(math.e)

def fun_nlineal(z):

    n = 4
    x_datos = np.array([2.4, 3.8, 4.75, 21.6])
    y_datos = np.array([31.8, 31.5, 31.2, 30.2])

    w = np.zeros(n)
    for i in range(n):
        w[i] = math.log(y_datos[i])
    
    # primera ecuación
    f1 = 0
    cnt_1 = 0
    for i in range(n):
        cnt_1 = cnt_1 + np.divide(1, (x_datos[i] - z[1])**(2*z[2]))
        f1 = f1 + np.divide(w[i]*y_datos[i], (x_datos[i] - z[1])**(z[2]))
    
    fun_a = f1/cnt_1 - z[0]

    # segunda ecuacion

    f2 = 0
    cnt_2 = 0
    for i in range(n):
        cnt_2 = cnt_2 + np.divide(1, (x_datos[i] - z[1])**(2*z[2]+1))

        f2 = f2 + np.divide(w[i]*y_datos[i], (x_datos[i] - z[1])**(z[2]+1))

    fun_b = f1*cnt_2 - f2*cnt_1

    # tercera ecuación

    f3 = 0
    cnt_3 = 0
    for i in range(n):
        cnt_3 = cnt_3 + np.divide(math.log(x_datos[i] - z[1]), (x_datos[i] - z[1])**(2*z[2]))

        f3 = f3 + np.divide(w[i]*y_datos[i]*math.log(x_datos[i] - z[1]), (x_datos[i] - z[1])**(z[2]))
    
    fun_c = f1*cnt_3 - f3*cnt_1


    return np.array([fun_a, fun_b, fun_c])

x_0 = np.array([0, 0, 0])

print(met_newton(x_0, fun_nlineal, np.infty, 1e-2, 10, sol1= False, sol2=True))


 


