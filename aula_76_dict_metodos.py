# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': '33'
}

# print(len(pessoa))

# pessoa.setdefault('idade', None)

# print(pessoa['idade'])

#chaves
# print(tuple(pessoa.keys()))

#valor
# print(tuple(pessoa.values()))

# keys and values
print(tuple(pessoa.items()))


# chave
# for chaves in pessoa.keys():
#     print(chaves)



# valor
# for values in pessoa.values():
#     print(values)



# for chave, valor in enumerate(pessoa.items()):
#     print(chave, valor)
