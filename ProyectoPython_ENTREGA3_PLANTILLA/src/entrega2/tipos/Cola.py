'''
Created on 21 oct 2024

@author: belenvegmar
'''


from __future__ import annotations
from typing import TypeVar
from entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')


class Cola(Agregado_lineal[E]):
    
    
    def __init__(self)->None:
        super().__init__()
        
        
        
        
    @staticmethod
    def of()->Cola[E]:
        return Cola()
    

    
    def add(self,e:E)->None:
        self._elements.append(e)
        
    
    def __str__(self) -> str:
        return f"Cola({self.elements()})"
        