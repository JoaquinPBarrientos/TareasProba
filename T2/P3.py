# PREGUNTA 3

import scipy.stats as st
import numpy as np
import math


muestra = np.array([35000, 44000, 38000, 55000, 33000, 56000, 67000, 45000])
media = np.mean(muestra) #Media muestral
sigma = np.std(muestra) #Desviacion estandar muestral
n = len(muestra) #largo de la muestra
gl = n - 1
#Utilizamos t de student debido a que es una muestra pequeña y conocemos la varianza muestral
#P3.A
alpha = 0.02 #alpha 
n_confianza = 1 - alpha

print(st.t.interval(n_confianza, gl, loc = media, scale = sigma/math.sqrt(n)))

#P3.B
#NO SE RECHAZA 
alpha = 0.05
μ0 = 47000
# En este caso queremos comprobar que μ > 47 
# si t_obt > t1-aplha entonces se rechaza H0: μ>μ0

def Test_Hipostesis_P3_B(n,alpha,μ0,media,sigma):

	t_obt = (media-μ0)/(sigma/math.sqrt(n))
	gl = n - 1
	t_alpha = st.t.sf(alpha,gl)


	
	if 	t_obt > t_alpha:
		print(t_obt,"!<",t_alpha)
		print("No se rechaza H0")
	elif t_obt < t_alpha:
		print(t_obt,"<",t_alpha)
		print("Se rechaza H0")
	else:
		print("Hay algo raro")


Test_Hipostesis_P3_B(n,alpha,μ0,media,sigma)
