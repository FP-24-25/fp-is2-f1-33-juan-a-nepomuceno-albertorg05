'''
Created on 11 nov 2024

@author: alber
'''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entrega2.tipos.Cola import Cola

def test_cola():
    print("TEST DE COLA:")
    print("\n################################################")
    print("Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5")
    
    cola = Cola.of()
    numeros = [23, 47, 1, 2, -3, 4, 5]
    cola.add_all(numeros)
    
    print(f"Resultado de la cola: {cola}")

    print("\n################################################")
    removed_all = cola.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_all}")

    print("\n################################################")
    print("Comprobando el comportamiento FIFO (First In, First Out)...")
    cola.add(10)
    cola.add(20)
    cola.add(30)
    print(f"Cola después de añadir 10, 20, 30: {cola}")
    
    removed = cola.remove()
    print(f"Elemento removido: {removed}")
    print(f"Cola después de remover un elemento: {cola}")

    print("\n################################################")
    print("Verificando el estado de la cola...")
    print(f"Tamaño de la cola: {cola.size}")
    print(f"¿La cola está vacía?: {cola.is_empty}")
    print(f"Elementos en la cola: {cola.elements}")


if __name__ == '__main__':
    pass

    test_cola()