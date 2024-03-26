"""

Lista em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo1
Conhecimentos reitilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""


lista = [10, 20, 30, 40]
# del lista[2]
# numero = lista[2]
# print(numero)

lista.append(50) # adciona no fim da lista
lista.pop() # remoove o ultiimo item da lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)

print(lista, 'Removido', ultimo_valor)