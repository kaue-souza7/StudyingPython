# eaise - lançando exceções (erros)


"""
criar função que divide
criar função que confere se d é igual a zero
criar função que checa se o numero é int ou float
"""

def nao_aceito_zero(x):
    if x == 0:
        raise ZeroDivisionError('Todo e qualquer numero é indivisivel por 0')
    return True

def checking_int_float(x):
    type_of_x = type(x)
    if not isinstance(x, (int, float)):
        raise TypeError(
            f'"{x}" não é do tipo float ou int, '
            f'"{x}" é do tipo "{type_of_x.__name__}"'
        )


def divide(a, b):
    checking_int_float(a)
    checking_int_float(b)
    nao_aceito_zero(b)

    return a / b


print(divide(2, 'x'))