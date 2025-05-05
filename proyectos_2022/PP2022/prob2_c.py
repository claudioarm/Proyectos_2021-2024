
import numpy as np 
from random import uniform
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt 


def freedman_diaconis(data):
    num_data = len(data)
    irq = np.percentile(data, 75) - np.percentile(data, 25)
    bin_width = 2 * irq / np.power(num_data, 1/3)
    num_bins = int((np.max(data) -  np.min(data)) / bin_width)  + 1
    return num_bins

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

m = 10000
n = 1000
media_muest = np.zeros(m)
varianza_muest = np.zeros(m)

for i in range(m):
     Z_n = np.zeros(n)
     t = int(n/2)
     for j in range(t):
         Z_n[j], Z_n[j+t] = tranf_boxmull(0, 1)
     media_muest[i] = sum(Z_n)/n

     YY_n = np.zeros(n)
     for k in range(n):
         YY_n[k] = (Z_n[k]-media_muest[i])**2
     varianza_muest[i] = np.sum(YY_n)/(n-1)

num_bins_1 = freedman_diaconis(media_muest)

num_bins_2 = freedman_diaconis(varianza_muest)
                                         
plt.figure()
count_1, bins_1, nn = plt.hist(media_muest, bins=num_bins_1, label= 'Histograma')
plt.legend()
plt.xlabel('valores')
plt.ylabel('frecuencia')
plt.title(f'Media muestral de Y_n, con bins = {num_bins_1}')   


estim_Y = sum(media_muest)/m

for j in range(len(media_muest)):
      media_muest[j] = (media_muest[j]- estim_Y)**2

errstand_Y = np.sum(media_muest)/(m-1)
errstand_Y = np.sqrt(errstand_Y)


#Graficando Normal Teórica 
new_count = np.zeros(len(count_1))

for jdx in range(len(bins_1)-1):
    new_count[jdx] = (norm.cdf(bins_1[jdx+1], estim_Y, errstand_Y)- norm.cdf(bins_1[jdx], estim_Y, errstand_Y))

x = np.linspace(bins_1[0], bins_1[-1], len(new_count))
plt.plot(x, m * new_count, label = 'Ajuste teorico')
plt.legend()
plt.show()

plt.figure() 
count_2, bins_2, nn = plt.hist(varianza_muest, bins=num_bins_2, label= 'Histograma')
plt.legend()
plt.xlabel('valores')
plt.ylabel('freccuencia')
plt.title(f'varianza muestral S^2, con bins = {num_bins_2}')   

estim_S2 = sum(varianza_muest)/m

for j in range(len(varianza_muest)):
     varianza_muest[j] = (varianza_muest[j]- estim_S2)**2

errstand_S2 = np.sum(varianza_muest)/(m-1)
errstand_S2 = np.sqrt(errstand_S2)

new_count_2 = np.zeros(len(count_2))

for jdx in range(len(bins_2)-1):
    new_count_2[jdx] = (norm.cdf(bins_2[jdx+1], estim_S2, errstand_S2)- norm.cdf(bins_2[jdx], estim_S2, errstand_S2))

x = np.linspace(bins_2[0], bins_2[-1], len(new_count_2))
plt.plot(x, m * new_count_2, label = 'Ajuste teorico')
plt.legend()
plt.show()
