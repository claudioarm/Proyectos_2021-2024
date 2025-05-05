from random import uniform
from scipy import stats
from scipy.stats import norm 
import numpy as np 
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
    media_muest[i] = np.sum(Z_n)/n
    YY_n = np.zeros(n)
    for k in range(n):
        YY_n[k] = (Z_n[k]-media_muest[i])**2
    varianza_muest[i] = np.sum(YY_n)/(n-1)

# chi_cuadrado para ajustar los S^2
mean_2 = np.sum(varianza_muest)/m

sigma_2 = 0 
for idx in range(m):
    sigma_2 += (varianza_muest[idx]- mean_2)**2

sigma_2 = sigma_2/(m-1)
sigma_2 = np.sqrt(sigma_2)

num_bins = freedman_diaconis(varianza_muest)

count, bins, non = plt.hist(varianza_muest, num_bins)

new_count = np.zeros(len(count))

for jdx in range(len(bins)-1):
    new_count[jdx] = (norm.cdf(bins[jdx+1], mean_2, sigma_2)- norm.cdf(bins[jdx], mean_2, sigma_2))

new_count_1 = new_count [10:num_bins-15]

new_count_1[-1] = (1- norm.cdf(bins[num_bins-15], mean_2, sigma_2))

new_count_1[0] = norm.cdf(bins[10], mean_2, sigma_2)

new_count_1 = m * new_count_1

count_1 = count [10:num_bins-15]

count_1[0] = np.sum(count [0:10])

count_1[-1] = np.sum(count [num_bins-15:])

chi_cuad = 0

for k in range(len(new_count_1)):
     chi_cuad += np.divide((count_1[k] - new_count_1[k])**2, new_count_1[k])

print(f'El valor encontrado para los S^2 es chi_cuad = {chi_cuad}')
# print('-------------------------------------------------')
gl = len(new_count_1)-3
ch2_gl = chi_cuad/gl
alpha = 0.05
chi2_critico = stats.chi2.ppf(1-alpha, gl)
print(f'El chi_cuadrado critico es = {chi2_critico}')
print('Se deduce que:')
if chi_cuad < chi2_critico:
    print(f'{chi_cuad} < {chi2_critico}. Aceptamos la hipotesis nula: Los valores generados (S^2) se ajustan a una distribucion normal')
else:
    print(f'{chi_cuad} > {chi2_critico}.  Rechazamos la hipotesis nula: Los valores generados (S^2) NO se ajustan a una distribucion normal')
print(f'Además el chi_cuadrado sobre los grados de libertad ({len(new_count_1-3)} en total) es = {ch2_gl}')





