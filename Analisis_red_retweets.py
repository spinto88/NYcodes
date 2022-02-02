import networkx as nx
from community.community_louvain import best_partition
import os
import pandas as pd

path = os.getcwd()
prev_path = path.replace('NYcodes','')

keyword = 'Espert'

rt_network = pd.read_csv(prev_path+'Data_procesada/'+keyword+'_red_rt.dat',sep = ' ', header = None) #retweet network
rt_network.columns = ['source','target','weight']
G = nx.from_pandas_edgelist(rt_network,'source','target',edge_attr = 'weight')
print(nx.info(G))

partition = best_partition(G,weight='weight')

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
