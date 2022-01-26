#!/usr/bin/env python
# coding: utf-8

"""
Este script toma el archivo con la fecha de creación
de los tweets o retweets y los junta por día 
(se pueden juntar eventualmente con una ventana temporal mas fina).
Devuelve un .csv con la fecha y la cantidad de tweets o retweets
realizados.
"""

import pandas as pd 
from datetime import datetime
from datetime import timedelta


# Archivo a leer con los tiempos de los tweets y retweets
filename = 'alferdez'

data = pd.read_csv('{}_ts.dat'.format(filename), header=None)

# Convierto los datos en formato fecha y le resto 3 horas para llevarlo a horario de argentina
data[0] = data[0].apply(lambda x: datetime.strptime(x, '%a %b %d %H:%M:%S %z %Y') - timedelta(hours = 3))

# Para resamplear, pongo el tiempo como indice y creo una columna espuria contando 1 por cada post
data.set_index(0, inplace = True)
data[1] = [1] * data.shape[0]

# Resampleo de los datos, agrupo todo en 24H
data_resampleada = data.resample('24H').sum()

# Renombro las columnas y guardo la serie temporal

data_resampleada.columns = ['#t+rt']
data_resampleada.index.name = 'date'

data_resampleada.to_csv('{}_por_dia.csv'.format(filename))

