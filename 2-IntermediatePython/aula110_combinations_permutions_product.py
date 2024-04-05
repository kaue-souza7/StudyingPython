# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca', 'vermelha'],
    ['p', 'm', 'g', 'gg'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))

# print_iter(product(*camisetas))

conjunto1 = [1, 2, 3]
conjunto2 = [4, 5, 6]
tamanho = 2
conjunto3 = []

for n in conjunto1:
    conjunto3.append(n)

for n in conjunto2:
    conjunto3.append(n)

print_iter(permutations(conjunto3, 2))

for i in conjunto3:
    print(i)
