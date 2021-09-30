import numpy as np
import matplotlib.pylab as plt
# import datetime
import random
from tqdm import tqdm
plt.style.use('ggplot')
# ts1=datetime.datetime.now().timestamp()

#Pasos de simulacion
steps=100000
#Tamanho de la muestra (cuadrada)
square_size=25
#Constante de Boltzman
k_b=1.38064852*(10**(-23))
#Temperatura y temperatura inversa
Temp=3.0
Beta=1/(Temp*k_b)
#Constante de acoplamiento - ferromagnetico
J_spin=1.0
#Matriz inicial aleatoria
Lattice=np.random.choice([1,-1],(square_size,square_size))
Original=Lattice.copy()
print("setup done")
def Switch(matrix):
    """Metodo que produce nueva matriz con un elemento cambiado (1--->-1 & -1--->1)

    Args:
        matrix (square np.array): Matriz de NxN elementos 

    Returns:
        matrix (square np.array): Misma matriz inicial con un elemento cambiado
    """    
    a,b= np.random.randint(0, high=square_size-1, size=2)
    aux=matrix.copy()
    aux[a,b]*=-1
    return aux
    
def CalcEnergia(matrix):
    """Metodo que calcula energía para cualquier matriz cuadrada o rectangular. Se realiza la suma por columnas y por filas con ella misma corrida un elemento. Despues se le agrega

    Args:
        matrix (np.array): Matriz cuadrada o rectangular

    Returns:
        suma: energia de la matriz incidente calculada por el modelo de Ising
    """    
    suma=0
    for i in range(square_size):
        filas=np.sum((matrix[i,1:]*matrix[i,:-1]))+matrix[i,0]*matrix[i,-1]
        suma+=(filas)
    for j in range(square_size):
        columnas=np.sum((matrix[1:,j]*matrix[:-1,j]))+matrix[0,j]*matrix[-1,j]
        suma+=(columnas)
    return -1*J_spin*suma

energias=np.zeros(steps)
magnetizacion=np.zeros(steps)
pasos=np.arange(0,steps,1)


E_inicial=CalcEnergia(Lattice)
for i in tqdm(range(steps)):
    switched=Switch(Lattice)
    E_nuevo=CalcEnergia(switched)
    if E_nuevo<=E_inicial:
        Lattice=switched 
        E_inicial=E_nuevo 
    elif np.exp(-1*Beta*(E_nuevo-E_inicial))>random.uniform(0,1):
        Lattice=switched 
        E_inicial=E_nuevo 
    energias[i]=E_inicial
    magnetizacion[i]=np.sum(Lattice)/(square_size**2)

print("steps done")
        
fig,(axes)=plt.subplots(2,1)
plt.suptitle("Evolución de energia y magnetización para %i particulas a T= %.1f K"%(square_size**2,Temp))
axes[0].plot(pasos,energias)
axes[0].set_ylabel("Energia total \n (unidades arbitrarias)")
axes[0].set_xlabel("Tiempo (pasos)")

axes[1].plot(pasos,magnetizacion)
axes[1].set_ylabel("Magnetizacion \n(unidades arbitrarias)")
axes[1].set_xlabel("Tiempo (pasos)")
plt.tight_layout()
# plt.savefig("/home/bleon/Documents/Maestria/Clases/Estadistica/ISING_pasos_{}_T{}_J{}_sq{}.pdf".format(steps,Temp,J_spin,square_size))
plt.show()

# fig,(axes)=plt.subplots(1,2)
# plt.title("Estados iniciales y finales de red {} x {} a T={}".format(square_size,square_size,Temp))
# axes[0].matshow(Original,cmap="coolwarm")
# axes[0].set_xlabel("Estado inicial")
# axes[1].matshow(Lattice,cmap="coolwarm")
# axes[1].set_xlabel("Estado final")
# plt.savefig("/home/bleon/Documents/Maestria/Clases/Estadistica/ISING_mat_{}_T{}_J{}_sq{}.pdf".format(steps,Temp,J_spin,square_size))
# # plt.show()
# print("matrix fig done")

# outfile=open("/home/bleon/Documents/Maestria/Clases/Estadistica/magnetizacion_{}_{}.txt".format(Temp,square_size),"w+")
# for mag in magnetizacion:
#     outfile.write("{}\n".format(mag))
# outfile.close()

# outfile2=open("/home/bleon/Documents/Maestria/Clases/Estadistica/energia_{}_{}.txt".format(Temp,square_size),"w+")
# for mag in energias:
#     outfile2.write("{}\n".format(mag))
# outfile2.close()
# print("output files done")

    
        
