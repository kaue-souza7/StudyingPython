"""
Exercício
Crie uma aplicação que diga o primeiro numero repetido levando em conta
o seu segundo numero. 
Caso não tenha numero repetido imprima 
na tela "não há numeros repetidos nesta lista".

"""
lista_de_listas_de_inteiros = [
    [
        [1, 2, 3, 4, 4, 3, 2, 1, 9, 10], # 4
        [4, 5, 6, 7, 8, 1, 2, 3, 0, 10], # não tem
        [2, 3, 4, 6, 0, 2, 5, 8, 1, 6], # 2
    ],
    [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # nt
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 1], # 1
        [2, 6, 3, 8, 4, 7, 0, 5, 3, 3], # 3
    ],
    [
        [5, 4, 3, 2, 7, 8, 5, 7, 9, 0], # 5
        [3, 2, 2, 3, 5, 0, 10, 3, 4, 5], # 2
        [1, 2, 0, 7, 3, 6, 0, 2, 0, 6], # 0
    ]

]

# Quando a return na função ou tem que imprimir ou guardar em uma variavel
# Se o print estiver dentro da função ja irá imprimir

"""
LÓGICA

- CRIAR UM FOR PARA PERCORRER A PRIMEIRA LISTA 
- DENTRO CRIAR OUTRO FOR PARA PERCORRER A LISTA DE INTEIROS
- DENTRO DO SEGUNDO FOR CHAMAR UMA FUNÇAO
- CRIAR UMA FUNÇAO
- CRIAR UM FOR DENTRO DA FUNÇÃO PARA PERCORRER OS NUMEROS
- CRIAR VARIAVEL DE TIPO SET() PARA GUARDAR NUMEROS JA CHECADO
- ANALISAR SE O NUMERO QUE ESTA SENDO CHECADO ESTA NA LISTA DE NUMEROS CHECADO
- SE NAO ESTIVER CONTINUE
- SE ESTIVER GUARDAR ELE DENTRO DE PRIMEIRO NUMERO REPETIDO(VARIAEL A SER CRIADA)
- 
"""

def first_repeated_number(lista_inteiros):
    checked_number = set()
    repeated_number = 'Não há numeros repetidos nesta lista!' 
    for number in lista_inteiros:
        if number in checked_number:
            repeated_number = 0
            repeated_number = number
            break
        else:
            checked_number.add(number)
            continue
    return repeated_number 


for listas in lista_de_listas_de_inteiros:
    for lista_inteiros in listas:
        print(first_repeated_number(lista_inteiros))