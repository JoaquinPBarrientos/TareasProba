import pandas as pd
import itertools as it
import scipy as sp
import matplotlib.pyplot as plt
import scipy.stats as st # ocupar para distribuciones
import numpy as np
import math
import seaborn as sns

bbdd = pd.read_csv('NAC_2017.csv', encoding= 'latin-1', sep = ';')
bbdd = pd.DataFrame(bbdd)

#P4.A
civil = bbdd['EST_CIVI_M']
soltera = 0
casada = 0
viuda = 0
divorciada = 0
separada = 0
conviviente = 0
ignorado = 0
i = 0
for i in range(len(civil)): #vamos a recorrer toda la columna de estado civil y poder obtener las cantidades de cada estado civil
    if civil[i] == 1:
        soltera += 1
    elif civil[i] ==2:
        casada += 1
    elif civil[i] ==3:
        viuda += 1
    elif civil[i] ==4:
        divorciada += 1
    elif civil[i] ==5:
        separada += 1
    elif civil[i] ==6:
        conviviente += 1
    elif civil[i] ==7:
        ignorado += 1

print("Naciminetos de solteras: \n", soltera)
print("Naciminetos de casadas: \n", casada)
print("Naciminetos de viudas: \n", viuda)
print("Naciminetos de divorciadas: \n", divorciada)
print("Naciminetos de separadas: \n", separada)
print("Naciminetos de convivientes: \n", conviviente)
print("Naciminetos de iganorados: \n", ignorado)

cols = ('Soltera', 'Casada', 'Viuda', 'Divorciada', 'Separada', 'Conviviente', 'Ignorado')
valores = [soltera, casada, viuda, divorciada, separada, conviviente, ignorado]
plt.title("Gráfico cantidad nacimiento según estado civil")
plt.ylabel('Cantidad nacida')
plt.xlabel('Estado Civil')
plt.bar(cols, valores)
plt.show()

#P4.B
peso = bbdd['PESO']
n = 1 + 3.32 * math.log(len(peso))
mayor = max(peso)
menor = min(peso)
rango = mayor - menor
intervalo = rango / n
colspeso = np.linspace(menor, mayor, intervalo)
print (colspeso)



#P4.D
mes = bbdd['MES_NAC']
enero = 0
febrero = 0
marzo = 0
abril = 0
mayo = 0
junio = 0
julio = 0
agosto = 0
septiembre = 0
octubre = 0
noviembre = 0
diciembre = 0

for r in range(len(mes)): #vamos a recorrer toda la columna de meses y poder obtener las cantidades de cada mes
    if mes[r] == 1:
        enero += 1
    elif mes[r] == 2:
        febrero += 1
    elif mes[r] == 3:
        marzo += 1
    elif mes[r] == 4:
        abril += 1
    elif mes[r] == 5:
        mayo += 1
    elif mes[r] == 6:
        junio += 1
    elif mes[r] == 7:
        julio += 1
    elif mes[r] == 8:
        agosto += 1
    elif mes[r] == 9:
        septiembre += 1
    elif mes[r] == 10:
        octubre += 1
    elif mes[r] == 11:
        noviembre += 1
    elif mes[r] == 12:
        diciembre += 1


print("Niños nacidos en enero: \n",enero)
print("Niños nacidos en febrero: \n",febrero)
print("Niños nacidos en marzo: \n",marzo)
print("Niños nacidos en abril: \n",abril)
print("Niños nacidos en mayo: \n",mayo)
print("Niños nacidos en junio: \n",junio)
print("Niños nacidos en julio: \n",julio)
print("Niños nacidos en agosto: \n",agosto)
print("Niños nacidos en septiembre: \n",septiembre)
print("Niños nacidos en octubre: \n",octubre)
print("Niños nacidos en noviembre: \n",noviembre)
print("Niños nacidos en diciembre: \n",diciembre)

colsmes = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
valores = (enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre)
plt.title("Cantidad de nacimientos según el mes de nacimiento")
plt.ylabel('Cantidad de nacimiento')
plt.xlabel('Mes')
plt.bar(colsmes, valores)
plt.axis([0,12,0,25000])
plt.show()
