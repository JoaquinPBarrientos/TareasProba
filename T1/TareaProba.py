import pandas as pd
import itertools as it
import scipy as sp
import matplotlib.pyplot as plt
import scipy.stats as st # ocupar para distribuciones
import numpy as np
import math
import seaborn as sns
# Pregunta 1


# Pregunta 2
# Abrimos la BD.

data_base = pd.read_csv('data.csv')
data_base = pd.DataFrame(data_base)
print("La base de datos es la siguiente:\n")
print(data_base,"\n")

	# P2.A
	# Aqui generamos nuestra tablas de frecuencias.

tabla_frecuencias = pd.crosstab( data_base["Numeros"],columns ="Frecuencias")
print("La tabla de frecuencias es la siguiente:\n ")
print(tabla_frecuencias)

	# P2.B
	# Como son frecuencias absolutas, lo mejor es ver la cantidad de de veces que se repite cada valor.
	# Entonces utilizaremos diagrama de barras.

plt.bar(tabla_frecuencias.index, tabla_frecuencias["Frecuencias"])
plt.xlabel("Minutos usados")
plt.ylabel("Frecuencia")
plt.show()

print(tabla_frecuencias)
	# P2.C
	# Hay que calcular el promedio con la funcion .mean()
	# Grafiquemos

d = st.norm(promedio,des_standard)

v = d.rvs(50)
plt.hist(d.rvs(1000),normed = True)
plt.show()
promedio = (data_base.mean())[0]
print("El promedio obtenido es",promedio)

	# Ahora obtendremos la desviacion estandar.
des_standard = (data_base.std())[0]
print("La desviación estándar es",des_standard)
	# Con ambos datos pordemos obtener el Coeficiente de Variacion

	# Al ojo, es una desviación bastante "Normal" si la comparamos con la media y los datos.



	#P2.D
CV = des_standard/promedio
print("El coeficiente de variación es",CV)
CV_porcentual = CV*100
print("El coeficiente de variación porcentual es",CV_porcentual)
	#Como podemos ver el porcentaje es de 6.9% lo que está mucho más abajo de 80% , por lo que el promedio 
	# es representativo del conjunto de datos, por lo tanto el conjunto de datos es homogeneo.

	# RESPUESTA: Solo un 6.9% 

# Pregunta 3
#data_base = pd.DataFrame(data_base)

#print(data_base)




                

