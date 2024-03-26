"""
args -> Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# lembrete de desempacotamento 
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total  = 0
    for numero in args:
        # print('Numero a somar', numero, 'a', total)
        total += numero
        # print('Total', total)
    print(total)
        


soma(1, 3, 4, 5, 7, 8, 10)
soma(1, 99, 11, 60, 10)
soma(1, 3, 4, 5)

# print(1, 2, 3, 4, 5)