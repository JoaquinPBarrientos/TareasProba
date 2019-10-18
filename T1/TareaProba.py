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

#DATOS NO AGRUPADOS

	# P2.A (DATOS NO AGRUPADOS)
	# Aqui generamos nuestra tablas de frecuencias.
	#Esta parte se hizo con datos no agrupados.

tabla_frecuencias = pd.crosstab( data_base["Numeros"],columns ="Frecuencias")
print("La tabla de frecuencias es la siguiente:\n ")
print(tabla_frecuencias)


	# P2.B (DATOS NO AGRUPADOS)
	# Como son frecuencias absolutas, lo mejor es ver la cantidad de de veces que se repite cada valor.
	# Entonces utilizaremos diagrama de barras.

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

	# Al ojo, es una desviación bastante "Normal" si la comparamos con la media y los datos.
	# Grafiquemos
	# Para este codigo se ultilizo al autor de esta pagina https://pythonforundergradengineers.com/plotting-normal-curve-with-python.html

d = st.norm(promedio,des_standard)

x1 = 201
x2 = 320
z1 = ( x1 - promedio ) / des_standard
z2 = ( x2 - promedio) / des_standard

plt.title("Funcion de Densidad de Probabilidad en datos no agrupados\n Z = (x - μ)/σ , μ = 260.64 , σ = 17.985, x =[221,300] ")
plt.ylabel('Probabilidad')
plt.xlabel('Valores')
x = np.arange(z1, z2, 0.001)
x_all = np.arange(-10, 10, 0.001)
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
	#Como podemos ver el porcentaje es de 6.9% lo que está mucho más abajo de 80% , por lo que el promedio 
	# es representativo del conjunto de datos, por lo tanto el conjunto de datos es homogeneo.

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

	# El codigo anterior sirve para agrupar datos, y se extrajo de:
	# https://es.stackoverflow.com/questions/40830/cómo-hacer-una-tabla-de-distribución-de-frecuencias-con-python

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

plt.title("Funcion de Densidad de Probabilidad en datos no agrupados\n Z = (x - μ)/σ , μ = 261.56 , σ = 18.0407, x =[221,300] ")
plt.ylabel('Probabilidad')
plt.xlabel('Valores')
x = np.arange(z1, z2, 0.001)
x_all = np.arange(-10, 10, 0.001)
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

	# Como podemos ver el porcentaje es de 6.9% lo que está mucho más abajo de 80% , por lo que el promedio 
	# es representativo del conjunto de datos, por lo tanto el conjunto de datos es homogeneo.

	# RESPUESTA: Solo un 6.897290415506971% 


#Pregunta 3	

base = pd.read_csv('NAC_2017.csv', encoding='latin-1', sep = ';')
base = pd.DataFrame(base)


	# P3.A
	# Podemos inferir que una población se distribuye de una forma normal.
	# Vamos a seleccionar de la tabla las variables:[SEMANAS,PESO,EDAD_P,EDAD_M,TALLA,HIJ_TOTAL]
	# Entonces vamos a eliminar las otras columnas.
	# LAs columnas que se eliminaron, fueron en genral por dor razones:
	#		1. Debido a que  eran cualitativas,pero expresadas en numeros,por ejemplo, en sexo, eran dos valores numericos, 1 y 2, correspondiente a hombre y mujer..
	#			y/o
	#		2. Tenian datos erroneos, como por ejemplo, cantidad de hijos = 99, lo que "ensuciaba" el analisis

base = base.drop(['SEXO','DIA_NAC','MES_NAC','TIPO_PARTO','ANO_NAC','ATENC_PART','LOCAL_PART','CURSO_P','NIVEL_P','ACTIV_P','OCUPA_P','CATEG_P','EST_CIVI_M','CURSO_M','NIVEL_M','ACTIV_M','OCUPA_M','CATEG_M','COMUNA','URBA_RURAL','HIJ_VIVOS','HIJ_FALL','HIJ_MORT','REG_RES','SERV_RES','ESTAB','NAC_MA'],axis = 1)
print(base)

# Aqui obtenemos el vector esperanza de nuestras variables cuantitativas.
Vector_Esperanza = [base["SEMANAS"].mean(),base["PESO"].mean(),base["EDAD_P"].mean(),base["EDAD_M"].mean(),base["TALLA"].mean(),base["HIJ_TOTAL"].mean(),]
print(Vector_Esperanza)
	# Ahora para sacaremos la matriz de varianza covarianza, pero para esto, queremos que todos los datos tengan coherencia entre ellos,
	# por lo que elegimos datos del peso de la guagua, las semanas a las que nacio, talla, edad de la madre, y los hijos totales. 
	#	Creemos que los hijos totales puede ser un factor ,o tener un relacion con la edad de la madre y otros aspectos.
base2 = base
base2 = base2.drop(["EDAD_P"],axis = 1)

#obtenemos matrix varianza covarianza
Matriz_Varianza_Covarianza = base2.cov()

print
print(Matriz_Varianza_Covarianza)

	#P3.B
	# Obtenemos el grafico pedido.
plt.title("Gráfico de dispersión")
plt.ylabel('PESO')
plt.xlabel('EDAD_M')
plt.axis([5,70,0,7000])
plt.scatter(base["EDAD_M"], base["PESO"],color = "grey")

plt.show()
		# Es explicativo debido a que a mayor edad es peor el metabolismo en el humano, 
		# y puede tener más peso una persona más anciana que una joven por esos motivos.
		# Así el peso del recien nacido tambien es mayor.
		# Tambien solo los valores se encuentran entre las edades fertiles de las mujeres.


	#P4.D
	# En este paso obtenemos la matriz de correlación
Matriz_Correlacion = base.corr()
print(Matriz_Correlacion)
	
	# Como podemos ver hay variables que tienen una correlacion muy alta, 
	# como  SEMANAS y PESO, lo cual es logico, debido a que entre más grande el feto, mayor es el peso.
	# También a igual que lo  anterior tenemos SEMANAS y TALLA.
	# Ambas correlaciones son altas y positivas, lo que implican que existe una tendencia lineal positiva entre ambas variables, correspondientemente.
	# correlaciones bajas pero positivas son las de PESO y EDAD_M, PESO e HIJ_TOTAL ,
	# SEMANAS e HIJ_TOTAL , TALLA e HIJ_TOTAL, EDAD_P e HIJ_TOTAL, EDAD_M e HIJ_TOTAL lo que implican que no existe una tendencia lineal clara. 
	# Esto parece ser debido a que su relacion no es muy signifcativa, por ejemplo el peso de la guagua y la edad de la mama, no son relevantes entre ellas.
	# Por otro lado tenemos alguna correlaciones negativas bajas como por ejemplo TALLA Y EDAD_M, que no tienen mucha relacion.




     

     