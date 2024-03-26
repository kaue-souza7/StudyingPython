# *****PRIMEIRO DIGITO*****

import random


for _ in range(0, 100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    # print(nove_digitos)
    # nove_digitos = '345512323'
    regressive_1 = 10


    resultado_digito_1 = 0

    for numero in nove_digitos:
        resultado_digito_1 += int(numero) * regressive_1
        regressive_1 -= 1

    primeiro_digito = (resultado_digito_1 * 10) % 11

    primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
    # print(f'O primeiro digito é: {primeiro_digito}')

    # *****SEGUNDO DIGITO*****

    dez_digitos = nove_digitos + str(primeiro_digito)
    regressive_2 = 11

    resultado_digito_2 = 0

    for number in dez_digitos:
        resultado_digito_2 += int(number) * regressive_2
        regressive_2 -= 1
    # print(resultado_digito_2)

    segundo_digito = (resultado_digito_2 * 10) % 11 

    segundo_digito = segundo_digito if segundo_digito <= 9 else 0
    # print(f'O segundo digito é: {segundo_digito}')



    novo_cpf = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
    # print(novo_cpf)

    print(novo_cpf)

