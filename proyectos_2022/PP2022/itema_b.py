from random import uniform
import numpy as np 
import matplotlib.pyplot as plt 

n = 10**4


num_random = np.random.uniform(0, 1, n)

# primera prueba 
num_bins = np.array([5, 50])
for i in range(2):
    contador, bins, d = plt.hist(num_random, num_bins[i])
    plt.xlabel('Valores')
    plt.ylabel('Freccuencia')
    plt.title(f'Histograma Uniforme con bins = {num_bins[i]}')
    plt.show()

#La regla de Sturges

def sturges(data):
    num_data = len(data)
    num_bins = int(np.log2(num_data)) + 1
    return num_bins

bins_s = sturges(num_random)
contador, bins, d = plt.hist(num_random, bins_s)
plt.xlabel('Valores')
plt.ylabel('Freccuencia')
plt.title(f'Histograma: La regla de Sturges con bins = {bins_s}')
plt.show()


# La regla de Freedman-Diaconis

def freedman_diaconis(data):
    num_data = len(data)
    irq = np.percentile(data, 75) - np.percentile(data, 25)
    bin_width = 2 * irq / np.power(num_data, 1/3)
    num_bins = int((np.max(data) -  np.min(data)) / bin_width)  + 1
    return num_bins

bins_fd = freedman_diaconis(num_random)
contador, bins, d = plt.hist(num_random, bins_fd)
plt.xlabel('Valores')
plt.ylabel('Freccuencia')
plt.title(f'Histograma: La regla de Freedman-Diaconis con bins = {bins_fd}')
plt.show()


            
    
     



