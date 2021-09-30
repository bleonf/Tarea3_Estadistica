# Tarea3_Estadistica
Implementación y uso de método de Montecarlo para estudio de la evolución energética basado en un modelo de Ising.

Para utilizar este modelo es necesaria una instalación de PYTHON3 con los módulos que se encuentran en el archivo.
~~~
requirements.txt
~~~
Desde una terminal de linux se puede utilizar el comando:
~~~
pip install -r requirements.txt
~~~
Sin embargo, las librerias utilizadas son numpy, matplotlib y random, las cuales se encuentran entre los paquetes básicos y ampliamente utilizados de python.

Despues de tener el ambiente preparado, el usuario debe editar en el código 4 diferentes caracteristicas. 
1. Pasos a modelar: editar opcion "steps"
2. Tamaño de la red: editar valor de "square_size"
3. Temperatura: editar valor "Temp"
4. Coeficiente de interacción: editar valor de "J_spin"

Estos valores estan fijados inicialmente en 10,5,273.0 y 1.0 respectivamente.

Finalmente, en las útlimas lineas del código esta la opción de descomentar la linea con la cual se crea una figura con la evolución temporal de la magnetización y la energía.
~~~
plt.savefig("ISING_pasos{}_T{}_J{}_sq{}.pdf".format(steps,Temp,J_spin,square_size))
~~~

Con estas opciones, el usuario ya puede correr el script de python que aparte de mostrar y guardar las figuras, guarda en dos archivos de texto los valores de energia y magnetizacion para analisis posterior.

Adicionalmente se incluye un codigo base con el que se pueden analizar los archivos output de magnetizacion y energia y graficarlos juntos.
