import matplotlib.pyplot as plt
import networkx as nx
import random
import math
import scipy
import numpy as np

#G = nx.random_geometric_graph(5, 0.2)

#A = {0: [2, 29], 1: [2], 2: [0, 1, 3], 3: [5, 2], 4: [5], 5: [3, 4, 6], 6: [8, 5], 7: [8], 8: [6, 7, 9], 9: [11, 8], 10: [11], 11: [9, 10, 12], 12: [14, 11], 13: [14], 14: [12, 13, 15], 15: [17, 14], 16: [17], 17: [15, 16, 18], 18: [20, 17], 19: [20], 20: [18, 19, 21], 21: [23, 20], 22: [23], 23: [21, 22, 24], 24: [26, 23], 25: [26], 26: [24, 25, 27], 27: [29, 26], 28: [29], 29: [27, 28, 0]}
#G = nx.from_dict_of_lists(A)


#G = nx.random_geometric_graph(n, 0.2)
G = nx.cycle_graph(5)
#for y in G:
#    G.nodes[y]['viz'] = {"position": {"x": G.nodes[y]['pos'][0], "y": G.nodes[y]['pos'][1], "z": 0.0}}
#    del (G.nodes[y]['pos'])

#G.remove_nodes_from(list(nx.isolates(G)))

#for x in A:
#    print(str(x)+':'+str(A[x]))

#print(G.graph["partition"])
#print(G.graph["partition"][0])


#print(list(G.nodes))

nx.write_gexf(G, "superTest.gexf")

#print(nx.adjacency_matrix(G))
