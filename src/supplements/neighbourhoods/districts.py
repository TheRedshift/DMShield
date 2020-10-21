import matplotlib.pyplot as plt
import networkx as nx
import random
import scipy
import numpy as np

#G = nx.random_geometric_graph(5, 0.2)

G = nx.connected_caveman_graph(10, 3)

print(list(G.nodes))

for x in range(0,10):
    t = x * 3
    for y in range(0,3):
        G.nodes[t+y]["neighbourhood"] = x

nx.write_gml(G, "test.gml")

print(nx.adjacency_matrix(G))

temp = (nx.to_numpy_array(G))

for x in temp:
    print (x)