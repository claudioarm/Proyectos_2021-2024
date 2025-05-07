import numpy as np
from scipy import linalg
from Jacobiana import Jacobiana

#Metodo de newton 

def met_newton(x0, F, p, tol, N, sol1 = True, sol2 =False):
    F_x0 = -F(x0)
    list_x = [x0]
    list_err = [] 
    list_Fx = []
    for i in range(N):
        JF_x0 = Jacobiana(F, x0)
        det_JF = np.linalg.det(JF_x0)
        if det_JF != 0:
            s = linalg.solve(JF_x0, F_x0)
            x = x0 + s
            list_x.append(x)
            F_x = F(x)
            list_Fx.append(F_x)
            err = np.linalg.norm(s, p)
            list_err.append(err)
            if err <= tol:
                break

            else:
                x0 = x
                F_x0 = -F_x

        else:
            print('La matriz es singular. No se pudo encontrar la solucion')
            break
    
    if sol1:
        k = len(list_x)
        if k < N-1:
            print('llegamos a la solucion')
            print(f'num de iteraciones: {k}')
            print(f'valor del minimizador: {list_x[k-1]}')
            print(f'el valor minimo: {list_Fx[k-1]}')
            print(f'el error es {list_err[k-1]}')
        
        if len(list_x) == N-1:
            print(f'Usamos el numero maximo de iteraciones: {N}')
            print(f'num de iteraciones: {list_x.index(list_x[N-1])}')
            print(f'valor del minimizador: {list_x[N-1]}')
            print(f'el valor minimo: {list_Fx[N-1]}')
            print(f'el error es {list_err[N-1]}')
                
    
    if sol2:
        return list_x
    
    


