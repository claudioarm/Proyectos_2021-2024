import numpy as np 
from scipy import linalg
from Jacobiana import Jacobiana

#Metodo de newton estacionario  

def met_newton_estacionario(x0, F, tol, N):
    F_x0 = -F(x0)
    JF_x0 = Jacobiana(F, x0)
    det_JF = np.linalg.det(JF_x0)
    if det_JF != 0:
        for i in range(N):
            s = linalg.solve(JF_x0, F_x0)
            x = x0 + s
            F_x = F(x)
            err = np.linalg.norm(s, 2)
            if err <= tol:
                print('llegamos a la solucion')
                print(f'num de iteraciones: {i}')
                print(f'valor del minimizador: {x}')
                print(f'el valor minimo: {F_x}')
                print(f'el error es {err}')
                break
            if i == N-1:
                print(f'Usamos el maximo de iteraciones:{N}')
                print(f'el valor del minimizador:{x}')
                print(f'el valor minimo: {F_x}')
                print(f'el error es {err}')
            else:
                x0 = x
                F_x0 = -F_x

    else:
        print('La matriz es singular. No se pudo encontrar la solucion')
