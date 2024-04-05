from functools import reduce

"""
Use a função map para calcular o quadrado de cada número na lista.
Use a função filter para manter apenas os números pares.
Use a função reduce para encontrar a soma dos números pares resultantes.
"""

numbers = [15, 7, 12, 4, 9, 2, 7, 8]

number_square = map(
    lambda n: n**2,
    numbers
)

print(list(number_square))

print()
print()


def only_par_number(number):
    if number % 2 == 0:
        return number
    

numbers_par = list(filter(
    only_par_number,
    numbers
))

print(numbers_par)

print()
print()


def somando(ac, n):
    return ac + n

sum_par_number = reduce(
    somando,
    numbers_par,
    0
)

print()
print()


print(sum_par_number)
