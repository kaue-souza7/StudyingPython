"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# cpf_digitado = ('746.824.890-70')
# if len(cpf_digitado) > 11:
#     cpf_sem_traco = cpf_digitado.split('-')
#     cpf_sem_ponto = cpf_sem_traco[0].split('.')

#     cpf = ''.join(cpf_sem_ponto)
    # print(cpf)

# *****PRIMEIRO DIGITO*****

import re
import sys



# cpf_enviado = '746.824.890-70' \
#     .replace('.', '') \
#     .replace('-', '')
entrada = input('Digite seu CPF: ')
cpf_enviado = re.sub(
    r'[^0-9]',
    '',
    entrada
    )

entrada_e_squencial = entrada == entrada[0] * len(entrada)
if entrada_e_squencial:
    print('Você enviou dados sequenciais!')
    sys.exit()
    



nove_digitos = cpf_enviado[:9]
regressive_1 = 10


resultado_digito_1 = 0

for numero in nove_digitos:
    resultado_digito_1 += int(numero) * regressive_1
    regressive_1 -= 1

primeiro_digito = (resultado_digito_1 * 10) % 11

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
# print(f'O primeiro digito é: {primeiro_digito}')

# *****SEGUNDO DIGITO*****

dez_digitos = cpf_enviado[:10]
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
validation = 'CPF valid!' if novo_cpf == cpf_enviado else 'CPF invalid'
print(validation)


"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""


    











