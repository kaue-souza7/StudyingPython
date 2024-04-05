"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input('Digite um numero inteiro: ')

# try:
#     numero_int = int(numero)
#     num_par = numero_int % 2 == 0
#     if num_par:
#         print(f'O numero {numero_int} é par')
#     else:
#         print('O numero é impar')
# except:
#     print('Isto não é um numero inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""


# horas = input('Digite as horas: ')
# horas_int = int(horas)

# bom_dia = horas_int >= 0 and horas_int <= 11
# boa_tarde = horas_int >= 12 and horas_int <= 17
# boa_noite = horas_int >= 18 and horas_int <= 23

# if  bom_dia:
#     print('Bom Dia')
# if  boa_tarde:
#     print('Boa Tarde')
# if  boa_noite:
#     print('Boa Noite')

# CÓDIGO MAIS VIÁVEL

# entrada = input('Digite a hora em numeros inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Boa Tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Boa Noite')
#     else:
#         print('Não conheço esta hora')
        
# except:
#     print('Você não digitou a hora em numeros inteiros!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Digite seu primeiro nome: ')

tamanho_nome = len(primeiro_nome)
nome_curto = tamanho_nome <= 4
nome_normal = tamanho_nome == 5 or len(primeiro_nome) == 6 

if tamanho_nome > 1:
    if nome_curto:
        print('Seu nome é curto!')
    elif nome_normal:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!')
else:
    print('Digite ao menos uma letra')