'''
Created on 17 nov 2024

@author: belen
'''
from __future__ import annotations
from typing import TypeVar, Generic, Optional, Dict, Set, List
from abc import ABC, abstractmethod
from entrega3.Grafo import Grafo, Graph_type, Traverse_type

V = TypeVar('V')
E = TypeVar('E')

class Recorrido(ABC, Generic[V,E]):
    """Clase abstracta base para implementar recorridos en grafos"""
    
    def __init__(self, grafo: Grafo[V,E]) -> None:
        self._grafo = grafo
        self._path: List[V] = []
        self._tree: Dict[V, tuple[Optional[V], float]] = {}
        self._visited: Set[V] = set()
        
    @abstractmethod
    def traverse(self, source: V) -> None:
        """Método abstracto para implementar el recorrido específico"""
        pass
    
    def traverse_all(self) -> None:
        """Realiza un recorrido completo del grafo"""
        vertices = self._grafo.vertex_set()
        while vertices:
            v = vertices.pop()
            if v not in self._visited:
                self.traverse(v)
            vertices -= self._visited
    
    def path(self) -> List[V]:
        """Devuelve el camino recorrido"""
        return self._path.copy()
    
    def tree(self) -> Dict[V, tuple[Optional[V], float]]:
        """Devuelve el árbol de recorrido"""
        return self._tree.copy()
    
    def path_to(self, target: V) -> List[V]:
        """Devuelve el camino hasta un vértice objetivo"""
        if target not in self._tree:
            return []
        
        result = []
        current = target
        while current is not None:
            result.append(current)
            current = self._tree[current][0]
        
        return list(reversed(result))
    
    def distance_to(self, target: V) -> float:
        """Devuelve la distancia hasta un vértice objetivo"""
        return self._tree[target][1] if target in self._tree else float('inf')
    
    def is_connected(self, v1: V, v2: V) -> bool:
        """Comprueba si dos vértices están conectados en el recorrido"""
        return self.get_root(v1) == self.get_root(v2)
    
    def get_root(self, v: V) -> V:
        """Obtiene la raíz del árbol que contiene al vértice"""
        if v not in self._tree:
            return v
        current = v
        while self._tree[current][0] is not None:
            current = self._tree[current][0]
        return current
    
    def get_components(self) -> Dict[V, Set[V]]:
        """Obtiene los componentes conexos del grafo"""
        components: Dict[V, Set[V]] = {}
        for v in self._tree:
            root = self.get_root(v)
            if root not in components:
                components[root] = set()
            components[root].add(v)
        return components

class Recorrido_en_anchura(Recorrido[V,E]):
    """Implementación del recorrido en anchura (BFS)"""
    
    @staticmethod
    def of(grafo: Grafo[V,E]) -> Recorrido_en_anchura[V,E]:
        return Recorrido_en_anchura(grafo)
    
    def traverse(self, source: V) -> None:
        from entrega2.tipos.Cola import Cola
        
        queue = Cola[V]()
        queue.add(source)
        self._tree[source] = (None, 0)
        self._visited.add(source)
        
        while not queue.is_empty():
            v = queue.remove()
            self._path.append(v)
            
            for w in self._grafo.successors(v):
                if w not in self._visited:
                    queue.add(w)
                    self._visited.add(w)
                    self._tree[w] = (v, self._tree[v][1] + 1)

class Recorrido_en_profundidad(Recorrido[V,E]):
    """Implementación del recorrido en profundidad (DFS)"""
    
    @staticmethod
    def of(grafo: Grafo[V,E]) -> Recorrido_en_profundidad[V,E]:
        return Recorrido_en_profundidad(grafo)
    
    def traverse(self, source: V) -> None:
        from entrega2.tipos.Pila import Pila
        
        stack = Pila[V]()
        stack.push(source)
        
        while not stack.is_empty():
            v = stack.pop()
            if v not in self._visited:
                self._visited.add(v)
                self._path.append(v)
                
                if v not in self._tree:
                    self._tree[v] = (None, 0)
                
                for w in reversed(list(self._grafo.successors(v))):
                    if w not in self._visited:
                        stack.push(w)
                        if w not in self._tree:
                            self._tree[w] = (v, self._tree[v][1] + 1)

if __name__ == '__main__':
    # Ejemplo de uso
    from entrega3.Grafo import E_grafo
    
    # Crear grafo de ejemplo
    g = E_grafo[str, str](Graph_type.UNDIRECTED)
    g.add_edge("A", "B", "e1")
    g.add_edge("B", "C", "e2")
    g.add_edge("C", "D", "e3")
    g.add_edge("D", "E", "e4")
    g.add_edge("F", "G", "e5")
    
    # Probar BFS
    print("Recorrido en anchura:")
    bfs = Recorrido_en_anchura.of(g)
    bfs.traverse_all()
    print("Camino:", bfs.path())
    print("Componentes:", bfs.get_components())
    
    # Probar DFS
    print("\nRecorrido en profundidad:")
    dfs = Recorrido_en_profundidad.of(g)
    dfs.traverse_all()
    print("Camino:", dfs.path())
    print("Componentes:", dfs.get_components())
    
    # Probar distancias y caminos
    print("\nPruebas de caminos:")
    print("Camino de A a D:", bfs.path_to("D"))
    print("Distancia de A a D:", bfs.distance_to("D"))
    print("¿Están A y D conectados?:", bfs.is_connected("A", "D"))
    print("¿Están A y F conectados?:", bfs.is_connected("A", "F"))