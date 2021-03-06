#!/usr/bin/env python
# coding: utf-8

""" Funcion para extraer la cantidad de tweets 
y retweets de una dada keyword.
En el main se puede iterar sobre diferentes keywords.
"""

def extraccion_serie_temporal(keyword, period):

    import os 
    import json
    import pandas as pd
    from datetime import datetime
    from datetime import timedelta

    """
    Aca extrae simplemente la fecha y hora de creación
    de un tweet o un retweet dada una keyword 
    para posteriomente analizar la serie
    temporal.
    """

    # Archivo a levantar 
    filename = '{}-{}.txt'.format(period, keyword)

    # Descomprime los datos y extrae el .txt
    os.system("zstd -d {}.zst".format(filename))

    # Archivo a guardar las fechas de tweets y retweets
    data2save = open("aux_ts.dat".format(keyword), 'w')

    with open(filename, "r") as fp:
        for line in fp:
            # Para cada linea lee el json y extrae la fecha
            json_data = json.loads(line)
            data2save.write(json_data['created_at'] + '\n')
        
    # Cierra el archivo a guardar 
    data2save.close()

    # Borra el .txt extraido del comprimido
    os.system("rm -rfv {}".format(filename))

    """
    A partir de aca toma el archivo con la fecha de creación
    de los tweets o retweets y los junta por día
    (se pueden juntar eventualmente con una ventana temporal mas fina).
    Devuelve un .csv con la fecha y la cantidad de tweets o retweets
    realizados.
    """

    data = pd.read_csv('aux_ts.dat', header=None)

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

    data_resampleada.to_csv('{}_por_dia.csv'.format(keyword))

    # Borra el aux_ts.dat extraido del comprimido
    os.system("rm -rfv aux_ts.dat")

    return None


""" Funcion main """

if __name__ == "__main__":

    keywords = ['alferdez', 'Espert']
    period = "201908"

    for keyword in keywords:
        extraccion_serie_temporal(keyword, period)   


