'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from typing import TypeVar
from entrega3.Recorrido import Recorrido
from entrega3.Grafo import Grafo
from entrega2.tipos.Pila import Pila

V = TypeVar('V')
E = TypeVar('E')

class Recorrido_en_profundidad(Recorrido[V,E]):
    
    @staticmethod
    def of(grafo: Grafo[V,E]) -> Recorrido_en_profundidad[V,E]:
        return Recorrido_en_profundidad(grafo)
    
    def __init__(self, grafo: Grafo[V,E]) -> None:
        super().__init__(grafo)
        
    def traverse(self, source: V) -> None:
        # Inicializar las estructuras de datos
        visitados = set()
        pila = Pila[V]()
        
        # Añadir el vértice inicial
        pila.push(source)
        
        while not pila.is_empty():
            vertice = pila.pop()
            
            if vertice not in visitados:
                # Marcar como visitado
                visitados.add(vertice)
                
                # Procesar el vértice
                self._process_vertex(vertice, visitados)
                
                # Obtener los sucesores no visitados
                sucesores = self._graph.successors(vertice)
                
                # Añadir los sucesores no visitados a la pila
                for sucesor in sucesores:
                    if sucesor not in visitados:
                        # Procesar la arista
                        self._process_edge(vertice, sucesor)
                        pila.push(sucesor)
    
    def _process_vertex(self, vertex: V, visited: set[V]) -> None:
        """
        Procesa un vértice durante el recorrido.
        Actualiza las estructuras de datos del recorrido.
        """
        # Actualizar el orden de visita
        self._visit_order.append(vertex)
        
        # Si es el primer vértice, es la raíz
        if len(self._visit_order) == 1:
            self._tree_roots.add(vertex)
        
    def _process_edge(self, source: V, target: V) -> None:
        """
        Procesa una arista durante el recorrido.
        Actualiza las estructuras de datos del recorrido.
        """
        # Añadir la arista al árbol de recorrido
        if target not in self._tree_edges:
            self._tree_edges[target] = source

if __name__ == '__main__':
    # Ejemplo de uso
    from entrega3.Grafo import E_grafo, Graph_type
    
    # Crear un grafo de ejemplo
    g = E_grafo[str, str](Graph_type.DIRECTED)
    g.add_edge("A", "B", "e1")
    g.add_edge("B", "C", "e2")
    g.add_edge("C", "D", "e3")
    g.add_edge("A", "D", "e4")
    g.add_edge("D", "E", "e5")
    
    # Crear el recorrido en profundidad
    dfs = Recorrido_en_profundidad.of(g)
    
    # Realizar el recorrido desde el vértice "A"
    dfs.traverse("A")
    
    # Mostrar resultados
    print("Orden de visita:", dfs.visit_order())
    print("Raíces del árbol:", dfs.tree_roots())
    print("Aristas del árbol:", dfs.tree_edges())