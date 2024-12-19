'''
Created on 19 dic 2024

@author: alber
'''
from dataclasses import dataclass

@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @classmethod
    def of(cls, nombre_gen1: str, nombre_gen2: str, conexion: float) -> 'RelacionGenAGen':
        if not -1 <= conexion <= 1:
            raise ValueError("El valor de conexión debe estar entre -1 y 1, ambos inclusive")
        return cls(nombre_gen1, nombre_gen2, conexion)

    @classmethod
    def parse(cls, cadena: str) -> 'RelacionGenAGen':
        nombre_gen1, nombre_gen2, conexion = cadena.strip().split(',')
        return cls.of(nombre_gen1, nombre_gen2, float(conexion))

    @property
    def coexpresados(self) -> bool:
        return self.conexion > 0.75

    @property
    def antiexpresados(self) -> bool:
        return self.conexion < -0.75

    def __str__(self) -> str:
        return f"RelacionGenAGen(nombre_gen1='{self.nombre_gen1}', nombre_gen2='{self.nombre_gen2}', conexion={self.conexion})"

if __name__ == "__main__":
    # Prueba del método parse
    relacion1 = RelacionGenAGen.parse("TP53,EGFR,0.5")
    print(relacion1)
    print(f"Coexpresados: {relacion1.coexpresados}")
    print(f"Antiexpresados: {relacion1.antiexpresados}")

    relacion2 = RelacionGenAGen.parse("BCL2,MYC,0.9")
    print(relacion2)
    print(f"Coexpresados: {relacion2.coexpresados}")
    print(f"Antiexpresados: {relacion2.antiexpresados}")

    relacion3 = RelacionGenAGen.parse("MSH6,EPCAM,-0.8")
    print(relacion3)
    print(f"Coexpresados: {relacion3.coexpresados}")
    print(f"Antiexpresados: {relacion3.antiexpresados}")

    # Prueba de valor fuera de rango
    try:
        RelacionGenAGen.of("GEN1", "GEN2", 1.5)
    except ValueError as e:
        print(f"Error esperado: {e}")

