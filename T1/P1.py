import scipy.stats as st # ocupar para distribuciones
import math
#Pregubta 1

#P1.A

fa = 4 #personas/minuto pregunta a
poissa = st.poisson(fa)
pmenor3 = poissa.cdf(3) #probabilidad acumulada de x=0,1,2,3

print ("La probabilidad de que la página tenga más de 3 visitas en un minuto cualquiera es: ")
pmayor3 = 1-pmenor3 #En esto se resta 1 menos la probabilidad acumulada hasta x =3

print(pmayor3)
print("\n")


#P1.B
fb = 12 #personas/minutos b
poissb = st.poisson(fb)
pmenor5 = poissb.cdf(4) #probabilidad acumulada de x=0,1,2,3,4

print("La probabilidad de que en un intervalo de 3 minuto la página tenga un mínimo de 5 visitas: ")
pmayor5 = 1-pmenor5 #En esto se resta 1 menos la probabilidad acumulada hasta x =4
print(pmayor5)
print("\n")

 
#P1.C
n, p = 5, pmayor3 #la probabilidad de 3 visitas es la misma que en P1.A
binomc = st.binom(n, p)
pmayor2 = binomc.cdf(2)
print("Probabilidad de que la página tenga más de 3 visitas por minuto como máximo en 2 de 5 días: ")
print(pmayor2)
print("\n")


#P1.D
media, sigma = 5, math.sqrt(2) #aqui tenemos los valores de la media y de la desviacion estandar
normald = st.norm(media, sigma)
pmenor4 = normald.cdf(4)
pmenor7 = normald.cdf(7)

print ("La probabilidad de que la cantidad de visitas por minuto esté entre 4 y 7 es: ")
print(pmenor7-pmenor4)






















