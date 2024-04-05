# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


ordena_por_nome = sorted(alunos, key=lambda alunos: alunos['nome'])

for aluno in ordena_por_nome:
    print(aluno)

print()
print()
print()


def ordena(aluno):
    return aluno['nota']


ordenar_por_nota = sorted(alunos, key=ordena)

grupos = groupby(ordenar_por_nota, key=ordena)

for key, grupo in grupos:
    print(key)
    for aluno in grupo:
        print(aluno)