'''
Created on 11 nov 2024

@author: alber
'''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entrega2.tipos.Lista_ordenada import Lista_ordenada

def test_lista_ordenada():
    print("TEST DE LISTA ORDENADA:")
    print("\n################################################")
    print("Creación de una lista con criterio de orden lambda x: x")
    print("Se añade en este orden: 3, 1, 2")
    lista = Lista_ordenada.of(lambda x: x)
    lista.add(3)
    lista.add(1)
    lista.add(2)
    print(f"Resultado de la lista: {lista}")
    assert str(lista) == "ListaOrdenada([1, 2, 3])", "La lista no está correctamente ordenada"

    print("\n################################################")
    removed = lista.remove()
    print(f"El elemento eliminado al utilizar remove(): {removed}")
    assert removed == 1, "El elemento eliminado debería ser 1"

    print("\n################################################")
    removed_all = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_all}")
    assert removed_all == [2, 3], "Los elementos eliminados deberían ser [2, 3]"

    print("\n################################################")
    print("Comprobando si se añaden los números en la posición correcta...")
    lista.add(1)
    lista.add(2)
    lista.add(3)
    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")
    assert str(lista) == "ListaOrdenada([0, 1, 2, 3])", "La lista no está correctamente ordenada después de añadir 0"

    lista.add(10)
    print(f"Lista después de añadirle el 10: {lista}")
    assert str(lista) == "ListaOrdenada([0, 1, 2, 3, 10])", "La lista no está correctamente ordenada después de añadir 10"

    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}")
    assert str(lista) == "ListaOrdenada([0, 1, 2, 3, 7, 10])", "La lista no está correctamente ordenada después de añadir 7"

    print("\n################################################")
    print("Probando con un criterio de orden diferente (longitud de cadenas)...")
    lista_str = Lista_ordenada.of(lambda x: len(x))
    lista_str.add("hola")
    lista_str.add("a")
    lista_str.add("mundo")
    print(f"Lista de cadenas ordenadas por longitud: {lista_str}")
    assert str(lista_str) == "ListaOrdenada(['a', 'hola', 'mundo'])", "La lista de cadenas no está correctamente ordenada por longitud"

    print("\n################################################")
    print("Verificando el estado de la lista...")
    print(f"Tamaño de la lista: {lista.size}")
    assert lista.size == 6, "El tamaño de la lista debería ser 6"

    print(f"¿La lista está vacía?: {lista.is_empty}")
    assert not lista.is_empty, "La lista no debería estar vacía"

    print(f"Elementos en la lista: {lista.elements}")
    assert lista.elements == [0, 1, 2, 3, 7, 10], "Los elementos en la lista no son los esperados"

    print("\n################################################")
    print("Pruebas superadas exitosamente.")

if __name__ == "__main__":
    test_lista_ordenada()