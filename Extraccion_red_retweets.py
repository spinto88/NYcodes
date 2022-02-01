#!/usr/bin/env python
# coding: utf-8

def extraccion_red_retweets(keyword, period):

    """
    Esta funcion lee los tweets con una dada keyword
    y devuelve un archivo con la info de la red de retweets
    en formato "source target #retweets".
    Para levantar la red en networkx y analizar, hacer:

    import networkx as nx 

    graph = nx.read_edgelist(archivo, data = [('weight', int)], create_using=nx.DiGraph)

    donde graph es una red dirigida y pesada.
    """

    import os 
    import json

    filename = '{}-{}.txt'.format(period, keyword)
    # Descomprime los datos y extrae el .txt
    os.system("zstd -d {}.zst".format(filename))


    # Archivo a guardar las fechas de tweets y retweets
    data2save = open("aux.dat", 'w')

    with open(filename, "r") as fp:
        for line in fp:
            # Para cada linea lee el json y extrae la fecha
            json_data = json.loads(line)
            if 'retweeted_status' in json_data.keys():
                target = json_data['user']['id']
                source = json_data['retweeted_status']['user']['id']
                data2save.write('{} {}\n'.format(source,target))
            else:
                pass
                

    # Cierra el archivo a guardar 
    data2save.close()

    # Saco los pesos y ordeno el archivo, de forma tal que me quede
    # source, target, weight; donde weight es la cantidad de retweets
    os.system('sort aux.dat | uniq -c | sort -bgr > aux2.dat')

    # Borro un archivo auxiliar
    os.system('rm -rfv aux.dat')

    fp = open('{}_red_rt.dat'.format(keyword), 'w')
    with open('aux2.dat', 'r') as fp1:
        for line in fp1:
            ls = line.split()
            fp.write('{} {} {}\n'.format(ls[1], ls[2], ls[0]))
    fp.close()

    # Borro un archivo auxiliar
    os.system("rm -rfv aux2.dat")
    # Borra el .txt extraido del comprimido
    os.system("rm -rfv {}".format(filename))

""" Funcion main """

if __name__ == "__main__":

    keywords = ['alferdez', 'Espert']
    period = '201908'
       
    for keyword in keywords:
          extraccion_red_retweets(keyword, period)

