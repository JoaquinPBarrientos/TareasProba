# PREGUNTA 3

import scipy.stats as st
import numpy as np
import math

#P1.A
muestra = np.array([35000, 44000, 38000, 55000, 33000, 56000, 67000, 45000])
media = np.mean(muestra) #Media muestral
sigma = np.std(muestra) #Desviacion estandar muestral
n = len(muestra) #largo de la muestra
alpha = 0.02 #alpha 
gl = n - 1
n_confianza = 1 - alpha

print(sigma)
print(st.t.interval(n_confianza, gl, loc = media, scale = sigma/math.sqrt(n)))

