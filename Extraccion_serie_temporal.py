#!/usr/bin/env python
# coding: utf-8

"""
Este archivo extrae simplemente la fecha y hora de creación
de un tweet o un retweet dada una keyword 
para posteriomente analizar la serie
temporal.
ESTE SCRIPT SE PUEDE JUNTAR CON Analisis_serie_temporal.py
"""

import os 
import json

# Archivo a levantar
keyword = 'alferdez'
filename = '201908-{}.txt'.format(keyword)

# Descomprime los datos y extrae el .txt
os.system("zstd -d {}.zst".format(filename))


# Archivo a guardar las fechas de tweets y retweets
data2save = open("{}_ts.dat".format(keyword), 'w')

with open(filename, "r") as fp:
    for line in fp:
        # Para cada linea lee el json y extrae la fecha
        json_data = json.loads(line)
        data2save.write(json_data['created_at'] + '\n')
        
# Cierra el archivo a guardar 
data2save.close()


# Borra el .txt extraido del comprimido
os.system("rm -rfv {}".format(filename))

