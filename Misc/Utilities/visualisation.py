# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:06:14 2023

@author: Xuzhi Brian Yang
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def draw_graph_group(G,size):
    edges, weights = zip(*nx.get_edge_attributes(G,'weight').items())
    nodes = G.nodes()
    color_map = {1:'#f09494', 2:'#eebcbc', 3:'#72bbd0', 4:'#91f0a1', 5:'#629fff', 6:'#bcc2f2',  
             7:'#eebcbc', 8:'#f1f0c0', 9:'#d2ffe7', 10:'#caf3a6', 11:'#ffdf55', 12:'#ef77aa', 
             13:'#d6dcff', 14:'#d2f5f0'}
    node_color= [color_map[d['group']] for n,d in G.nodes(data=True)]
    node_size = [d['nodesize']*10 for n,d in G.nodes(data=True)]
    pos = nx.drawing.spring_layout(G,k=0.70,iterations=60)
    plt.figure(figsize=size)
    nx.draw_networkx(G,pos=pos,node_color=node_color,node_size = node_size,
                     edge_color = weights, width = 4, edge_cmap=plt.cm.Blues)
    plt.show()
    
    
    
def draw_graph_cluster(G,labels,size):
    nodes = G.nodes()
    color_map = {1:'#f09494', 2:'#eebcbc', 3:'#72bbd0', 4:'#91f0a1', 5:'#629fff', 6:'#bcc2f2',  
             7:'#eebcbc', 8:'#f1f0c0', 9:'#d2ffe7', 10:'#caf3a6', 11:'#ffdf55', 12:'#ef77aa', 
             13:'#d6dcff', 14:'#d2f5f0'}
    # pos_spring = nx.drawing.spring_layout(G,k=0.70,iterations=60)
    # pos_gr = nx.nx_agraph.graphviz_layout(G, prog = 'neato')
    pos_gr = nx.spring_layout(G, k=0.70,iterations=60)
    plt.figure(figsize=size)
    nx.draw_networkx(G,node_color = labels,pos=pos_gr, edge_color='#629fff', arrowsize = 25, node_size = 1500, width=3.0, font_size=25, font_color='#72bbd0', font_weight="bold")
    plt.show()
    

    
def draw_graph_sim(G,size):
    nodes = G.nodes()
    edges = G.edges(data = True)
    check_weights = [x[-1] for x in edges]
    if check_weights == [{} for x in range(len(edges))]:
        weights = 0
    else:
        weights = np.array([x[-1]['weight'] for x in edges])

    color_map = {1:'#f09494', 2:'#eebcbc', 3:'#72bbd0', 4:'#91f0a1', 5:'#629fff', 6:'#bcc2f2',  
             7:'#eebcbc', 8:'#f1f0c0', 9:'#d2ffe7', 10:'#caf3a6', 11:'#ffdf55', 12:'#ef77aa', 
             13:'#d6dcff', 14:'#d2f5f0'}
    pos_gr = nx.spring_layout(G, k = 0.7)
    plt.figure(figsize=size)
    
    if np.all((weights == 0)|(weights == 1)):
        nx.draw(G, pos_gr, node_color='#ef77aa',
                with_labels = True, 
                node_size = 1500,
                edge_color = '#bcc2f2', 
                width=2.5, 
                font_size=25,
                font_color='#f1f0c0', 
                font_weight="bold",
                arrowsize = 20)
        plt.show()
    else:
        edges, weights = zip(*nx.get_edge_attributes(G,'weight').items())
        nx.draw(G, pos_gr, node_color='#ef77aa',
                with_labels = True, 
                node_size = 1500, 
                edgelist = edges, 
                edge_color = weights, 
                width=2.5, 
                edge_cmap=plt.cm.Blues, 
                font_size=25, 
                font_color='#f1f0c0', 
                font_weight="bold",
                arrowsize = 20)
        plt.show()
