import numpy as np

def unit(n, i):
    e = np.zeros(n)
    e[i] = 1
    return e 

#Matriz Jacobiana

def Jacobiana(F, x):
    h = 0.1
    F_x = F(x)
    m = len(x)
    n = len(F_x)
    JF_x = np.zeros((n,m))
    for j in range(m):
        x_h = x+h*unit(m,j)
        F_xh = F(x_h)
        for i in range(n):
            JF_x[i,j] = (F_xh[i] - F_x[i])/h
    
    return JF_x


