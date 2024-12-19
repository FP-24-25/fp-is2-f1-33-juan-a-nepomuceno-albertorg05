'''
Created on 19 dic 2024

@author: alber
'''
from dataclasses import dataclass
from typing import ClassVar

@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_cromosoma: str

    @classmethod
    def of(cls, nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str) -> 'Gen':
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones debe ser mayor o igual que cero")
        return cls(nombre, tipo, num_mutaciones, loc_cromosoma)

    @classmethod
    def parse(cls, cadena: str) -> 'Gen':
        nombre, tipo, num_mutaciones, loc_cromosoma = cadena.strip().split(',')
        return cls.of(nombre, tipo, int(num_mutaciones), loc_cromosoma)

    def __str__(self) -> str:
        return f"{self.nombre}: ({self.tipo},{self.num_mutaciones},{self.loc_cromosoma})"

if __name__ == "__main__":
    # Prueba del método parse
    gen = Gen.parse("TP53,supresor tumoral,256,17p13.1")
    print(gen)  # Debería imprimir: TP53: (supresor tumoral,256,17p13.1)
