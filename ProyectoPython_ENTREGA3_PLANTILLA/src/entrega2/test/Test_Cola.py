'''
Created on 21 oct 2024

@author: belenvegmar
'''

from entrega2.tipos.Cola import *


def test_add_and_size():
    print("Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5")
    cola: Cola[int] = Cola.of()
    
    cola.add_all([23, 47, 1,2,-3,4,5])
    print(f"Resultado de la cola: {cola}\n")
    
    



def test_remove_all():
    cola: Cola[int] = Cola.of()
    
    cola.add_all([23, 47, 1,2,-3,4,5])

    
    removed_elements = cola.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_elements}\n")







if __name__ == "__main__":
    
    print("TEST DE COLA:\n")
    print("############"*4)
    test_add_and_size()

    print("############"*4)
    test_remove_all()



  
