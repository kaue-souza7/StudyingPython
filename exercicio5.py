# Validação de Entrada: 
# Implemente uma função decoradora que valide os argumentos 
# de entrada para uma função decorada. Por exemplo, 
# se a função decorada espera um número inteiro como 
# argumento, a decoradora pode verificar se o tipo de entrada é um número inteiro.

def create_function(funcao):
    def interna(*args):
        for arg in args:
            is_int_number(arg)
            result = funcao(*args)
        return result
    return interna

@create_function
def inverted_int_number(n):
    n = str(n)
    n = n[::-1]
    n = int(n)
    return n

def is_int_number(number):
    if not isinstance(number, int):
        raise TypeError('Náo é um inteiro')

inverted_int = inverted_int_number('aab')
print(inverted_int)
