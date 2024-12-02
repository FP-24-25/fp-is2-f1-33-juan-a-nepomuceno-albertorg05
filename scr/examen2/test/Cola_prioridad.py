'''
Created on 11 nov 2024

@author: alber
'''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entrega2.tipos.Cola_prioridad import Cola_de_prioridad

def test_cola_prioridad():
    print("TEST DE COLA DE PRIORIDAD:")
    print("\n################################################")
    print("Prueba básica con pacientes:")
    
    cola = Cola_de_prioridad[str, int]()

    # Agregar pacientes
    cola.add('Paciente A', 3)  # Dolor de cabeza leve
    cola.add('Paciente B', 2)  # Fractura en la pierna
    cola.add('Paciente C', 1)  # Ataque cardíaco

    # Verificar el estado de la cola
    print(f"Estado inicial de la cola: {cola}")
    assert cola.elements() == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de la cola es incorrecto."

    # Atender a los pacientes y verificar el orden de atención
    atencion = []
    while not cola.is_empty:
        atencion.append(cola.remove())
    
    print(f"Orden de atención: {atencion}")
    assert atencion == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de atención no es correcto."

    print("\n################################################")
    print("Pruebas adicionales:")

    # Prueba de add_all
    cola.add_all([('Paciente D', 2), ('Paciente E', 1), ('Paciente F', 3)])
    print(f"Cola después de add_all: {cola}")

    # Prueba de decrease_priority
    cola.decrease_priority('Paciente F', 0)
    print(f"Cola después de disminuir la prioridad de Paciente F: {cola}")

    # Prueba de remove_all
    removed = cola.remove_all()
    print(f"Elementos removidos con remove_all: {removed}")

    # Verificar que la cola está vacía
    assert cola.is_empty, "La cola debería estar vacía después de remove_all"

    print("\n################################################")
    print("Pruebas superadas exitosamente.")

if __name__ == '__main__':
    test_cola_prioridad()
