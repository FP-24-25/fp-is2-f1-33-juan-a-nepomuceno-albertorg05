'''
Created on 11 nov 2024

@author: alber
'''
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Generic, TypeVar

E = TypeVar('E')

class Agregado_lineal(ABC, Generic[E]):
    def __init__(self):
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0

    @property
    def elements(self) -> List[E]:
        return self._elements.copy()

    @abstractmethod
    def add(self, e: E) -> None:
        pass

    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed = []
        while not self.is_empty:
            removed.append(self.remove())
        return removed
if __name__ == '__main__':
    pass