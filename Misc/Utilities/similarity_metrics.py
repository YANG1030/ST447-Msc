# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 16:08:13 2023

@author: Xuzhi Brian Yang
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

def Sorenson(A, G):
    n_nodes = A.shape[0]
    SM = np.ones((n_nodes, n_nodes))
    for i, node1 in enumerate(G.nodes()):
        for j, node2 in enumerate(G.nodes()):
            neighbors1 = [n for n in nx.neighbors(G, node1)];n_neighbors1=len(neighbors1)
            neighbors2 = [n for n in nx.neighbors(G, node2)];n_neighbors2=len(neighbors2)
            inter = list(set(neighbors1) & set(neighbors2))
            n_inter = len(inter)
            SM[i][j] = 2 * n_inter/(n_neighbors1 + n_neighbors2) # Optimize it.
    return SM


def Salton(A, G):
    n_nodes = A.shape[0]
    ST = np.ones((n_nodes, n_nodes))
    for i, node1 in enumerate(G.nodes()):
        for j, node2 in enumerate(G.nodes()):
            neighbors1 = [n for n in nx.neighbors(G, node1)];n_neighbors1=len(neighbors1)
            neighbors2 = [n for n in nx.neighbors(G, node2)];n_neighbors2=len(neighbors2)
            inter = list(set(neighbors1) & set(neighbors2))
            n_inter = len(inter)
            ST[i][j] = 2 * n_inter/(math.sqrt(n_neighbors1 * n_neighbors2))
    return ST