# ***/// MAPEAMENTO DE DADOS EM LIST COMPREHENSION \\\***


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

print(*produtos, sep="\n")
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



print(*aumentar_preco, sep="\n")