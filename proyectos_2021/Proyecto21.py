
import numpy as np 

#A continuación se presenta los datos de OpenFlights

datos_aeropuertos = np.genfromtxt("C:\\Users\\54385\\OneDrive\\Escritorio\\Proyectos_2021-2024\\Proyectos_2021\\airports.dat.txt", delimiter=",", dtype="str", encoding="Latin-1")

datos_rutas = np.genfromtxt("C:\\Users\\54385\\OneDrive\\Escritorio\\Proyectos_2021-2024\\Proyectos_2021\\routes.dat.txt", delimiter=",", dtype="str", encoding="Latin-1")

#########################################################################################

rutas = datos_rutas[:, [2, 4]]

aeropuertos = np.unique(rutas)

rutas_indice = rutas.copy()
for idx in range(len(aeropuertos)):
    rutas_indice = np.where(rutas_indice == aeropuertos[idx], idx, rutas_indice)

rutas_indice  = rutas_indice.astype(int)
 
######################################################################################

#Matriz de enlaces

m = len(aeropuertos) 

matriz_enlaces = np.zeros((m, m))

m_0, n_0 = rutas_indice.shape

for i in range(m_0):

    matriz_enlaces[rutas_indice[i,1], rutas_indice[i, 0]] = 1
 
for j in range(m):
    w = np.sum(matriz_enlaces[:, j])
    if w != 0:
    
        matriz_enlaces[:, j] = matriz_enlaces[:, j] / float(w) 
        
##################################################################################################################

N = len(aeropuertos)
vector_inicial = (1/N) * np.ones(N)

#Método de la potencia

def autpotencias(A, q_0, err=1e-10, M=500):
    q_tilde = A @ q_0 
    rho_tilde = (q_0.T@q_tilde)/np.linalg.norm(q_0, 2)**2 
    for k in range(M):
        q = q_tilde/np.linalg.norm(q_tilde, 2)
        q_tilde = A @ q 
        rho = q.T@q_tilde
        if np.abs(rho - rho_tilde) < err:
            print("iteraciones:", k)
            return q, rho
        rho_tilde = rho
    return q, rho 


#Aplicación del método de las potencias

aeropuertos_rangos, autovalor_proporcional = autpotencias(matriz_enlaces, vector_inicial)


indices = np.argsort(aeropuertos_rangos) #Se ordenan los indices de menor a mayor

aeropuertos_rangos = aeropuertos_rangos[indices] #Se reordenan los rangos

aeropuertos_rangos = list(reversed(aeropuertos_rangos)) #Se reordena la lista de mayor a menor

#Se aplica lo mismo para aeropuertos

aeropuertos = aeropuertos[indices]

aeropuertos = list(reversed(aeropuertos))


top_diez_rangos = aeropuertos_rangos[:10]

top_diez = aeropuertos[:10]

datos_codigos = datos_aeropuertos[:, 4] #Lista de codigos de datos_aeropuertos

for i in range(len(datos_codigos)):
    datos_codigos[i] = datos_codigos[i].strip('"')

print('Top 10 de los aeropuertos con mejor clasificacion en el mundo de acuerdo a los datos de OpenFlights registrados en 2014.')
print('/')

#Top 10 de mejor clasificación. 
print('Puesto /','  Clasificacion /','  Nombre  /', '   Ciudad   /', '  Pais   /', '   Codigo  /')
i = 0
for k in range(len(top_diez)):
    if top_diez[k] in datos_codigos:
        r = np.where(datos_codigos == top_diez[k])[0]
        i = i+1
        lista_ranking = datos_aeropuertos[r[0], 1:5]
        for l in range(len(lista_ranking)):
             lista_ranking[l] = lista_ranking[l].strip('"')
           
        print(f'  {i}   /', f'{top_diez_rangos[k]} /', f' {lista_ranking[0]} /', f' {lista_ranking[1]} /', 
              f' {lista_ranking[2]} /', f' {lista_ranking[3]} /')
        print('----------------------------------------------------------------------------------------------------')
    
    else:
        print('Desconocido')

# Aeropuerto con la menor clasificación.

ultimo_areopuerto = aeropuertos[-1]
print('Por ultimo el aeropuerto con menor clasificacon es:')
print('/')
print('Puesto /','Clasificacion /', '  Nombre   /', '  Ciudad   /', '  Pais   /', '  Codigo    /')

if ultimo_areopuerto in datos_codigos:
    r = np.where(datos_codigos == ultimo_areopuerto)[0]
    menor_ranking = datos_aeropuertos[r[0], 1:5]
    for l in range(len(menor_ranking)):
        menor_ranking[l] = menor_ranking[l].strip('"')
             
    print(f' {len(aeropuertos)} /', f'{aeropuertos_rangos[-1]} /', f' {menor_ranking[0]} /', f' {menor_ranking[1]} /', f' {menor_ranking[2]} /', f' {menor_ranking[3]} /')
    print('-------------------------------------------------------------------------------------------------------')
    
    
else:
    print('Desconocido')