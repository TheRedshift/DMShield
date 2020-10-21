import matplotlib.pyplot as plt
import networkx as nx
import random
import scipy
import numpy as np

#G = nx.random_geometric_graph(5, 0.2)

G = nx.connected_caveman_graph(10, 3)

print(list(G.nodes))

nx.write_gml(G, "test.gml")

print(nx.to_dict_of_lists(G))
