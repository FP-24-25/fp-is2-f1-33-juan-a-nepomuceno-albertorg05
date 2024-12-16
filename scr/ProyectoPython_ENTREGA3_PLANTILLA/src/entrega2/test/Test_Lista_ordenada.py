'''
Created on 21 oct 2024

@author: belenvegmar
'''

from entrega2.tipos.Lista_ordenada import *
from _operator import index

def test_add_and_size():
    print("Creación de una lista con criterio de orden lambda x: x")
    print("Se añade en este orden: 3, 1, 2")
    order_function = lambda x: x
    lista = Lista_ordenada.of(order_function)
    
    lista.add(3)
    lista.add(1)
    lista.add(2)
    print(f"Resultado de la lista: {lista}\n")
    
    


def test_remove():
    
    order_function = lambda x: x
    lista = Lista_ordenada.of(order_function)
    
    lista.add(3)
    lista.add(1)
    lista.add(2)
    
    removed = lista.remove()
    print(f"El elemento eliminado al utilizar remove(): {removed}\n")



def test_remove_all():
    order_function = lambda x: x
    lista = Lista_ordenada.of(order_function)
    
    lista.add(3)
    lista.add(1)
    lista.add(2)
    
    removed_elements = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_elements}\n")


def test_add_order():
    order_function = lambda x: x
    lista = Lista_ordenada.of(order_function)
    
    lista.add(3)
    lista.add(1)
    lista.add(2)
    
    
    print("Comprobando si se añaden los números en la posición correcta...")
    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")
    lista.add(10)
    print(f"Lista después de añadirle el 10: {lista}")
    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}\n")





if __name__ == "__main__":
    
    print("TEST DE LISTA ORDENADA:\n")
    print("############"*4)
    test_add_and_size()

    print("############"*4)
    test_remove()
    print("############"*4)
    test_remove_all()
    print("############"*4)
    test_add_order()
    
    
    
    print("Creación de una lista con criterio de orden lambda x: x")
    print("Se añade en este orden: 3, 1, 2")
    order_function = lambda x: x
    lista = Lista_ordenada.of(order_function)
    
    lista.add(3)
    lista.add(1)
    lista.add(2)
    print(f"Resultado de la lista: {lista}\n")
    
    print(lista.contains(3))
    

    


  
