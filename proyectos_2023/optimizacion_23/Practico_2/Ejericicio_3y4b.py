import numpy as np 
import matplotlib.pyplot as plt
from met_newton import met_newton
#Graficar las curvas de F(x)=0 

def fun1(x, y):
    z = np.sin(4*np.pi*x*y)-2*y-x
    return z


def fun2(x, y):
    z = np.divide(4*np.pi - 1, 4*np.pi)*(np.exp(2*x) - np.exp(1)) + 4*np.exp(1)*y**2 - 2*np.exp(1)*x    
    return z

x = np.linspace(-np.pi/2, np.pi/2, 1000)
y = np.linspace(-np.pi/2, np.pi/2, 1000)

X, Y = np.meshgrid(x,y)

z_1 = fun1(X,Y)
z_2 = fun2(X,Y)

fig, ax1 = plt.subplots()

cnt1 = ax1.contour(X, Y, z_1, levels = 20)
fig.colorbar(cnt1)
ax1.set_xlabel('x')
ax1.set_xlabel('y')
ax1.set_title('curvas de nivel de f_1')

fig2, ax2 = plt.subplots()
cnt2 = ax2.contour(X, Y, z_2, levels = 20)
fig2.colorbar(cnt2)
ax2.set_xlabel('x')
ax2.set_xlabel('y')
ax2.set_title('curvas de nivel de f_2')

plt.show()

# Ejercicio 4) 

x_0 = np.array([-0.697, 0.071])
x_01 = np.array([0.127, -0.243])
x_02 = np.array([0.760, -0.337])


def FUN2(x):
    f1 = fun1(x[0], x[1])
    f2 = fun2(x[0], x[1])
    f3 = np.array([f1, f2])
    return f3

#met_newton(x_02, FUN2, 1e-4, 10)