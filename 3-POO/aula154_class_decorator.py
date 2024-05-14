# Classes decoradoras (Decorator class)

from typing import Any


class Soma:
    def __init__(self, somando):
        self._somando = somando

    def __call__(self, func):
        def interna(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'{result + self._somando} is your number!'
        return interna
    


@Soma(3)
def soma(x, y, nome):
    return x + y


print(soma(2, 3, 'João'))

