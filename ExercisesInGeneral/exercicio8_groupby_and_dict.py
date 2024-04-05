from itertools import groupby
import copy

alunos = [
    {"nome": "Ana", "nota": 8},
    {"nome": "João", "nota": 7},
    {"nome": "Maria", "nota": 6},
    {"nome": "Pedro", "nota": 9},
    {"nome": "Carla", "nota": 5},
    {"nome": "Rafael", "nota": 8},
    {"nome": "Julia", "nota": 7},
    {"nome": "Marcos", "nota": 6},
    {"nome": "Luisa", "nota": 9},
    {"nome": "Miguel", "nota": 5},
    {"nome": "Ana", "nota": 8},
    {"nome": "João", "nota": 7},
    {"nome": "Maria", "nota": 6},
    {"nome": "Pedro", "nota": 9},
    {"nome": "Carla", "nota": 5},
    {"nome": "Rafael", "nota": 8},
    {"nome": "Julia", "nota": 7},
    {"nome": "Marcos", "nota": 6},
    {"nome": "Luisa", "nota": 9},
    {"nome": "Miguel", "nota": 5},
    {"nome": "Ana", "nota": 8},
    {"nome": "João", "nota": 7},
    {"nome": "Maria", "nota": 6},
    {"nome": "Pedro", "nota": 9},
    {"nome": "Carla", "nota": 5},
    {"nome": "Rafael", "nota": 8},
    {"nome": "Julia", "nota": 7},
    {"nome": "Marcos", "nota": 6},
    {"nome": "Luisa", "nota": 9},
    {"nome": "Miguel", "nota": 5},
    {"nome": "Ana", "nota": 8},
    {"nome": "João", "nota": 7},
    {"nome": "Maria", "nota": 6},
    {"nome": "Pedro", "nota": 9},
    {"nome": "Carla", "nota": 5},
    {"nome": "Rafael", "nota": 8},
    {"nome": "Julia", "nota": 7},
    {"nome": "Marcos", "nota": 6},
    {"nome": "Luisa", "nota": 9},
    {"nome": "Miguel", "nota": 5},
    {"nome": "Ana", "nota": 8},
    {"nome": "João", "nota": 7},
    {"nome": "Maria", "nota": 6},
    {"nome": "Pedro", "nota": 9},
    {"nome": "Carla", "nota": 5},
    {"nome": "Rafael", "nota": 8},
    {"nome": "Julia", "nota": 7},
    {"nome": "Marcos", "nota": 6},
    {"nome": "Luisa", "nota": 9},
    {"nome": "Miguel", "nota": 5}
]


ordenado = sorted(alunos, key=lambda alunos: alunos['nota'], reverse=True)
grupos = groupby(ordenado, key=lambda alunos: alunos['nota'])

for key, grupo in grupos:
    print(key)
    for aluno in grupo:
        print(aluno)


# ordenado_por_nota = sorted(alunos, key=lambda alunos: alunos['nome'])
# print(*ordenado_por_nota, sep="\n")

# def ordenar_lista_por(list, ordenar_por, ordem):
#     ordenado = sorted(list, key=lambda alunos: alunos[ordenar_por], reverse=ordem)
#     print(*ordenado, sep="\n")

# def ordenar_por_nota(list, ordenar_por):
#     ordenado_por_nota = sorted(list, key=lambda alunos: alunos[ordenar_por], reverse=True)
#     print(ordenado_por_nota)
    



    

