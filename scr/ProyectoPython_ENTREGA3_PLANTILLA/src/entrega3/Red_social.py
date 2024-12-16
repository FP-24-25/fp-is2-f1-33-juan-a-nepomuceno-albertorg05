'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from entrega3.E_grafo import E_grafo, Graph_type, Traverse_type
from entrega3.Usuario import Usuario
from entrega3.Relacion import Relacion
from us.lsi.tools.File import lineas_de_fichero, absolute_path

# Esta clase se debe ejecutar (ver el main abajo del todo)

class Red_social(E_grafo[Usuario, Relacion]):
    
    def __init__(self,graph_type:Graph_type,traverse_type:Traverse_type)->None:
        super().__init__(graph_type, lambda r: r.interacciones, traverse_type)
        self.__usuarios_dni:dict[str,Usuario] = {}
        
    
    @staticmethod
    def of() -> Red_social: # TODO: Hay que añadir los parámetros de entrada
        #TODO
        pass
    
    @staticmethod
    def parse(f1:str, f2:str, graph_type:Graph_type = Graph_type.UNDIRECTED, traverse_type: Traverse_type = Traverse_type.BACK) -> Red_social:
        #TODO
        pass

    @property
    def usuarios_dni(self)->dict[str,Usuario]:
        return self.__usuarios_dni



if __name__ == '__main__':
    # 
    rrss: Red_social = Red_social.parse('resources/usuarios.txt', 'resources/relaciones.txt')
    print(rrss.plot_graph())