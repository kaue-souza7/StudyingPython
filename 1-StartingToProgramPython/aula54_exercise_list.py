"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar, e listar valores da sua lista
Não permita que o programa quebre com
erros de indices inexistentes na lista
"""
'''
Arroz
Feijão
Óleo
Azeite de oliva
Vinagre
Açúcar
Milho para pipoca
Farinha de trigo
Fermento em pó
Aveia

'''

lista_compras = ["Arroz",
                "Feijão",
                "Óleo",
                "Azeite de oliva",
                "Vinagre",
                "Açúcar",
                "Milho de pipoca",
                "Farinha de trigo",
                "Fermento em pó",
                "Aveia"
                ]

while True:
    acao = input(f'Você deseja: [I]nserir, [A]apagar ou [V]er lista: ').lower()

    if acao == 'i':

        valor_inserir = input('Digigte o produto que deseja adicionar: ')
        lista_compras.append(valor_inserir)

    elif acao == 'a':

        if lista_compras == []:
            print('Você não tem produtos para apagar')
            continue

        for indice, produto in enumerate(lista_compras):
            print(indice, produto)

        try:
            indice_apagar = input('Escolha o numero do produto que deseja apagar: ')
            int_indice_apagar = int(indice_apagar)

            if int_indice_apagar in range(len(lista_compras)):
                lista_compras.pop(int_indice_apagar)
                print('Produto apagado, veja abaixo como esta sua lista:')
            else: 
                print(f'Escolha um numero de 0 a {len(lista_compras) - 1}')
        except TypeError:
            print('Digte apenas o NUMEROS existentes na lista!')

    elif acao == 'v':

        if len(lista_compras) == 0:
            print('Nada em sua lista!')
        for indice, produto in enumerate(lista_compras):
            print(indice, produto)

    else:
        
        print('Digite apenas [I], [A] ou [V]!')
        