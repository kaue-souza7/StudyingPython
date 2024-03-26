import os
# import sys
"""
criar uma funçao que receba dois numeros que os elevem ao quadrado
e retorna a soma.
Os numeros não podem ser negativos e nem float
"""
def validar_function(funcao):
    def validando(*args):

        for arg in args:
            is_positive(arg)

        for arg in args:
            is_int(arg)

        resultado = funcao(*args)
        return resultado
        
    return validando

@validar_function
def somando_ao_quadrado(x, y):
    print((x**2) + (y**2))


def is_positive(number):
    if number < 0:
        raise ValueError('A entrada não pode ser um número negativo!')

def is_int(number):
    if not isinstance(number, int):
        raise TypeError('O numero deve ser inteiro!')
    

somando_ao_quadrado(2, 2)


# def meu_decorador(funcao):
#     def validando(**kwargs):
        
#         return funcao(**kwargs)
#     return validando

# @meu_decorador
# def minha_funcao(a, b, c):
#     print(a + b + c)

# minha_funcao(a=3, b=4, c=13)







# # def validar_function(function):
# #     def valindando(*args):
# #         for arg in args:
# #             number_is_negative(arg)
# #         return function(*args)
# #     return valindando

# # @validar_function
# # def soma(x, y):
# #     print(x + y)

# # def number_is_negative(number):
# #     if number < 0:
# #         raise ValueError('AS ENTRADAS NÃO PODEM SER NEGATIVAS')


# # # validando_function = validar_function(soma)
# # # somando = validando_function(2, 1000)
# # soma(100, -20)