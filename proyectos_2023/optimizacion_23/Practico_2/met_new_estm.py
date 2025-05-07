import numpy as np 
from scipy import linalg
from Jacobiana import Jacobiana

#Metodo de newton estacionario con recomienzo cada m iteraciones  

def met_newton_estacionario_m(x0, F, tol, N, m):
    F_x0 = -F(x0)
    JF_x0 = Jacobiana(F, x0)
    det_JF = np.linalg.det(JF_x0)
    if det_JF == 0:
        print('La matriz es singular. No se pudo encontrar la solucion')
    else:
        j = 1
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
                print(f'se evaluo {j} veces la Jacobiana')
                break
            if i == N-1:
                print(f'Usamos el maximo de iteraciones:{N}')
                print(f'el valor del minimizador:{x}')
                print(f'el valor minimo: {F_x}')
                print(f'el error es {err}')
                print(f'se evaluo {j} veces la Jacobiana')
            if i+1 == m * j:
                JF_x0 = Jacobiana(F, x)
                det_JF = np.linalg.det(JF_x0)
                j = j+1
                if det_JF == 0:
                    print('La matriz es singular, no se puede seguir')
                    print(f'num de iteraciones: {i}')
                    print(f'valor del minimizador: {x}')
                    print(f'el valor minimo: {F_x}')
                    print(f'el error es {err}')
                    print(f'se evaluo {j} veces la Jacobiana')
                    break
            else:
                x0 = x
                F_x0 = -F_x
           
