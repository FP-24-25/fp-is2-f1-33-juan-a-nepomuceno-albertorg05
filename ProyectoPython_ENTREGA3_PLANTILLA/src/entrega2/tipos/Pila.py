'''
Created on 21 oct 2024

@author: belenvegmar
'''


from __future__ import annotations
from typing import TypeVar
from entrega2.tipos.Agregado_lineal import *

E = TypeVar('E')


class Pila(Agregado_lineal[E]):
    
    @staticmethod
    def of()->Pila[E]:
        return Pila()
    
    def __init__(self)->None:
        super().__init__()
    
    def add(self,e:E)->None:
        self._elements.insert(0,e)
        
