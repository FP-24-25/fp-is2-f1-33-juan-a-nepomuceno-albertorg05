'''
Created on 21 oct 2024

@author: belenvegmar
'''

from __future__ import annotations
from typing import Generic, TypeVar, Callable
from abc import ABC, abstractmethod


E = TypeVar('E')


class Agregado_lineal(ABC,Generic[E]):
    
    #===========================================================================
    # PROPIEDADES
    #===========================================================================
    
    def __init__(self)->None:
        self._elements:list[E] = []
            
    def size(self)->int:
        return len(self._elements)
    
    def is_empty(self)->bool:
        return len(self._elements) == 0
    
    def elements(self)->list[E]:
        return self._elements

            
    #===========================================================================
    # OTROS MÉTODOS
    #===========================================================================
    @abstractmethod
    def add(self,e:E)->None:
        pass
        
    def add_all(self,ls:list[E])->None:
        for e in ls:
            self.add(e)
    
    def remove(self)->E:  
        assert len(self._elements) > 0, 'El agregado esta vacío'
        return self._elements.pop(0) 
    
    def remove_all(self)->list[E]:
        ls:list[E] = []
        while not self.is_empty():
            ls.append(self.remove())
        return ls
    
    
    def contains(self, e: E) -> bool:
        return e in self._elements
    
    def find(self, func: Callable[[E], bool]) -> E | None:
        for e in self._elements:
            if func(e):
                return e
        return None
    
    
    def filter(self, func: Callable[[E], bool]) -> list[E]:

        lista = []
        for elem in self._elements:
            if func(elem):
                lista.append(elem)
        return lista
    


