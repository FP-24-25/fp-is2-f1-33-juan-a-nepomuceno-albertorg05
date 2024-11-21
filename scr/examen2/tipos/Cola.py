'''
Created on 11 nov 2024

@author: alber
'''
from __future__ import annotations
from entrega2.tipos.Agregado_lineal import Agregado_lineal
from typing import TypeVar

E = TypeVar('E')

class Cola(Agregado_lineal[E]):
    @staticmethod
    def of() -> Cola[E]:
        return Cola()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __str__(self):
        return f"Cola({self._elements})"

if __name__ == '__main__':
    pass