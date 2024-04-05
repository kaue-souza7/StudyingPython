# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.html

import sys
sys.setrecursionlimit


# def recursiva(start=0, end=4):
#     print(start, end)
#     # Caso base

#     if start >= end:
#         return end
    
    

#     # Caso recursivo 
#     # contar até chegar ao final
#     start += 1
#     return recursiva(start, end)



# print(recursiva(0, 1000))

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
    
print(factorial(5))