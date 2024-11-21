'''
Created on 11 nov 2024

@author: alber
'''

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entrega2.tipos.Pila import Pila

def test_pila():
    print("TEST DE PILA:")
    print("\n################################################")
    print("Creación de una pila vacía")
    
    pila = Pila.of()
    
    print(f"¿La pila está vacía?: {pila.is_empty}")
    assert pila.is_empty, "La pila debería estar vacía inicialmente"
    
    print("\n################################################")
    print("Añadiendo elementos a la pila")
    
    elementos = [1, 2, 3, 4, 5]
    for elem in elementos:
        pila.add(elem)
    
    print(f"Pila después de añadir elementos: {pila}")
    assert str(pila) == "Pila([5, 4, 3, 2, 1])", "La pila no está en el orden correcto (LIFO)"
    
    print(f"Tamaño de la pila: {pila.size}")
    assert pila.size == 5, "El tamaño de la pila debería ser 5"
    
    print("\n################################################")
    print("Probando el método remove (pop)")
    
    removido = pila.remove()
    print(f"Elemento removido: {removido}")
    assert removido == 5, "El elemento removido debería ser 5 (último elemento añadido)"
    
    print(f"Pila después de remove: {pila}")
    assert str(pila) == "Pila([4, 3, 2, 1])", "La pila no está en el orden correcto después de remove"
    
    print("\n################################################")
    print("Probando el método add_all")
    
    pila.add_all([6, 7, 8])
    print(f"Pila después de add_all: {pila}")
    assert str(pila) == "Pila([8, 7, 6, 4, 3, 2, 1])", "La pila no está en el orden correcto después de add_all"
    
    print("\n################################################")
    print("Probando el método remove_all")
    
    removidos = pila.remove_all()
    print(f"Elementos removidos: {removidos}")
    assert removidos == [8, 7, 6, 4, 3, 2, 1], "Los elementos removidos no están en el orden correcto (LIFO)"
    
    print(f"¿La pila está vacía después de remove_all?: {pila.is_empty}")
    assert pila.is_empty, "La pila debería estar vacía después de remove_all"
    
    print("\n################################################")
    print("Verificando el comportamiento con diferentes tipos de datos")
    
    pila.add("Hola")
    pila.add(42)
    pila.add([1, 2, 3])
    
    print(f"Pila con diferentes tipos de datos: {pila}")
    assert str(pila) == "Pila([[1, 2, 3], 42, 'Hola'])", "La pila no maneja correctamente diferentes tipos de datos"
    
    print("\n################################################")
    print("Pruebas superadas exitosamente.")

if __name__ == '__main__':
    test_pila()