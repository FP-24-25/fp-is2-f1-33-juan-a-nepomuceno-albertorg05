'''
Created on 21 nov 2024

@author: alber
'''
class ColaConLimite:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = []

    def add(self, elemento):
        if self.is_full():
            raise OverflowError("La cola está completamente llena.")
        self.cola.append(elemento)

    def remove(self):
        if self.cola:
            return self.cola.pop(0)
        return None

    def is_full(self):
        return len(self.cola) >= self.capacidad

    @classmethod
    def of(cls, capacidad):
        return cls(capacidad)


class Agregado_Lineal:
    def __init__(self):
        self.elementos = []

    def add(self, elemento):
        self.elementos.append(elemento)

    def contains(self, e):
        return e in self.elementos

    def find(self, func):
        for elemento in self.elementos:
            if func(elemento):
                return elemento
        return None

    def filter(self, func):
        return [elemento for elemento in self.elementos if func(elemento)]


# Tests
def test_cola_con_limite():
    cola = ColaConLimite.of(3)
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")
    try:
        cola.add("Tarea 4")
    except OverflowError as e:
        print(e)  # Debe imprimir: "La cola está completamente llena."
    print(cola.remove())  # Debe imprimir: "Tarea 1"
    print(cola.is_full())  # Debe imprimir: False

def test_agregado_lineal():
    agregado = Agregado_Lineal()
    agregado.add(1)
    agregado.add(2)
    agregado.add(3)
    print(agregado.contains(2))  # Debe imprimir: True
    print(agregado.contains(4))  # Debe imprimir: False
    print(agregado.find(lambda x: x > 1))  # Debe imprimir: 2
    print(agregado.find(lambda x: x > 5))  # Debe imprimir: None
    print(agregado.filter(lambda x: x % 2 == 0))  # Debe imprimir: [2]
    print(agregado.filter(lambda x: x > 1))  # Debe imprimir: [2, 3]
    print(agregado.filter(lambda x: x > 5))  # Debe imprimir: []
    
if __name__ == '__main__':
    pass
test_cola_con_limite()
test_agregado_lineal()