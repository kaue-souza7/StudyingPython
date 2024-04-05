"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um codigo nao tem fim
"""

condicao = True
while condicao:
    nome = input('Qual o seu nome? ')
    print(f'O seu nome é {nome}')

    if nome == 'sair':
        break

print('ACABOU')
    