


# **** CADASTRO DE BIBLIOTECA COM WHILE ****

nome = input('Digite seu nome ou digite sair: ')
numero_inscricao = 0


while nome != 'sair':
    nome = input('Digite seu nome ou digite sair: ')
    print(f'Seu numero de inscrição é {numero_inscricao}')
    numero_inscricao = numero_inscricao + 1