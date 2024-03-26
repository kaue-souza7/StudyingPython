

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)



listando = [
    valor 
    for chave, valor in pessoa_completa.items()



]

print(listando)