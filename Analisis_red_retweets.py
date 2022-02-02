import networkx as nx
from community.community_louvain import best_partition
import os
import pandas as pd
from funciones import *
import json 
path = os.getcwd()
prev_path = path.replace('NYcodes','')
data_path = prev_path + 'Data_procesada/'
#keyword = 'Espert'
# Archivos a levantar
keywords = open(prev_path+'keywords.txt','r').readlines()

# Archivo a levantar    
for keyword in keywords[12::]:
    print(keyword)
    if ' ' not in keyword:
        keyword = keyword.replace('\n','')

        rt_network = pd.read_csv(data_path + keyword + '_red_rt.dat',sep = ' ', header = None) #retweet network
        rt_network.columns = ['source','target','weight']
        G = nx.from_pandas_edgelist(rt_network,'source','target',edge_attr = 'weight')
        print(nx.info(G))
        print(keyword)
        partition = best_partition(G,weight='weight')
        with open(data_path+keyword + '_red_rt_comunidades.txt','w') as fp:
            fp.write(json.dumps(partition))
        #save_dict(partition, keyword + '_red_rt_comunas',data_path) # (dictionary, name, path = '')
'''

nx.set_node_attributes(G, partition, "community")
c1 = [u for u,c in partition.items() if c ==0]
c2 = [u for u,c in partition.items() if c ==1]
c3 = [u for u,c in partition.items() if c ==2]
c4 = [u for u,c in partition.items() if c ==3]
c5 = [u for u,c in partition.items() if c ==4]

with open(prev_path + 'Data_procesada/'+ keyword+'_redrt_comuna1.txt', 'w') as f:
    for item in c1:
        f.write("%s\n" % item)

with open(prev_path + 'Data_procesada/'+ keyword+'_redrt_comuna2.txt', 'w') as f:
    for item in c2:
        f.write("%s\n" % item)

with open(prev_path + 'Data_procesada/'+ keyword+'_redrt_comuna3.txt', 'w') as f:
    for item in c3:
        f.write("%s\n" % item)

with open(prev_path + 'Data_procesada/'+ keyword+'_redrt_comuna4.txt', 'w') as f:
    for item in c4:
        f.write("%s\n" % item)
with open(prev_path + 'Data_procesada/'+keyword+'_redrt_comuna5.txt', 'w') as f:
    for item in c5:
        f.write("%s\n" % item)
print(len(c1))
print(len(c2))
'''
