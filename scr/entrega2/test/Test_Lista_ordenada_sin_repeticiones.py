'''
Created on 11 nov 2024

@author: alber
'''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion

def test_lista_ordenada_sin_repeticion():
    print("TEST DE LISTA ORDENADA SIN REPETICIÓN:")
    print("\n################################################")
    print("Creación de una lista con criterio de orden lambda x: -x")
    print("Se añade en este orden: 23, 47, 47, 1, 2, -3, 4, 5")
    lista = Lista_ordenada_sin_repeticion.of(lambda x: -x)
    numeros = [23, 47, 47, 1, 2, -3, 4, 5]
    for num in numeros:
        lista.add(num)
    print(f"Resultado de la lista ordenada sin repetición: {lista}")
    assert str(lista) == "ListaOrdenadaSinRepeticion([47, 23, 5, 4, 2, 1, -3])", "La lista no está correctamente ordenada o contiene repeticiones"

    print("\n################################################")
    removed = lista.remove()
    print(f"El elemento eliminado al utilizar remove(): {removed}")
    assert removed == 47, "El elemento eliminado debería ser 47"

    print("\n################################################")
    removed_all = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_all}")
    assert removed_all == [23, 5, 4, 2, 1, -3], "Los elementos eliminados no son los esperados"

    print("\n################################################")
    print("Comprobando si se añaden los números en la posición correcta...")
    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")
    assert str(lista) == "ListaOrdenadaSinRepeticion([0])", "La lista no está correctamente ordenada después de añadir 0"

    lista.add(0)  # Intentando añadir un elemento repetido
    print(f"Lista después de intentar añadir 0 de nuevo: {lista}")
    assert str(lista) == "ListaOrdenadaSinRepeticion([0])", "La lista no debería cambiar al intentar añadir un elemento repetido"

    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}")
    assert str(lista) == "ListaOrdenadaSinRepeticion([7, 0])", "La lista no está correctamente ordenada después de añadir 7"

    print("\n################################################")
    print("Probando con un criterio de orden diferente (longitud de cadenas)...")
    lista_str = Lista_ordenada_sin_repeticion.of(lambda x: len(x))
    lista_str.add("hola")
    lista_str.add("a")
    lista_str.add("mundo")
    lista_str.add("hola")  # Intentando añadir un elemento repetido
    print(f"Lista de cadenas ordenadas por longitud sin repetición: {lista_str}")
    assert str(lista_str) == "ListaOrdenadaSinRepeticion(['a', 'hola', 'mundo'])", "La lista de cadenas no está correctamente ordenada por longitud o contiene repeticiones"

    print("\n################################################")
    print("Verificando el estado de la lista...")
    print(f"Tamaño de la lista: {lista.size}")
    assert lista.size == 2, "El tamaño de la lista debería ser 2"

    print(f"¿La lista está vacía?: {lista.is_empty}")
    assert not lista.is_empty, "La lista no debería estar vacía"

    print(f"Elementos en la lista: {lista.elements}")
    assert lista.elements == [7, 0], "Los elementos en la lista no son los esperados"

    print("\n################################################")
    print("Pruebas superadas exitosamente.")

if __name__ == "__main__":
    test_lista_ordenada_sin_repeticion()