import pandas as pd
import itertools as it
import scipy as sp
import matplotlib.pyplot as plt
import scipy.stats as st # ocupar para distribuciones
import numpy as np


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

Vector_Esperanza = [base["SEMANAS"].mean(),base["PESO"].mean(),base["EDAD_P"].mean(),base["EDAD_M"].mean(),base["TALLA"].mean(),base["HIJ_TOTAL"].mean()]

print("El vector de esperanzas es el siguiente:",Vector_Esperanza)

	#

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


	#P3.D
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




     

     