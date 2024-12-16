'''
Created on 17 nov 2024

@author: belen
'''
from entrega3.Red_social import Red_social

if __name__ == '__main__':
    rrss: Red_social = Red_social.parse('resources/usuarios.txt', 'resources/relaciones.txt')

    sep = '\n'
    print("************** Nº Predecesores de cada vértice")
    print(sep.join(f'{v} -- {len(rrss.predecessors(v))}'  for v in rrss.vertex_set()))

    print("\n************** Nº Vecinos de cada vértice")
    print(sep.join(f'{v} -- {len(rrss.neighbors(v))}'  for v in rrss.vertex_set()))
    