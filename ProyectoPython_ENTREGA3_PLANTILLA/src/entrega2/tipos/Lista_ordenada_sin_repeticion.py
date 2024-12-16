'''
Created on 21 oct 2024

@author: belenvegmar
'''
from __future__ import annotations
from typing import TypeVar, Callable, Generic
from entrega2.tipos.Agregado_lineal import Agregado_lineal
from us.lsi.tools.Types import Comparable


E = TypeVar('E')
R = TypeVar('R', bound=Comparable)


class Lista_ordenada_sin_repeticion(Agregado_lineal[E],Generic[E,R]):
    
    
    #===========================================================================
    # PROPIEDADES
    #===========================================================================   
    
    def __init__(self,order:Callable[[E],R])->None:
        super().__init__() 
        self.__order = order
        
    #===========================================================================
    # MÉTODOS DE FACTORÍA
    #===========================================================================      
        
    @staticmethod
    def of(order:Callable[[E],R])->Lista_ordenada_sin_repeticion[E,R]:
        return Lista_ordenada_sin_repeticion(order)
       
       
       
    #===========================================================================
    # OTROS MÉTODOS
    #===========================================================================  
    def __index_order(self,e:E)->int:
        '''
        Obtiene el índice del elemento que es menor o igual que e y tal que el siguiente elemento es mayor que e
        '''
        ln:int = len(self._elements)
        order_e:R = self.__order(e)
        
        if self.is_empty() or order_e < self.__order(self._elements[0]):
            return 0
        if self.__order(self._elements[ln-1]) <= order_e:
            return ln        
        for i in range(ln):
            if self.__order(self._elements[i]) <= order_e and self.__order(self._elements[i + 1]) > order_e:
                return i+1
        return -1
    
    def add(self,e:E)->None:
        if e not in self._elements:
            i:int = self.__index_order(e)
            self._elements.insert(i,e)
            
    def __str__(self) -> str:
        return f"ListaOrdenadaSinRepeticion({self.elements()})"