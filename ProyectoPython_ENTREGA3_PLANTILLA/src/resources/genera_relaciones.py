'''
Created on 17 nov 2024

@author: belen
'''

# Vamos a crear un archivo de texto con relaciones entre usuarios.
import random
from datetime import datetime, timedelta

# Generar relaciones de ejemplo
usuarios_dni = ["45718832U", "85707754E",
                "10115245D", "25143909I",
                "82007713N", "16274768S",
                "55039956S", "71894470A",
                "95287188O", "61832964Y",
                "76929765H", "95157732O",
                "62258675I", "87345530M",
                "60412985S", "63506915L",
                "58127458W", "56427434U",
                "92322186A", "18909774Z"]



def generar_relacion(dni1, dni2):
    """Genera una relación entre dos usuarios."""
    interacciones = random.randint(1, 100)
    dias_activa = random.randint(30, 365)
    return f"{dni1},{dni2},{interacciones},{dias_activa}\n"



if __name__ == '__main__':
    # Crear un archivo de relaciones
    archivo_relaciones = "../resources/relaciones.txt"
    
    with open(archivo_relaciones, "w") as file:
        # Generar 20 relaciones
        for _ in range(20):
            usuario1, usuario2 = random.sample(usuarios_dni, 2)
            file.write(generar_relacion(usuario1, usuario2))