'''
Created on 21 oct 2024

@author: belenvegmar
'''
from __future__ import annotations
from typing import TypeVar, Generic
from us.lsi.tools.Types import Comparable


E = TypeVar('E')
P = TypeVar('P', bound=Comparable)

class Cola_de_prioridad(Generic[E,P]):
    
    #===========================================================================
    # PROPIEDADES
    #===========================================================================
    
    def __init__(self)->None:
        self._elements:list[E] = []
        self._priorities: list[P] = []
        
    def size(self)->int:
        return len(self._elements)
    
    def is_empty(self)->bool:
        return len(self._elements) == 0
    
    def elements(self)->list[E]:
        return self._elements
        
        
    #===========================================================================
    # OTROS MÉTODOS
    #===========================================================================
    
    def add(self,e:E,priority:P)->None:
        i:int = self._index_order(priority)
        self._elements.insert(i,e)
        self._priorities.insert(i,priority)
        
        
    def add_all(self,ls:list[tuple[E,P]])->None:
        for e in ls:
            self.add(e[0],e[1])
    
        
    def remove(self)->E:
        assert len(self._elements) > 0, 'El agregado esta vacío'
        e:E = self._elements.pop(0)
        self._priorities.pop(0)
        return e 
        

    def remove_all(self)->list[E]:
        ls:list[E] = []
        while not self.is_empty():
            ls.append(self.remove())
        return ls
    
    
    
    
    def _index_order(self,priority:P)->int:
        '''
        Obtiene el índice del elemento que es menor o igual que e y tal que el siguiente elemento es mayor que e
        '''
        ln:int = len(self._elements)
        
        if self.is_empty() or priority < self._priorities[0]:
            return 0
        if self._priorities[ln-1] <= priority:
            return ln        
        for i in range(ln):
            if self._priorities[i] <= priority and self._priorities[i + 1] > priority:
                return i+1
        return -1
    

    

    def decrease_priority(self,e:E,new_priority:P)->None:
        index:int = self._elements.index(e)
        if new_priority < self._priorities[index] :
            self.elements().pop(index)
            self._priorities.pop(index)
            self.add(e,new_priority)
            
    def __str__(self) -> str:
        cad =  ''
        for i in range(self.size()):
            elem = self._elements[i]
            prior = self._priorities[i]
            cad += f'({elem}, {prior})'
            
        return f"ColaPrioridad[{cad}]"
    

    
    
