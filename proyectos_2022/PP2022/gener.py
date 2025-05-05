from random import uniform

import numpy as np 

n = 20

num_random = np.random.uniform(0, 1, n)


print(f'num_random = {num_random}')

#Generador mixto 
# def randMixto(a, c, M, u):
#     return np.mud((a*u+c),M)

# def ranmulti(a, M, u):  
#     return np.mod((a*u), M)

# a = 1103515245
# c = 12345
# M = 2**(32)
# semilla = 9876543210
# u = 3
# num_random = []
# for i in range(20):
#     u = np.mud((a*u+c),M)
#     num_random.append(u/M)

# # ran0 
# M = 2**(31)-1    
# a = 7**5
# semilla = 987654321
# u = semilla
# num_random = []
# for j in range(10):
#     num_random.append(u/M)
#     u = np.mod((a*u), M)

# print(f'num_random = {num_random}')

# Ia = 16807
# Im = 2**31-1
# Am = 1/Im
# Iq = 127773
# Ir = 2836
# Mask = 123459876

# def ran0(idum):
#     num = []
#     for i in range(20):
#         k = idum/Iq
#         idum = Ia*(idum-k*Iq)-Ir*k
#         if idum >= 0:
#             u = idum
#         else:
#             u = idum+Im
#         num.append(u/Im)
#     return num
            
# print(ran0(semilla))            
        
          


#########################

# M1 = 2**(31)-86
# a1 = 40014
# def ran0(u):
#     return np.mod((a1*u),M1)

# M2 = 2**(31)-249
# a2 = 40692
# def ran1(u):
#     return np.mod((a2*u),M2) 

# def ran2(u1, u2, M):
#     u = np.mod((u1-u2), M)
#     return (u1-u2)

# N = 10 
# semilla1 = 1000
# semilla2 = 1000

# u1 = semilla1

# u2 = semilla2

# for i in range(N):
#     u1 = ran0(u1)
#     u2 = ran1(u2)
#     u3 = ran2(u1,u2, M)















