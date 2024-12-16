'''
Created on 17 nov 2024

@author: belen
'''


from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    edad: int
    ciudad: str
    
    @staticmethod
    def of(dni: str, nombre: str, edad: int, ciudad: str) -> Usuario:
        return Usuario(dni, nombre, edad, ciudad)
    
    @staticmethod
    def parse(text: str) -> Usuario:
        # Formato esperado: dni,nombre,edad,ciudad
        partes = text.strip().split(',')
        if len(partes) != 4:
            raise ValueError(f"Formato inválido: {text}")
        return Usuario(
            dni=partes[0],
            nombre=partes[1],
            edad=int(partes[2]),
            ciudad=partes[3]
        )
    
    def __str__(self) -> str:
        return f"{self.nombre} ({self.dni})"

# Relacion.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Relacion:
    id: int
    dni1: str
    dni2: str
    interacciones: int
    dias_activa: int
    
    _next_id: int = 1  # Contador estático para IDs únicos
    
    @staticmethod
    def of(dni1: str, dni2: str, interacciones: int, dias_activa: int) -> Relacion:
        id_actual = Relacion._next_id
        Relacion._next_id += 1
        return Relacion(id_actual, dni1, dni2, interacciones, dias_activa)
    
    @staticmethod
    def parse(text: str) -> Relacion:
        # Formato esperado: dni1,dni2,interacciones,dias_activa
        partes = text.strip().split(',')
        if len(partes) != 4:
            raise ValueError(f"Formato inválido: {text}")
        return Relacion.of(
            dni1=partes[0],
            dni2=partes[1],
            interacciones=int(partes[2]),
            dias_activa=int(partes[3])
        )
    
    def __str__(self) -> str:
        return f"Relación {self.id}: {self.dni1}-{self.dni2} ({self.interacciones} interacciones)"

# Red_social.py

from entrega3.E_grafo import E_grafo, Graph_type, Traverse_type
from typing import Optional
import networkx as nx
import matplotlib.pyplot as plt

class Red_social(E_grafo[Usuario, Relacion]):
    
    def __init__(self, graph_type:Graph_type, traverse_type:Traverse_type)->None:
        super().__init__(graph_type, lambda r: r.interacciones, traverse_type)
        self.__usuarios_dni:dict[str,Usuario] = {}
    
    @staticmethod
    def of(usuarios:list[Usuario], relaciones:list[Relacion], 
           graph_type:Graph_type = Graph_type.UNDIRECTED, 
           traverse_type:Traverse_type = Traverse_type.BACK) -> Red_social:
        red = Red_social(graph_type, traverse_type)
        
        for usuario in usuarios:
            red.add_vertex(usuario)
            red.__usuarios_dni[usuario.dni] = usuario
            
        for relacion in relaciones:
            usuario1 = red.__usuarios_dni[relacion.dni1]
            usuario2 = red.__usuarios_dni[relacion.dni2]
            red.add_edge(usuario1, usuario2, relacion)
            
        return red
    
    @staticmethod
    def parse(f1:str, f2:str, 
              graph_type:Graph_type = Graph_type.UNDIRECTED, 
              traverse_type:Traverse_type = Traverse_type.BACK) -> Red_social:
        usuarios = [Usuario.parse(linea) for linea in open(f1, encoding='utf-8')]
        relaciones = [Relacion.parse(linea) for linea in open(f2, encoding='utf-8')]
        return Red_social.of(usuarios, relaciones, graph_type, traverse_type)

    def get_usuario_by_dni(self, dni:str) -> Optional[Usuario]:
        return self.__usuarios_dni.get(dni)
    
    def get_relaciones_usuario(self, usuario:Usuario) -> list[Relacion]:
        return [self.edge(usuario, vecino) for vecino in self.neighbors(usuario)]
    
    def get_usuarios_mas_activos(self, n:int=5) -> list[Usuario]:
        usuarios_interacciones = [(usuario, sum(r.interacciones for r in self.get_relaciones_usuario(usuario))) 
                                for usuario in self.vertex_set()]
        usuarios_interacciones.sort(key=lambda x: x[1], reverse=True)
        return [u for u,_ in usuarios_interacciones[:n]]
    
    def get_usuarios_mas_conectados(self, n:int=5) -> list[Usuario]:
        usuarios_conexiones = [(usuario, len(self.neighbors(usuario))) 
                             for usuario in self.vertex_set()]
        usuarios_conexiones.sort(key=lambda x: x[1], reverse=True)
        return [u for u,_ in usuarios_conexiones[:n]]
    
    def plot_graph(self) -> None:
        """Visualiza el grafo usando networkx"""
        G = nx.Graph() if self.graph_type() == Graph_type.UNDIRECTED else nx.DiGraph()
        
        # Añadir nodos
        for usuario in self.vertex_set():
            G.add_node(usuario.nombre)
        
        # Añadir aristas
        for relacion in self.edge_set():
            source = self.edge_source(relacion)
            target = self.edge_target(relacion)
            G.add_edge(source.nombre, target.nombre, 
                      weight=relacion.interacciones)
        
        # Dibujar el grafo
        pos = nx.spring_layout(G)
        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                node_size=1500, font_size=10, font_weight='bold')
        plt.title("Red Social")
        plt.show()
    
    def __str__(self) -> str:
        return f"Red Social con {len(self.vertex_set())} usuarios y {len(self.edge_set())} relaciones"

if __name__ == '__main__':
    # Ejemplo de uso
    red = Red_social.parse('datos/usuarios.txt', 'datos/relaciones.txt')
    print(red)
    
    # Mostrar usuarios más activos
    print("\nUsuarios más activos:")
    for usuario in red.get_usuarios_mas_activos(3):
        print(f"- {usuario}")
    
    # Mostrar usuarios más conectados
    print("\nUsuarios más conectados:")
    for usuario in red.get_usuarios_mas_conectados(3):
        print(f"- {usuario}")
    
    # Visualizar el grafo
    red.plot_graph()