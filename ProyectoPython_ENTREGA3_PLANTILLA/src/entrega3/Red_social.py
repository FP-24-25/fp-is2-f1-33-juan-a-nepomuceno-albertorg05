'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from entrega3.E_grafo import E_grafo, Graph_type, Traverse_type
from entrega3.Usuario import Usuario
from entrega3.Relacion import Relacion
from us.lsi.tools.File import lineas_de_fichero, absolute_path

class Red_social(E_grafo[Usuario, Relacion]):
    
    def __init__(self, graph_type:Graph_type, traverse_type:Traverse_type)->None:
        super().__init__(graph_type, lambda r: r.interacciones, traverse_type)
        self.__usuarios_dni:dict[str,Usuario] = {}
    
    @staticmethod
    def of(usuarios:list[Usuario], relaciones:list[Relacion], 
           graph_type:Graph_type = Graph_type.UNDIRECTED, 
           traverse_type:Traverse_type = Traverse_type.BACK) -> Red_social:
        red = Red_social(graph_type, traverse_type)
        
        # Añadir usuarios
        for usuario in usuarios:
            red.add_vertex(usuario)
            red.__usuarios_dni[usuario.dni] = usuario
            
        # Añadir relaciones
        for relacion in relaciones:
            usuario1 = red.__usuarios_dni[relacion.dni1]
            usuario2 = red.__usuarios_dni[relacion.dni2]
            red.add_edge(usuario1, usuario2, relacion)
            
        return red
    
    @staticmethod
    def parse(f1:str, f2:str, 
              graph_type:Graph_type = Graph_type.UNDIRECTED, 
              traverse_type:Traverse_type = Traverse_type.BACK) -> Red_social:
        # Leer y parsear usuarios
        usuarios = []
        for linea in lineas_de_fichero(absolute_path(f1)):
            usuarios.append(Usuario.parse(linea))
            
        # Leer y parsear relaciones
        relaciones = []
        for linea in lineas_de_fichero(absolute_path(f2)):
            relaciones.append(Relacion.parse(linea))
            
        return Red_social.of(usuarios, relaciones, graph_type, traverse_type)

    @property
    def usuarios_dni(self)->dict[str,Usuario]:
        return self.__usuarios_dni
    
    def get_usuario_by_dni(self, dni:str) -> Usuario:
        """Obtiene un usuario por su DNI"""
        return self.__usuarios_dni.get(dni)
    
    def get_relaciones_usuario(self, usuario:Usuario) -> list[Relacion]:
        """Obtiene todas las relaciones de un usuario"""
        relaciones = []
        for vecino in self.neighbors(usuario):
            relacion = self.edge(usuario, vecino)
            relaciones.append(relacion)
        return relaciones
    
    def get_usuarios_mas_activos(self, n:int=5) -> list[Usuario]:
        """Retorna los n usuarios con más interacciones"""
        usuarios_interacciones = []
        for usuario in self.vertex_set():
            total_interacciones = sum(r.interacciones for r in self.get_relaciones_usuario(usuario))
            usuarios_interacciones.append((usuario, total_interacciones))
        
        # Ordenar por número de interacciones (descendente)
        usuarios_interacciones.sort(key=lambda x: x[1], reverse=True)
        
        # Retornar los n primeros usuarios
        return [u for u,_ in usuarios_interacciones[:n]]
    
    def get_usuarios_mas_conectados(self, n:int=5) -> list[Usuario]:
        """Retorna los n usuarios con más conexiones"""
        usuarios_conexiones = []
        for usuario in self.vertex_set():
            num_conexiones = len(self.neighbors(usuario))
            usuarios_conexiones.append((usuario, num_conexiones))
        
        # Ordenar por número de conexiones (descendente)
        usuarios_conexiones.sort(key=lambda x: x[1], reverse=True)
        
        # Retornar los n primeros usuarios
        return [u for u,_ in usuarios_conexiones[:n]]
    
    def __str__(self) -> str:
        resultado = "Red Social:\n"
        resultado += f"Número de usuarios: {len(self.vertex_set())}\n"
        resultado += f"Número de relaciones: {len(self.edge_set())}\n"
        return resultado

if __name__ == '__main__':
    # Ejemplo de uso
    rrss: Red_social = Red_social.parse('resources/usuarios.txt', 'resources/relaciones.txt')
    print(rrss)
    
    # Mostrar usuarios más activos
    print("\nUsuarios más activos:")
    for usuario in rrss.get_usuarios_mas_activos():
        print(f"- {usuario.nombre}: {sum(r.interacciones for r in rrss.get_relaciones_usuario(usuario))} interacciones")
    
    # Mostrar usuarios más conectados
    print("\nUsuarios más conectados:")
    for usuario in rrss.get_usuarios_mas_conectados():
        print(f"- {usuario.nombre}: {len(rrss.neighbors(usuario))} conexiones")
    
    # Visualizar el grafo
    print("\nVisualizando el grafo...")
    print(rrss.plot_graph())