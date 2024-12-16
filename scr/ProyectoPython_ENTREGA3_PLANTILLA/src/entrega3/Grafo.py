'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from typing import Generic, TypeVar
from abc import ABC, abstractmethod

V = TypeVar('V')
E = TypeVar('E')

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

if __name__ == '__main__':
    pass