"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

"""

def soma(x, y, z):
    # Definição
    print(f'{x=} {y=} | x + y = {x+y}')

# soma(3, 10)
# soma(y=2, x=1)

soma(1, 2, z=5)