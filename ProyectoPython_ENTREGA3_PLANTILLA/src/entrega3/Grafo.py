'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from typing import Generic, TypeVar, Callable
from abc import ABC, abstractmethod
from enum import Enum

V = TypeVar('V')
E = TypeVar('E')

class Graph_type(Enum):
    DIRECTED = 0
    UNDIRECTED = 1

class Traverse_type(Enum):
    DEPTH_FIRST = 0
    BREADTH_FIRST = 1

class Grafo(ABC,Generic[V,E]):
    
    @abstractmethod
    def successors(self,vertex:V)->set[V]:
        pass
    
    @abstractmethod
    def edge_weight(self,sourceVertex:V, targetVertex:V) -> float:
        pass
    
    @abstractmethod
    def edge(self,sourceVertex:V, targetVertex:V) -> E:
        pass

class E_grafo(Grafo[V,E]):
    def __init__(self, 
                 graph_type: Graph_type = Graph_type.DIRECTED,
                 weight: Callable[[E], float] = lambda e: 1,
                 traverse_type: Traverse_type = Traverse_type.DEPTH_FIRST):
        self._graph_type = graph_type
        self._weight = weight
        self._traverse_type = traverse_type
        # Estructuras de datos para almacenar el grafo
        self._vertex_set = set()
        self._edge_set = set()
        self._edges_dict = dict()
        self._neighbors = dict()
        self._predecessors = dict()
        self._sources = dict()
        self._targets = dict()

    def graph_type(self) -> Graph_type:
        return self._graph_type

    def weight(self) -> Callable[[E], float]:
        return self._weight

    def traverse_type(self) -> Traverse_type:
        return self._traverse_type

    def __add_neighbors(self, source:V, target:V)->None:
        if source not in self._neighbors:
            self._neighbors[source] = set()
        self._neighbors[source].add(target)
        if self._graph_type == Graph_type.UNDIRECTED:
            if target not in self._neighbors:
                self._neighbors[target] = set()
            self._neighbors[target].add(source)

    def __add_predecessors(self, source:V, target:V)->None:
        if target not in self._predecessors:
            self._predecessors[target] = set()
        self._predecessors[target].add(source)
        if self._graph_type == Graph_type.UNDIRECTED:
            if source not in self._predecessors:
                self._predecessors[source] = set()
            self._predecessors[source].add(target)

    def add_vertex(self, vertex:V)->bool:
        if vertex not in self._vertex_set:
            self._vertex_set.add(vertex)
            return True
        return False

    def add_edge(self, source:V, target:V, e:E)->None:
        self.add_vertex(source)
        self.add_vertex(target)
        self._edge_set.add(e)
        self._edges_dict[(source,target)] = e
        self._sources[e] = source
        self._targets[e] = target
        self.__add_neighbors(source, target)
        self.__add_predecessors(source, target)

    def vertex_set(self)->set[V]:
        return self._vertex_set

    def edge_set(self)->set[E]:
        return self._edge_set

    def edge(self, sourceVertex:V, targetVertex:V) -> E:
        if self.contains_edge(sourceVertex, targetVertex):
            return self._edges_dict[(sourceVertex,targetVertex)]
        raise ValueError("La arista no existe")

    def edge_weight(self, sourceVertex:V, targetVertex:V) -> float:
        if self.contains_edge(sourceVertex, targetVertex):
            return self._weight(self._edges_dict[(sourceVertex,targetVertex)])
        raise ValueError("La arista no existe")

    def edge_source(self, e:E)->V:
        return self._sources[e]

    def edge_target(self, e:E)->V:
        return self._targets[e]

    def contains_edge(self, sourceVertex:V, targetVertex:V)->bool:
        return (sourceVertex, targetVertex) in self._edges_dict

    def neighbors(self, vertex:V)->set[V]:
        return self._neighbors.get(vertex, set())

    def predecessors(self, vertex:V)->set[V]:
        return self._predecessors.get(vertex, set())

    def successors(self, vertex:V)->set[V]:
        return self.neighbors(vertex)

    def inverse_graph(self)->E_grafo[V,E]:
        g = E_grafo(self.graph_type(), self.weight(), self.traverse_type())
        for v in self.vertex_set():
            g.add_vertex(v)
        for e in self.edge_set():
            source = self.edge_source(e)
            target = self.edge_target(e)
            g.add_edge(target, source, e)
        return g

if __name__ == '__main__':
    # Ejemplo de uso
    g = E_grafo[str, str](Graph_type.DIRECTED)
    g.add_edge("A", "B", "e1")
    g.add_edge("B", "C", "e2")
    g.add_edge("C", "A", "e3")
    
    print("Vértices:", g.vertex_set())
    print("Aristas:", g.edge_set())
    print("Vecinos de B:", g.neighbors("B"))
    print("Predecesores de B:", g.predecessors("B"))