# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# lista = [2, 5, 7, 9, 4, 32, 68, 94, 0, 11, 6]
# lista.sort(reverse=True)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def orderna(item):
#     print(item)
#     return item['nome']

"""
SORT - Mexe na ordem da lista original 
SORTED - Cria uma nova lista com a ordem requerida
"""

# def exibir(list):
#     for item in lista:
#         print(item)

# l1 = sorted(lista, key=lambda item: item['nome'])
# l2 = sorted(lista, key=lambda item: item['sobrenome'])

# exibir(l1)
# print()
# print()
# exibir(l2)









# ***/// EXERCITANDO \\\****

lista_produto_preco = [
    {'product': 'notebook', 'value': 2500}, 
    {'product': 'secador', 'value': 150}, 
    {'product': 'smartphone', 'value': 1800}, 
    {'product': 'bacia', 'value': 100},
    {'product': 'notebook', 'value': 3500}, 
    {'product': 'secador', 'value': 180}, 
    {'product': 'smartphone', 'value': 1200}, 
    {'product': 'bacia', 'value': 250},
    {'product': 'notebook', 'value': 2000}, 
    {'product': 'secador', 'value': 300}, 
    {'product': 'smartphone', 'value': 2100},  
    {'product': 'bacia', 'value': 80},   
]


list_one = sorted(lista_produto_preco, key=lambda item: item['product'])
list_two = sorted(lista_produto_preco, key=lambda item: item['value'])



def exibir(lista):
    for item in lista:
        print(item)

exibir(list_one)
print()
print()
exibir(list_two)
