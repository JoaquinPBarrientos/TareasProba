import pandas as pd
import itertools as it
import scipy as sp
import matplotlib.pyplot as plt
import scipy.stats as st # ocupar para distribuciones


# Pregunta 1


# Pregunta 2
# Abrimos la BD.
data_base = pd.read_csv('data.csv')
data_base = pd.DataFrame(data_base)
print(data_base)

	# P1.A
	# Aqui generamos nuestra tablas de frecuencias.
tabla_frecuencias = pd.crosstab( data_base["Numeros"],columns ="Frecuencias")
print(tabla_frecuencias)
	#P1.B
	# Como son frecuencias absolutas, lo mejor es ver la cantidad de de veces que se repite cada valor.
	#Entonces utilizaremos diagrama de barras.
plt.bar(tabla_frecuencias.index, tabla_frecuencias["Frecuencias"])
plt.xlabel("Minutos usados")
plt.ylabel("Frecuencia")
plt.show(True)

print(tabla_frecuencias)



# Pregunta 3
#data_base = pd.DataFrame(data_base)

#print(data_base)



