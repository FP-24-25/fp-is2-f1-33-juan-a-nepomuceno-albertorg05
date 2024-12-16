'''
Created on 17 nov 2024

@author: belen
'''
from __future__ import annotations
from dataclasses import dataclass



@dataclass(frozen=True)
class Relacion:
    pass
    
    @staticmethod
    def of(interacciones: int, dias_activa: int)->Relacion:
        Relacion.__xx_num+=1 # De esta manera creamos identificadores únicos
        #TODO
        pass
    
    def __str__(self):
        #TODO
        pass
    

if __name__ == '__main__':
    pass