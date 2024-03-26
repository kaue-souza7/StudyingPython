# Empacotamento e
# Desempacotamento
# em dicionários


# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza'
# }

# (a1, a2), (b) = pessoa.items()

# print(a1, a2)
# print(b)

# for chave, valor in pessoa.items():
#     print(chave)


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}

# args e kwargs
# args (ja visto) (argumentos não nomeados)
# kwargs keyword arguments (argumentos nomeados)

def mostre_argumentos_nomeados(*args, **kwargs):
    print(args, ': São os args')

    for chave, valor in kwargs.items():
        print(chave, valor)



# mostre_argumentos_nomeados(nome='kaue', altura=1.80, sobrenome='Souza')
mostre_argumentos_nomeados(**pessoa_completa)


