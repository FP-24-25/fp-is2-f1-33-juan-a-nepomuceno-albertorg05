'''
Created on 19 dic 2024

@author: alber
'''
from typing import Dict, List, Tuple
from Gen import Gen
from genagen import RelacionGenAGen

class RedGenica:
    def __init__(self):
        self.genes: Dict[str, Gen] = {}
        self.relaciones: Dict[Tuple[str, str], RelacionGenAGen] = {}

    @classmethod
    def of(cls) -> 'RedGenica':
        return cls()

    def add_gen(self, gen: Gen):
        self.genes[gen.nombre] = gen

    def add_relacion(self, relacion: RelacionGenAGen):
        key = (relacion.nombre_gen1, relacion.nombre_gen2)
        self.relaciones[key] = relacion

    @classmethod
    def parse(cls, fichero_genes: str, fichero_red: str) -> 'RedGenica':
        red = cls.of()

        # Cargar genes
        with open(fichero_genes, 'r') as f:
            for linea in f:
                gen = Gen.parse(linea)
                red.add_gen(gen)

        # Cargar relaciones
        with open(fichero_red, 'r') as f:
            for linea in f:
                relacion = RelacionGenAGen.parse(linea)
                red.add_relacion(relacion)

        return red

    def get_genes(self) -> List[Gen]:
        return list(self.genes.values())

    def get_relaciones(self) -> List[RelacionGenAGen]:
        return list(self.relaciones.values())

    def __str__(self) -> str:
        result = "Vertices:\n"
        for gen in self.get_genes():
            result += f"{gen}\n"
        result += "\nAristas:\n"
        for relacion in self.get_relaciones():
            result += f"{relacion}\n"
        return result

if __name__ == "__main__":
    # Prueba del método parse
    red = RedGenica.parse("genes", "red_genes")
    print(red)


