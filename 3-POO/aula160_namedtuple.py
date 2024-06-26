# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
from collections import namedtuple
from typing import NamedTuple

class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALUE', 'NAIPE']
# )
as_espada = Carta('A', 'Espada')


print(as_espada._asdict())

print(as_espada)
print(as_espada[0])
print(as_espada.valor)
print(as_espada[1])
print(as_espada.naipe)
print()
print(as_espada._fields[0])
print(as_espada._field_defaults)



for valor in as_espada:
    print(valor)