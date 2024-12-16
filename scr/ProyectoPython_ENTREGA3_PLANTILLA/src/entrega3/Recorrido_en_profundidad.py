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
    def of(grafo:Grafo[V,E])->Recorrido_en_profundidad[V,E]:
        #TODO
        pass
    
    def __init__(self,grafo:Grafo[V,E])->None:
        super().__init__(grafo)
    
    
    def traverse(self,source:V)->None:
        #TODO 
        pass    

if __name__ == '__main__':
    pass