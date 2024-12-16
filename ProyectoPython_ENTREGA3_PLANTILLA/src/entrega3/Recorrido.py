'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from typing import Generic, TypeVar, Optional
from entrega3.Grafo import Grafo
from abc import ABC, abstractmethod

V = TypeVar('V')
E = TypeVar('E')

class Recorrido(ABC,Generic[V,E]):
    
    def __init__(self, grafo:Grafo[V,E])->None:
        self._grafo = grafo
        self._path: list[V] = []
        self._tree: dict[V,tuple[Optional[V],float]] = {}
        
    def path(self)->list[V]:
        return self._path
    
    def tree(self)->dict[V,tuple[Optional[V],float]]:
        return self._tree
    
    def path_to_origin(self, source:V)->list[V]:
        """Devuelve el camino desde el origen hasta el vértice dado"""
        if source not in self._tree:
            return []
        
        resultado: list[V] = []
        actual: V = source
        
        while actual is not None:
            resultado.append(actual)
            if self._tree[actual][0] is None:
                break
            actual = self._tree[actual][0]
            
        return resultado
    
    def path_from_origin(self, source:V)->list[V]:
        ls:list[V] = []
        v:V = source
        ls.append(v)
        nxt:tuple[Optional[V],float] = self._tree[v]
        while nxt[0] is not None:
            v = nxt[0]
            ls.insert(0,v)
            nxt = self._tree[v]
        return ls 
    
    def path_weight(self, source:V)->float:
        return self._tree[source][1] 
    
    def origin(self, source:V)->V:
        """Devuelve el vértice origen del camino que llega a source"""
        if source not in self._tree:
            return source
        
        actual: V = source
        while self._tree[actual][0] is not None:
            actual = self._tree[actual][0]
            
        return actual
    
    def path_edges(self, source:V)->list[E]:
        path:list[V] = self.path_from_origin(source)
        ls:list[E] = []
        for i in range(len(path)-1):
            ls.append(self._grafo.edge(path[i], path[i+1]))
        return ls
    
    @abstractmethod
    def traverse(self, source:V)->None:
        """Recorrerá desde un vértice específico según un método de recorrido concreto"""
        pass
    
    def traverse_all(self)->None:
        """Realiza un recorrido completo del grafo, visitando todos los vértices"""
        all_elements:set[V] = {v for v in self._grafo.vertex_set()}
        while len(all_elements) > 0:
            v:V = all_elements.pop()
            self.traverse(v)
            all_elements = all_elements - self._tree.keys()
            
    def groups(self)->dict[V,set[V]]:
        """Devuelve un diccionario que asocia cada vértice origen con el conjunto de vértices alcanzables desde él"""
        resultado: dict[V,set[V]] = {}
        
        # Primero hacemos el recorrido completo si no se ha hecho
        if not self._tree:
            self.traverse_all()
            
        # Para cada vértice en el árbol
        for vertice in self._tree.keys():
            origen = self.origin(vertice)
            
            # Si el origen no está en el diccionario, lo añadimos
            if origen not in resultado:
                resultado[origen] = set()
                
            # Añadimos el vértice al conjunto de su origen
            resultado[origen].add(vertice)
            
        return resultado
    
    def groups_list(self)->list[set[V]]:
        return list(self.groups().values())
    
    def path_exist(self, source:V, target:V)->bool:
        return self.origin(source) == self.origin(target)

if __name__ == '__main__':
    # Ejemplo de uso
    from entrega3.Grafo import E_grafo, Graph_type
    
    # Crear un grafo de ejemplo
    g = E_grafo[str, str](Graph_type.DIRECTED)
    g.add_edge("A", "B", "e1")
    g.add_edge("B", "C", "e2")
    g.add_edge("C", "A", "e3")
    g.add_edge("D", "E", "e4")
    g.add_edge("E", "F", "e5")
    
    # Crear una clase concreta que herede de Recorrido
    class RecorridoEjemplo(Recorrido[str,str]):
        def traverse(self, source: str) -> None:
            # Implementación simple para el ejemplo
            visitados = set()
            def dfs(v: str, padre: Optional[str] = None, peso: float = 0.0):
                if v not in visitados:
                    visitados.add(v)
                    self._tree[v] = (padre, peso)
                    for w in self._grafo.successors(v):
                        dfs(w, v, peso + 1)
            dfs(source)
    
    # Crear una instancia y probar los métodos
    rec = RecorridoEjemplo(g)
    rec.traverse_all()
    
    print("Grupos:", rec.groups())
    print("¿Existe camino de A a C?:", rec.path_exist("A", "C"))
    print("¿Existe camino de A a D?:", rec.path_exist("A", "D"))
    print("Camino desde origen hasta C:", rec.path_to_origin("C"))