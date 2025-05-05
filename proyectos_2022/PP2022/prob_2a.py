
import numpy as np 
from random import uniform
from scipy import stats
import matplotlib.pyplot as plt 

# a

def boxmuller(n):
    Z = np.zeros(n)
    for i in range(n):
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, 1)
        R = np.sqrt(-2 * np.log(u1))
        theta = 2*np.pi*u2
        Z[i] = R * np.cos(theta)
        
    return Z 

def tranf_boxmull(a, b):
    u_1 = np.random.uniform(a, b)
    u_2 = np.random.uniform(a, b)  
    v_1 = 2*u_1-1
    v_2 = 2*u_2-1
    R2 = v_1**2 + v_2**2
    if R2==1 or R2>1:
        return tranf_boxmull(a,b)
    else:
        x = np.sqrt(np.divide(-2* np.log(R2), R2))*v_1
        y = np.sqrt(np.divide(-2* np.log(R2), R2))*v_2
    
    return x, y 

# b

def muesaleat(n):
         Z_n = np.zeros(n)
         t = int(n/2)
         for j in range(t):
             Z_n[j], Z_n[j+t] = tranf_boxmull(0, 1)
         print(f'Muestra aleatoria Z={Z_n} con tamano muestral n = {n}')
         Y_n = sum(Z_n)/n
         S2 = 0
         for i in range(n):
             S2 += (Z_n[i]-Y_n)**2/(n-1)
       
         print(f'Media muestral Y_n={Y_n}; varianza muestral S2_n = {S2}')
         print('--------------------------------------------------------')

N = np.array([10, 100, 1000, 10000])

for k in range(len(N)):
     muestra_n = muesaleat(N[k])


# def muesaleat(n):
#       Z_n = boxmuller(n)
#       print(f'Muestra aleatoria Z_{n}={Z_n} con tamano muestral n = {n}')
#       Y_n = sum(Z_n)/n
#       X = np.zeros(n)
#       for i in range(n):
#           X[i] = (Z_n[i]+Y_n)**2
#       S2 = np.sum(X)/(n-1)
    
#       print(f'Media muestral Y_{n}={Y_n}; varianza muestral S2_{n} = {S2}')

# n = np.array([10, 100, 1000, 10000])

# for k in range(len(n)):
#      muestra_z = muesaleat(n[k])

           
             
            
            
    
    


    
    
    