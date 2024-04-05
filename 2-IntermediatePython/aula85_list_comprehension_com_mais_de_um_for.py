import pprint

lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista = []


lista = [
    [letra for letra in 'Rebecca']
    for x in range(3)
]

pprint.pprint(lista)