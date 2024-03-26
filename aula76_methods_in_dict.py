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



p1 = {
    'nome': 'Sabrina',
    'sobrenome': 'Almeida Perira'
}

# print(p1.get('nome'))

# p1.pop('nome')
# print(p1)

# p1.popitem()
# print(p1)

# print(p1)


p1.update({
    'nome': 'Carlos'
})

tupla = ('nome2', 'Alfredo'),
p1.update(tupla)

print(p1)
