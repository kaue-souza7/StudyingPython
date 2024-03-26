"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetro podem
ter valores padrão, Caso o valor nao seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código. 
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}',  x + y + z)
    else:
        print(f'{x=} {y=}',  x + y)



soma(100, 200)
soma(100, 200, 0)