
"""
Peça ao usuário para inserir uma lista de números inteiros separados por espaço.
Use a função map para calcular o quadrado de cada número na lista.
Imprima os quadrados calculados.
"""

number_digited = input('Enter a list of number: ').split(" ")

number_digited_int = [
    int(number) for number in number_digited
]

square_number_of_list = map(
    lambda number: number ** 2,
    number_digited_int
)

print(list(square_number_of_list))
