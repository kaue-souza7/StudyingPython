# ***/// MAPEAMENTO DE DADOS EM LIST COMPREHENSION \\\***
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis
# print(list(range(10)))
import pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# print(*produtos, sep="\n")
print()
print()

# aumentando_preco

aumentar_preco = [
    {**produto, 'preco': produto['preco'] * 1.1}
    if produto['preco'] > 20 else {**produto}
    # {**produto, 'preco': produto['preco'] - (produto['preco'] * 0.05)}
    # {'nome': produto['nome'], 'preco': produto['preco'] * 2}
    for produto in produtos
]



# print(*aumentar_preco, sep="\n")



# pprint.pprint(aumentar_preco, sort_dicts=False, width=40)
# p(aumentar_preco)


#   ***/// O QUE VEM NA ESQUERDA DO FOR É MAPEAMENTO \\\***
#   ***/// O QUE VEM NA DIREITA DO FOR É FILTRO \\\***

# lista = [n for n in range(10) if n < 5]

# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]

aumentar_preco = [
    {**produto, 'preco': produto['preco'] * 1.1}
    if produto['preco'] > 20 else {**produto}
    # {**produto, 'preco': produto['preco'] - (produto['preco'] * 0.05)}
    # {'nome': produto['nome'], 'preco': produto['preco'] * 2}
    for produto in produtos
    if produto['preco'] > 10
]

p(aumentar_preco)