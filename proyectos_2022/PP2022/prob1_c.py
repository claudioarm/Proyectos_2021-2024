from random import uniform
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt 


def freedman_diaconis(data):
    num_data = len(data)
    irq = np.percentile(data, 75) - np.percentile(data, 25)
    bin_width = 2 * irq / np.power(num_data, 1/3)
    num_bins = int((np.max(data) -  np.min(data)) / bin_width)  + 1
    return num_bins
def sturges(data):
    num_data = len(data)
    num_bins = int(np.log2(num_data)) + 1
    return num_bins
n = 10**4

num_random = np.random.uniform(0, 1, n)

num_bins = sturges(num_random)

count_num, bins, non = plt.hist(num_random, num_bins, label= f'{num_bins} bins')
plt.legend()
plt.show()

prob_num = np.zeros(num_bins)

for idx in range(len(bins)-1):
    prob_num[idx] = bins[idx+1] - bins[idx]

new_count = n * prob_num

chi_cuad = 0

for k in range(len(new_count)):
     chi_cuad += np.divide((count_num[k] - new_count[k])**2, new_count[k])

print(f'El valor encontrado es chi_cuad = {chi_cuad}')
# print('-------------------------------------------------')
gl = len(new_count)-1
ch2_gl = chi_cuad/gl
alpha = 0.05
chi2_critico = stats.chi2.ppf(1-alpha, gl)

print(f'El chi_cuadrado critico es = {chi2_critico}')
print('Se deduce que:')
if chi_cuad < chi2_critico:
    print(f'{chi_cuad} < {chi2_critico}. Aceptamos la hipotesis nula: Los numeros aleatorios generados se ajustan a una distribucion uniforme')
else:
    print(f'{chi_cuad} > {chi2_critico}.  Rechazamos la hipotesis nula: Los numeros aleatorios generados NO se ajustan a una distribucion uniforme')
print(f'Ademas el chi_cuadrado sobre los grados de libertad ({len(new_count)-1} en total) es = {ch2_gl}')

print(gl)