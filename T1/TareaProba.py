import pandas as pd
import itertools as it
import scipy as sp
import matplotlib.pyplot as plt
import scipy.stats as st # ocupar para distribuciones



# Abrimos la BD.
data_base = pd.read_csv('data.xlsx')
data_base = pd.DataFrame(data_base)

print(data_base)