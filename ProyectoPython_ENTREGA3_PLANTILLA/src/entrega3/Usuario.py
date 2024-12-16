'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import date
import re

@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    
    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> Usuario:
        # Validar DNI
        if not re.match(r'^\d{8}[A-Z]$', dni):
            raise ValueError(f"DNI inválido: {dni}")
        
        # Validar nombre y apellidos
        if not nombre or not apellidos:
            raise ValueError("Nombre y apellidos no pueden estar vacíos")
        
        # Validar fecha de nacimiento
        if fecha_nacimiento > date.today():
            raise ValueError("Fecha de nacimiento no puede ser futura")
        
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)
    
    @staticmethod
    def parse(linea: str) -> Usuario:
        try:
            # Formato esperado: dni,nombre,apellidos,YYYY-MM-DD
            partes = linea.strip().split(',')
            if len(partes) != 4:
                raise ValueError(f"Formato inválido: {linea}")
            
            dni = partes[0]
            nombre = partes[1]
            apellidos = partes[2]
            fecha = date.fromisoformat(partes[3])
            
            return Usuario.of(dni, nombre, apellidos, fecha)
        except ValueError as e:
            raise ValueError(f"Error al parsear línea: {linea}") from e
    
    def edad(self) -> int:
        """Calcula la edad actual del usuario"""
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellidos} ({self.dni})"

# Relacion.py
from __future__ import annotations
from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Relacion:
    id: int
    dni1: str
    dni2: str
    fecha_inicio: date
    tipo: str
    nivel_confianza: int
    
    _next_id: int = 1
    
    @staticmethod
    def of(dni1: str, dni2: str, fecha_inicio: date, tipo: str, nivel_confianza: int) -> Relacion:
        # Validar DNIs
        if not (dni1 and dni2):
            raise ValueError("DNIs no pueden estar vacíos")
        
        # Validar tipo
        tipos_validos = {'amigo', 'familiar', 'trabajo', 'conocido'}
        if tipo not in tipos_validos:
            raise ValueError(f"Tipo de relación inválido. Debe ser uno de: {tipos_validos}")
        
        # Validar nivel de confianza
        if not (1 <= nivel_confianza <= 5):
            raise ValueError("Nivel de confianza debe estar entre 1 y 5")
        
        id_actual = Relacion._next_id
        Relacion._next_id += 1
        return Relacion(id_actual, dni1, dni2, fecha_inicio, tipo, nivel_confianza)
    
    @staticmethod
    def parse(linea: str) -> Relacion:
        try:
            # Formato esperado: dni1,dni2,YYYY-MM-DD,tipo,nivel_confianza
            partes = linea.strip().split(',')
            if len(partes) != 5:
                raise ValueError(f"Formato inválido: {linea}")
            
            return Relacion.of(
                dni1=partes[0],
                dni2=partes[1],
                fecha_inicio=date.fromisoformat(partes[2]),
                tipo=partes[3],
                nivel_confianza=int(partes[4])
            )
        except ValueError as e:
            raise ValueError(f"Error al parsear línea: {linea}") from e
    
    def duracion_dias(self) -> int:
        """Calcula la duración de la relación en días hasta hoy"""
        return (date.today() - self.fecha_inicio).days
    
    def __str__(self) -> str:
        return f"Relación {self.id}: {self.dni1}-{self.dni2} ({self.tipo})"


# main.py
if __name__ == '__main__':
    # Crear la red social
    red = Red_social.parse('datos/usuarios.txt', 'datos/relaciones.txt')
    print(red)
    
    # Mostrar usuarios más activos
    print("\nUsuarios más activos:")
    for usuario in red.get_usuarios_mas_activos(3):
        print(f"- {usuario}")
        relaciones = red.get_relaciones_usuario(usuario)
        print(f"  Relaciones: {len(relaciones)}")
        for relacion in relaciones:
            print(f"  - {relacion}")
    
    # Mostrar estadísticas de la red
    print("\nEstadísticas de la red:")
    print(f"Número total de usuarios: {len(red.vertex_set())}")
    print(f"Número total de relaciones: {len(red.edge_set())}")
    
    # Buscar usuario por DNI
    dni_buscar = "45718832U"
    usuario = red.get_usuario_by_dni(dni_buscar)
    if usuario:
        print(f"\nInformación del usuario {dni_buscar}:")
        print(f"Nombre completo: {usuario.nombre} {usuario.apellidos}")
        print(f"Edad: {usuario.edad()} años")
        relaciones = red.get_relaciones_usuario(usuario)
        print(f"Número de relaciones: {len(relaciones)}")
    
    # Visualizar el grafo
    red.plot_graph()