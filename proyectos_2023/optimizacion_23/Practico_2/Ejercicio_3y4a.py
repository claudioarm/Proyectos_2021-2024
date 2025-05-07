import numpy as np 
import matplotlib.pyplot as plt
from met_new_estm import met_newton_estacionario_m

#Graficar las curvas de F(x)=0 

def fun1(x, y):
    z = 4 * x**2 - 20*x + np.divide(y**2, 4) +8
    return z


def fun2(x, y):
    z = 0.5 * x*y**2 + 2*x - 5 * y + 8    
    return z

x = np.linspace(-10, 10, 1000)
y = np.linspace(-5, 10, 1000)

X, Y = np.meshgrid(x,y)

z_1 = fun1(X,Y)
z_2 = fun2(X,Y)

fig, ax1 = plt.subplots()

cnt1 = ax1.contour(X, Y, z_1, levels = 50)
fig.colorbar(cnt1)
ax1.set_xlabel('x')
ax1.set_xlabel('y')
ax1.set_title('curvas de nivel de f_1')


fig2, ax2 = plt.subplots()
cnt2 = ax2.contour(X, Y, z_2, levels = 50)
fig2.colorbar(cnt2)
ax2.set_xlabel('x')
ax2.set_xlabel('y')
ax2.set_title('curvas de nivel de f_2')

plt.show()



#Ejercicio 4)

x_0 = np.array([-1.05, 1.0])
x_01 = np.array([-0.36, 1.37])
x_02 = np.array([1.25, 3.86])


def FUN(x):
    f1 = fun1(x[0], x[1])
    f2 = fun2(x[0], x[1])
    f3 = np.array([f1, f2])
    return f3

#met_newton_estacionario_m(x_01, FUN, 1e-4, 10, 3)
