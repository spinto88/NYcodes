#!/usr/bin/env python
# coding: utf-8

""" Funcion para extraer la cantidad de tweets 
y retweets de una dada keyword.
En el main se puede iterar sobre diferentes keywords.
"""

def extraccion_serie_temporal(keyword, period, date2extract):

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
    data2save = open("{}-{}-{}.txt".format(period, keyword, date2extract), 'w')

    date2extract = datetime.strptime(date2extract, '%Y-%m-%d').date()
   
    with open(filename, "r") as fp:
        for line in fp:
            # Para cada linea lee el json y extrae la fecha
            json_data = json.loads(line) 
            tweet_date = (datetime.strptime(json_data['created_at'], '%a %b %d %H:%M:%S %z %Y') - timedelta(hours = 3)).date() 
            if tweet_date == date2extract:
                data2save.write(json.dumps(json_data) + '\n')
 
    # Cierra el archivo a guardar 
    data2save.close()

    # Borra el .txt extraido del comprimido
    os.system("rm -rfv {}".format(filename))

    # Comprime la data extraida
    os.system("zstd {}-{}-{}.txt".format(period, keyword, date2extract))

    # Borra la data extraida no comprimida
    os.system("rm -rfv {}-{}-{}.txt".format(period, keyword, date2extract))

    return None

 
""" Funcion main """

if __name__ == "__main__":

    keywords = ['alferdez']
    period = "201908"

    for keyword in keywords:
        extraccion_serie_temporal(keyword, period, "2019-09-01")   


