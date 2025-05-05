from cProfile import label
import numpy as np 
import matplotlib.pyplot as plt 

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
        #y = np.sqrt(np.divide(-2* np.log(R2), R2))*v_2
    
    return x 

def SRK1(x_0, funa, fun_b, Dt, n):
    X = np.zeros(n)
    X[0] = x_0
    for t in range(n-1):
        Y = tranf_boxmull(0, 1)
        X[t+1] = X[t] + funa(X, t)*Dt + fun_b(X, t)*(Dt)**0.5*Y 
    return X

def SRK1_prss(x_0, k, D, Dt, n):
    X = np.zeros(n)
    X[0] = x_0
    for t in range(n-1):
        Y = tranf_boxmull(0, 1)
        X[t+1] = X[t]*(1 - k*Dt) + (D*Dt)**0.5*Y 
    return X

n, m = 40, 5000

mtrx = np.zeros((m, n))

means = np.zeros((2, n))

var = np.zeros((2, n))

for idx in range(2):
    for k in range(m):
        X = SRK1_prss(1.0, 1.0, 2, 0.1, n)
        mtrx[k, :] = X
    Z = np.zeros(n)
    Z_1 = np.zeros(n)
    W = np.zeros(m)
    for i in range(n):
        Z[i] = np.sum(mtrx[:, i])/m
        for j in range(m):
            W[j] = (Z[i]- mtrx[j, i])**2
        Z_1[i] = np.sum(W)/(m-1)
    means[idx, :] = Z
    var[idx, :] = Z_1

Dt = 0.1
    
T = np.zeros(40)
for kdx in range(40):
    T[kdx] = kdx*Dt 
    
#Media teorica 

def media(x_0, t, k):
    return x_0*np.exp(-k*t)
teo = np.zeros(40)
for jdx in range(40):
    teo[jdx] = media(1.0, T[jdx], 1.0)

plt.plot(T, means[0, :], label = 'aprox 1')
plt.plot(T, means[1, :], label = 'aprx 2')
plt.plot(T, teo, label = 'curva teorica')
plt.xlabel('T')
plt.ylabel('<x>')
plt.title(f'SRK1')
plt.legend()
plt.show()

def varian(x_0, t, k, D):
  return (x_0**2)*np.exp(-2*k*t)+ D*k*(1-np.exp(-2*k*t))-1
teo_2 = np.zeros(40)
for jdx in range(40):
  teo_2[jdx] = varian(1.0, T[jdx], 1.0, 2.0)
       
plt.plot(T, var[0, :], label = 'aprox 1')
plt.plot(T, var[1, :], label = 'aprox 2')
plt.plot(T, teo_2, label = 'curva teorica')
plt.xlabel('T')
plt.ylabel('<x^2>')
plt.title(f'SRK1')
plt.legend()
plt.show()
        

#######################################################
    
def SRK2(x_0, funa, funb, Dt, n):
    X = np.zeros(n)
    X[0] = x_0
    for t in range(n-1):
        Y = tranf_boxmull(0, 1)
        f1 = funa(X, t)
        f2 = X[t]+funa(X, t)*Dt + funb*(Dt)**0.5*Y
        X[t+1] = X[t] + 0.5*Dt*(f1+f2)+funb*(Dt)**0.5*Y
        
    return X

def SRK2_pross(x_0, k, D, Dt, n):
    X = np.zeros(n)
    X[0] = x_0
    for t in range(n-1):
        Y = tranf_boxmull(0, 1)
        X[t+1] = X[t] - (0.5*k*Dt)*(X[t]*(2-k*Dt)+(D*Dt)**0.5*Y)+(D*Dt)**0.5*Y
        
    return X

n1, m1 = 40, 5000

mtrx_1 = np.zeros((m1, n1))

means_1 = np.zeros((2, n1))

var_1 = np.zeros((2, n1))

for idx in range(2):
    for k in range(m1):
        X1 = SRK2_pross(1.0, 1.0, 2, 0.1, n1)
        mtrx_1[k, :] = X1
    Z_1 = np.zeros(n1)
    Z_2 = np.zeros(n1)
    W_1 = np.zeros(m1)
    for i in range(n1):
        Z_1[i] = np.sum(mtrx_1[:, i])/5000
        for j in range(m):
            W_1[j] = (Z_1[i]- mtrx_1[j, i])**2
        Z_2[i] = np.sum(W_1)/(m-1)
    means_1[idx, :] = Z_1
    var_1[idx, :] = Z_2

Dt = 0.1

T1 = np.zeros(40)
for kdx in range(40):
    T1[kdx] = kdx*Dt 
    
#Varianza teorica 

def media_2(x_0, t, k):
    return x_0*np.exp(-k*t)
teo_3 = np.zeros(40)
for jdx in range(40):
    teo_3[jdx] = media(1.0, T[jdx], 1.0)
    
plt.plot(T1, means_1[0, :], label = 'aprox 1')
plt.plot(T1, means_1[1, :], label = 'aprox 2')
plt.plot(T1, teo_3, label = 'curva toerica')
plt.xlabel('T')
plt.ylabel('<x>')
plt.title(f'SRK2')
plt.legend()
plt.show()

def varian(x_0, t, k, D):
  return (x_0**2)*np.exp(-2*k*t)+ D*k*(1-np.exp(-2*k*t))-1
teo_4 = np.zeros(40)
for jdx in range(40):
  teo_4[jdx] = varian(1.0, T1[jdx], 1.0, 2.0)


plt.plot(T1, var_1[0, :], label = 'aprox 1')
plt.plot(T1, var_1[1, :], label = 'aprox 2')
plt.plot(T1, teo_4, label = 'curva toerica')
plt.xlabel('T')
plt.ylabel('<x^2>')
plt.title(f'SRK2 Dt')
plt.legend()
plt.show()


    
    
