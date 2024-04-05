"""
Você precisa criar um decorador @validar_entrada que verifica se os 
argumentos passados para uma função são todos inteiros. Se algum argumento 
não for um número inteiro, a função deve retornar uma mensagem de erro adequada. 
Caso contrário, a função decorada deve ser executada normalmente.
"""

def create_string(funcao):
    def interna(*args):
        for arg in args:
            is_int(arg)
        result = funcao(*args)
        return result
    return interna

# @create_string
def number_is_int(*args):
    print('Number is int')

def is_int(number):
    if not isinstance(number, int):
        raise TypeError('A entrada não foi um número inteiro')

is_int_checked_param = create_string(number_is_int)
is_int_var = is_int_checked_param(2)
# print(is_int_var)





    
