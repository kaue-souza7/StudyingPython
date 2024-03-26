"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input('Digite um numero: ')

try:
    numero_float = float(numero)
    print('Float:', numero_float)
    print(f'O dobro de {numero} é {numero_float*2:.2f}')
except:
    print('Isso não é numero')

# if numero.isdigit():
#     numero_float = float(numero)
#     print(f'O dobro de {numero} é {numero_float*2:.2f}')
# # else:
#     print('Isso não é numero')

