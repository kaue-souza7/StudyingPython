# Exercício - sistema de perguntas e respostas



perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for dict in perguntas:
    print('Pergunta:', dict['Pergunta'])
    print(end="\n")

    opcoes = dict['Opções']
    print('Opções:')
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')

    opcao_escolhida = input('Escolha uma opção: ')
    resposta_certa = 0
    opcao_escolhida_int = None
    qtd_opcoes = len(opcoes)
    acertou = False
    

    if opcao_escolhida.isdigit():
        opcao_escolhida_int = int(opcao_escolhida)

    if opcao_escolhida_int is not None:
        if opcao_escolhida_int >= 0 and opcao_escolhida_int < qtd_opcoes:
            if opcoes[opcao_escolhida_int] == dict['Resposta']:
                acertou = True
    if acertou:
        acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print(f'Você acertou {acertos} de 3 perguntas')
























        


        