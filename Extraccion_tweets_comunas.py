#!/usr/bin/env python
# coding: utf-8

""" Recorre los tweets y si el mismo no es un retweet,
guarda el texto en un archivo indicado por el numero de 
comuna a la cual pertenece el autor del tweet,
comunas descritas en el archivo comunas.dat
"""

def extraccion_tweets_comunas(keyword, period, dict_comunas):

    import os 
    import json
   
    # Archivo a levantar 
    filename = '{}-{}.txt'.format(period, keyword)

    # Descomprime los datos y extrae el .txt
    os.system("zstd -d {}.zst".format(filename))
      
    with open(filename, "r") as fp:
        for line in fp:
            # Lee la linea y extrae el json 
            json_data = json.loads(line) 

            # Si no es un retweet 
            if 'retweeted_status' not in json_data.keys():
                # Id usuario
                user_id = json_data['user']['id']

                # Manejo el error en caso que el usuario no tenga identificada la comuna
                try:
                    # Archivo a guardar el texto del tweet 
                    file2save = 'tweets_comuna_{}.txt'.format(dict_comunas[user_id])
                    data2save = open(file2save, 'a')
                    data2save.write(json_data['text'] + '\n')
                    data2save.close()

                except KeyError:
                    pass
            else:
                pass

    # Borra el .txt extraido del comprimido
    os.system("rm -rfv {}".format(filename))
 
    return None

 
""" Funcion main """

if __name__ == "__main__":

    import ast

    keyword = 'alferdez'
    period = "201908"

    # Las comunas las lee desde un archivo comunas.dat que tiene el formato de un diccionario: {"usuario": "comuna"}
    dict_comunas = ast.literal_eval(open('comunas.dat', 'r').read())

    extraccion_serie_temporal(keyword, period, dict_comunas) 
