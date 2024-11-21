'''
Created on 11 nov 2024

@author: alber
'''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entrega2.tipos.Agregado_lineal import Agregado_lineal
from typing import TypeVar

E = TypeVar('E')

# Subclase concreta de Agregado_lineal para pruebas
class AgregadoLinealConcreto(Agregado_lineal[E]):
    def add(self, e: E) -> None:
        self._elements.append(e)

def test_agregado_lineal():
    print("TEST DE AGREGADO LINEAL:")
    print("\n################################################")
    print("Creación de un agregado lineal vacío")
    
    agregado = AgregadoLinealConcreto()
    
    print(f"¿El agregado está vacío?: {agregado.is_empty}")
    assert agregado.is_empty, "El agregado debería estar vacío inicialmente"
    
    print("\n################################################")
    print("Añadiendo elementos al agregado")
    
    elementos = [1, 2, 3, 4, 5]
    agregado.add_all(elementos)
    
    print(f"Tamaño del agregado: {agregado.size}")
    assert agregado.size == 5, "El tamaño del agregado debería ser 5"
    
    print(f"Elementos en el agregado: {agregado.elements}")
    assert agregado.elements == elementos, "Los elementos en el agregado no coinciden con los añadidos"
    
    print("\n################################################")
    print("Probando el método remove")
    
    removido = agregado.remove()
    print(f"Elemento removido: {removido}")
    assert removido == 1, "El primer elemento removido debería ser 1"
    
    print(f"Tamaño del agregado después de remove: {agregado.size}")
    assert agregado.size == 4, "El tamaño del agregado debería ser 4 después de remove"
    
    print("\n################################################")
    print("Probando el método remove_all")
    
    removidos = agregado.remove_all()
    print(f"Elementos removidos: {removidos}")
    assert removidos == [2, 3, 4, 5], "Los elementos removidos no son los esperados"
    
    print(f"¿El agregado está vacío después de remove_all?: {agregado.is_empty}")
    assert agregado.is_empty, "El agregado debería estar vacío después de remove_all"
    
    print("\n################################################")
    print("Pruebas superadas exitosamente.")

if __name__ == '__main__':
    test_agregado_lineal()