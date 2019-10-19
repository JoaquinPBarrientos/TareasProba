import pandas as pd
import itertools as it
import scipy as sp
import matplotlib.pyplot as plt
import scipy.stats as st # ocupar para distribuciones
import numpy as np
import math
data_base = pd.read_csv('data.csv')
data_base = pd.DataFrame(data_base)
print("La base de datos es la siguiente:\n")
print(data_base,"\n")

#DATOS NO AGRUPADOS

	# P2.A (DATOS NO AGRUPADOS)
	

tabla_frecuencias = pd.crosstab( data_base["Numeros"],columns ="Frecuencias")
print("La tabla de frecuencias es la siguiente:\n ")
print(tabla_frecuencias)


	# P2.B (DATOS NO AGRUPADOS)
	

plt.hist(data_base["Numeros"],color ="orange")
plt.title("Histograma con las frecuencias absolutas en datos no agrupados")
plt.xlabel("Minutos usados")
plt.ylabel("Frecuencia")
plt.show()

print(tabla_frecuencias)

	# P2.C (DATOS NO AGRUPADOS)
	# Hay que calcular el promedio con la funcion .mean()

promedio = (data_base.mean())[0]
print("El promedio obtenido es",promedio)

	# Ahora obtendremos la desviacion estandar.
des_standard = (data_base.std())[0]
print("La desviación estándar es",des_standard)
	# Con ambos datos pordemos obtener el Coeficiente de Variacion

	

d = st.norm(promedio,des_standard)

x1 = 201
x2 = 320
z1 = ( x1 - promedio ) / des_standard
z2 = ( x2 - promedio) / des_standard

plt.title("Funcion de Densidad de Probabilidad en datos no agrupados\n Z = (x - μ)/σ , μ = 260.64 , σ = 17.985, x =[221,300] ")
plt.ylabel('Probabilidad')
plt.xlabel('Valores')
x = np.arange(z1, z2, 0.001)
y = st.norm.pdf(x,0,1)
plt.plot(x,y)
plt.legend("Z")
plt.fill_between(x,y,y<0, color='blue', alpha=.15)
plt.show()



	#P2.D (DATOS NO AGRUPADOS)
CV = des_standard/promedio
print("El coeficiente de variación es",CV)
CV_porcentual = CV*100
print("El coeficiente de variación porcentual es",CV_porcentual)

	# RESPUESTA: Solo un 6.9% 



	#ATENCIÓN: AHORA REALIZAREMOS LA MISMA PREGUNTA PERO PARA DATOS AGRUPADOS

	#P2.A (DATOS AGRUPADOS)
	#Esta parte se hizo con datos agrupados

k = 1 + 3.322 * math.log10(len(data_base))
periodos = math.ceil(k)

inf = min(data_base["Numeros"])        # Limite inferior del primer intervalo
dif = max(data_base["Numeros"])
sup = max(data_base["Numeros"]) + 1    # Limite superior del último intervalo

intervals = pd.interval_range(
    start=inf,
    end=sup,
    periods=k,
    name="Intervalo",
    closed="left")

tabla_distribucion_frecuencias = pd.DataFrame(index=intervals)
tabla_distribucion_frecuencias["FreqAbs"] = pd.cut(data_base["Numeros"], bins=tabla_distribucion_frecuencias.index).value_counts()
tabla_distribucion_frecuencias["Marca"]  = tabla_distribucion_frecuencias.index.mid

print(tabla_distribucion_frecuencias)


	# P2.B
	# A partir de los datos obtenidos en el paso anterior, podemos graficar el histograma. 

plt.title("Histograma con las frecuencias absolutas en datos agrupados")
plt.xlabel("Minutos usados en intervalos")
plt.ylabel("Frecuencia")
plt.bar(["[221, 231)","[231, 241)","[241, 251)","[251, 261)","[261, 271)","[271, 281)","[281, 291)","[291, 301)"],tabla_distribucion_frecuencias["FreqAbs"])
plt.show()


	#P2.C (DATOS AGRUPADOS)
	#Primero obtenemos el promedio
N = 160
X = 0
for i in range(len(tabla_distribucion_frecuencias["Marca"])):
	X += (tabla_distribucion_frecuencias["Marca"].iloc[i])*(tabla_distribucion_frecuencias["FreqAbs"].iloc[i])

promedio = X/N
	
print("El promedio es",promedio)

	#Ahora obtenido el promedio podemos calcular la desviacion estandar.
D = 0
for i in range(len(tabla_distribucion_frecuencias["Marca"])):
	D += ((tabla_distribucion_frecuencias["Marca"].iloc[i] - promedio)**2)*(tabla_distribucion_frecuencias["FreqAbs"].iloc[i])
	
Desviacion_estandar = math.sqrt(D/(N-1))
print("La desviación estándar es",Desviacion_estandar)


#Graficamos segun la distribucion normal
# Para este codigo se ultilizo al autor de esta pagina https://pythonforundergradengineers.com/plotting-normal-curve-with-python.html
d = st.norm(promedio,Desviacion_estandar,)

d = st.norm(promedio,Desviacion_estandar)
d.pdf(0.5)

x1 = 201
x2 = 320
z1 = ( x1 - promedio ) / Desviacion_estandar
z2 = ( x2 - promedio) / Desviacion_estandar

plt.title("Funcion de Densidad de Probabilidad en datos  agrupados\n Z = (x - μ)/σ , μ = 261.56 , σ = 18.0407, x =[221,300] ")
plt.ylabel('Probabilidad')
plt.xlabel('Valores')
x = np.arange(z1, z2, 0.001)
y = st.norm.pdf(x,0,1)
plt.plot(x,y,color = "y")
plt.legend("Z")
plt.fill_between(x,y,y<0, color='yellow', alpha=.1)
plt.show()

#P2.D (DATOS AGRUPADOS)
CV = Desviacion_estandar/promedio
print("El coeficiente de variación es",CV)
CV_porcentual = CV*100
print("El coeficiente de variación porcentual es",CV_porcentual)


	# RESPUESTA: Solo un 6.897290415506971% 
