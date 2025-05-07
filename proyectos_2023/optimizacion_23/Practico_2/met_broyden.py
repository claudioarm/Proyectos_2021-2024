import numpy as np 
from scipy import linalg
from Jacobiana import Jacobiana

# Metodo de broyden 

def met_broyden(x, F, tol, N):
    
    B_0 = Jacobiana(F, x)
    det_B = np.linalg.det(B_0)
    if det_B != 0:
        for i in range(N):
            F_x = F(x)
            s = np.linalg.solve(B_0, -F_x)
            x = x + s
            norm_s = np.linalg.norm(s, 2)
            if norm_s <= tol:
                print('llegamos a la solucion')
                print(f'num de iteraciones: {i}')
                print(f'valor del minimizador: {x}')
                print(f'el valor minimo: {F_x}')
                print(f'el error es {norm_s}')
                break
            
            if i == N-1:
                print(f'Usamos el maximo de iteraciones:{N}')
                print(f'el valor del minimizador:{x}')
                print(f'el valor minimo: {F_x}')
                print(f'el error es {norm_s}')
            
            else:
                y = F(x) - F_x
                v = np.dot(B_0, s)
                rho = np.dot(s.T,s)
                B_0 = B_0 + np.outer(y - v, s.T)/rho


def met_broyden_1(x_0, Fun, tol, M):
    v = Fun(x_0)
    B_0 = Jacobiana(Fun, x_0)
    B = np.linalg.inv(B_0)
    s = - np.dot(B, v)
    x = x_0 + s
    k = 2
    
    while k <= M:
        w = v
        v = Fun(x)
        y = v - w
        z = -np.dot(B, y)
        p = - np.dot(s.T, z)
        ut = np.dot(s.T, B)
        B = B + np.outer(s+z, ut)/p
        s = -np.dot(B, v)
        x = x + s
        norm_s = np.linalg.norm(s, np.inf)
        if norm_s <= tol:
            print('llegamos a la solucion')
            print(f'num de iteraciones: {k}')
            print(f'valor del minimizador: {x}')
            print(f'el valor minimo: {v}')
            print(f'el error es {norm_s}')
            break 
    if k == M:
        print(f'Usamos el maximo de iteraciones:{M}')
        print(f'el valor del minimizador:{x}')
        print(f'el valor minimo: {v}')
        print(f'el error es {norm_s}')
        








