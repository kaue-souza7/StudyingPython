import copy


from dados import produtos
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = copy.deepcopy(produtos)

novos_produtos = [
        {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in copy.deepcopy(produtos)
]






# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = copy.deepcopy(produtos)

produtos_ordenados_por_nome = sorted(
    produtos_ordenados_por_nome,
    key=lambda produto: produto['nome'],
    reverse=True
)





# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(produtos)



produtos_ordenados_por_preco = sorted(
    produtos_ordenados_por_preco,
    key=lambda produto: produto['preco']
)

print('Ordenado por preço')
print(*produtos_ordenados_por_preco, sep="\n")

print()

print('Ordenado po nome')
print(*produtos_ordenados_por_nome, sep="\n")

print()

print('Produtos com aumento')
print(*novos_produtos, sep="\n")
