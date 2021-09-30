import numpy as np
import matplotlib.pylab as plt
plt.style.use('ggplot')
tes=["3.0","300.0","3000.0"]
path="/home/bleon/Documents/Maestria/Clases/Estadistica/energia_"
end=["_5.txt","_25.txt","_50.txt"]

energia_5_3=np.loadtxt(path+tes[0]+end[2])
energia_5_300=np.loadtxt(path+tes[1]+end[2])
energia_5_3000=np.loadtxt(path+tes[2]+end[2])

fig=plt.figure()
plt.title("Sistema 50x50")
plt.plot(energia_5_3,label="T=3K")
plt.plot(energia_5_300,label="T=300K")
plt.plot(energia_5_3000,label="T=3000K")
plt.legend()
plt.show()

tes=["3.0","300.0","3000.0"]
path="/home/bleon/Documents/Maestria/Clases/Estadistica/magnetizacion_"
end=["_5.txt","_25.txt","_50.txt"]

energia_5_3=np.loadtxt(path+tes[0]+end[1])
energia_5_300=np.loadtxt(path+tes[1]+end[1])
energia_5_3000=np.loadtxt(path+tes[2]+end[1])

fig=plt.figure()
plt.title("Sistema 25x25 - magnetizacion")
plt.plot(energia_5_3,label="T=3K")
plt.plot(energia_5_300,label="T=300K")
plt.plot(energia_5_3000,label="T=3000K")
plt.legend()
plt.show()

