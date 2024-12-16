'''
Created on 17 nov 2024

@author: belen
'''
from __future__ import annotations
from typing import TypeVar
from entrega3.Grafo import Grafo
from entrega2.tipos.Cola import Cola
from entrega3.Recorrido import Recorrido

V = TypeVar('V')
E = TypeVar('E')


class Recorrido_en_anchura(Recorrido[V,E]):
    
    @staticmethod
    def of(grafo:Grafo[V,E])->Recorrido_en_anchura[V,E]:
        return Recorrido_en_anchura(grafo)
    
    def __init__(self,grafo:Grafo[V,E])->None:
        super().__init__(grafo)
    
    def traverse(self,source:V)->None:
        v:V = source
        q:Cola[V] = Cola.of()
        q.add(v)
        self._tree[v] = (None,0)
        while not q.is_empty():
            v = q.remove()
            self._path.append(v) 
            for neighbor in self._grafo.successors(v):
                if neighbor not in self._tree:
                    q.add(neighbor)
                    self._tree[neighbor] = (v, self._tree[v][1] + 1)
   

if __name__ == '__main__':
    pass