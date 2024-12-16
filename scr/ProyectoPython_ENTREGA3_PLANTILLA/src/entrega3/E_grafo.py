'''
Created on 17 nov 2024

@author: belen
'''
from __future__ import annotations
from typing import TypeVar, Callable
from enum import Enum
from entrega3 import Grafo
import networkx as nx
import matplotlib.pyplot as plt

V = TypeVar('V')
E = TypeVar('E')

class Graph_type(Enum):
    UNDIRECTED = 1
    DIRECTED = 2
    

#===============================================================================
# Traverse_type -> Tipo de recorrido del grafo
#===============================================================================
class Traverse_type(Enum):
    FORWARD = 1
    BACK = 2

class E_grafo(Grafo[V,E]):
    
    def __init__(self,graph_type:Graph_type,weight:Callable[[E],float],traverse_type:Traverse_type=Traverse_type.FORWARD)->None:
        self._vertex_set:set[V] = set() # Conjunto de vértices del grafo (nodos)
        self._edge_set:set[E] = set() # Conjunto de aristas (relaciones entre nodos)
        self._edges_dict:dict[tuple[V,V],E] = {}  # Diccionario que mapea las parejas de vértices a las aristas
        self._neighbors:dict[V,set[V]] = {} # Diccionario que guarda los vecinos de cada vértice
        self._predecessors:dict[V,set[V]] = {} # Diccionario que guarda los predecesores (vértices anteriores) de cada vértice
        self._sources:dict[E,V] = {} # Diccionario que mapea las aristas a sus vértices de origen
        self._targets:dict[E,V] = {} # Diccionario que mapea las aristas a sus vértices de origen
        self._graph_type = graph_type # Tipo de grafo (dirigido o no dirigido)
        self._weight = weight  # Función que calcula el peso de una arista
        self._traverse_type = traverse_type # Tipo de recorrido: hacia adelante (FORWARD) o hacia atrás (BACK)
     
    def __add_neighbors(self, source:V, target:V)->None:
        #TODO
        pass
            
    def __add_predecessors(self, source:V, target:V)->None:
        #TODO
        pass

    def add_edge(self,source:V,target:V,e:E)->None:
        #TODO
        pass
    
    def edge_weight(self,sourceVertex:V, targetVertex:V) -> float:
         #TODO
        pass
    
    def add_vertex(self,vertex:V)->bool:
        #TODO
        pass
    
    def edge_source(self,e:E)->V:
        #TODO
        pass
    
    def edge_target(self,e:E)->V:
        #TODO
        pass
    
    def vertex_set(self)->set[V]:
        #TODO
        pass
     
    def edge_set(self)->set[E]:
        return self._edge_set
    
    def contains_edge(self,sourceVertex:V, targetVertex:V)->bool:
        #TODO
        pass 
     
    def neighbors(self,vertex:V)->set[V]:
        return self._neighbors.get(vertex,set())
    
    def predecessors(self,vertex:V)->set[V]:
        #TODO
        pass
        
    def successors(self,vertex:V)->set[V]:
        #TODO
        pass
    
    def edge(self,sourceVertex:V, targetVertex:V) -> E:
        return self._edges_dict[(sourceVertex,targetVertex)]
            
    def vertex_list(self)->list[V]:
        return list(self._vertex_set)
    
    def graph_type(self)->Graph_type:
        return self._graph_type
    
    def traverse_type(self)->Traverse_type:
        return self._traverse_type
    
    def weight(self)->Callable[[E],float]:
        return self._weight
    
    def inverse_graph(self)->E_grafo[V,E]:
        #TODO
        pass
    
    def subgraph(self,vertices:set[V]) -> Grafo[V,E]:
        g:E_grafo[V,E] = E_grafo(self.graph_type(),self.weight(),self.traverse_type())
        for v in vertices:
            g.add_vertex(v)
        for e in self.edge_set():
            s = self.edge_source(e)
            t = self.edge_target(e)
            if s in vertices and t in vertices:
                g.add_edge(s,t,e)
        return g
    
    def plot_graph(self):
        # Create an empty networkx graph
        G = nx.DiGraph() if self._graph_type == Graph_type.DIRECTED else nx.Graph()
    
        # Add vertices to the graph
        for vertex in self._vertex_set:
            G.add_node(vertex)
    
        # Add edges to the graph
        edge_labels: dict = {}
        for edge in self._edge_set:
            source = self.edge_source(edge)
            target = self.edge_target(edge)
            G.add_edge(source, target)
            edge_labels[(source, target)] = self._weight(edge)
    
        # Plot the graph using matplotlib
        plt.figure(figsize=(8, 8))  # You can adjust the size
        pos = nx.spring_layout(G)  # Layout for node positioning
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=12, font_weight="bold", edge_color="gray")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color="red")
        # Show the plot
        plt.title("Graph Visualization")
        plt.show()
            
    def __str__(self):
        sep = '\n'
        return f'Vertices: \n{sep.join(str(x) for x in self._vertex_set)} \nAristas: \n{sep.join(str(x) for x in self._edge_set)}'

if __name__ == '__main__':
    pass
