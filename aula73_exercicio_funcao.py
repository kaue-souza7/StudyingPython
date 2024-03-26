# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# def mult(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#         # print(total)

#     return total

# resultado = mult(1, 2, 3, 4, 5)
# print(resultado)



# Cire uma função que fala se um número é par ou ímpar
# Retorne se o numero é par ou impar

# def par_imp(x):
#     par = x % 2 == 0
#     if par:
#         print('O numero', x, 'é par!')
#     else:
#         print('O numero é impar')
    
# par_imp()






def par_impar(x):
    par = x % 2 == 0
    if par:
        return f'O numero {x} é par!'
    return f'O numero {x} é impar'

resultado = par_impar(3)
print(resultado)

