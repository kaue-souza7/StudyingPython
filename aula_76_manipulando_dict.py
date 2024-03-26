# Manipulando chaves e valores em dicionarios

pessoa = {}

chave_1 = 'nome'
chave_2 = 'sobrenome'
chave_3 = 'idade'


pessoa[chave_1] = 'Camila'
pessoa[chave_2] = 'Miranda'
pessoa[chave_3] = 22

print(pessoa['sobrenome'])
del pessoa['sobrenome']

# try:
#     print(pessoa['sobrenome'])
# except KeyError: 
#     print('Essa chave não está definida')


if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print('EXISTE')
