"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuario para digitar sua idade
Se o nome e idade forem digitados
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) Espaços
        Seu nome tem {n letras}
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""


nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Your name is {nome}')
    print(f'Your name inverted is: {nome[ : :-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    print(f'Seu nome tem {len(nome)} letras!')
    print(f'A primeria letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')
elif nome == '' or idade == '':
    print('Desculpe, você deixou campos vazios')




