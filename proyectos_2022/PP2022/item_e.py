import numpy as np 
from random import uniform

#e

def genbernoulli(p, k):
    var_ber = np.zeros(k)
    for i in range(k):
        u = np.random.uniform(0, 1)
        if  u > p: 
            var_ber[i] = 0 
        if u <= p:
            var_ber[i] = 1
        
    return var_ber

# Ejemplo
#Sea p = 0.6 y k = 20
print(f'AV_bernoulli = {genbernoulli(0.6, 20)}')

#f

def genbinomial(p, n, k):
    var_bin = np.zeros(k)
    for j in range(k):
        var_bernll = genbernoulli(p, n)
        var_bin[j] = sum(var_bernll)
    
    return var_bin

parm = np.array([0.5, 0.7, 0.9])

muestras = np.array([10, 100, 1000, 10000])

L = len(muestras)

for t in range(len(parm)):
    for k in range(L):
        Y = genbinomial(parm[t], muestras[k], 1)[0]
        p_hat =Y/muestras[k]
        sigma_p_hat = np.sqrt((p_hat*(1-p_hat))/muestras[k])
        print(f'Para p = {parm[t]} y n = {muestras[k]} se obtiene la VA Y_{k} ={Y}. El estimador puntual y error estandar para p son; p_hat_{k} ={p_hat} y sigma_p_hat_{k} = {sigma_p_hat}')  
    print('-------------------------------------------------------------------------------------------------')

