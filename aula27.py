"""

Fatiamento de strings
 012345678 ---> ***INDÍCES***
 Olá mundo
-987654321
Fatiamenoto [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""

# variavel = input('Digite uma unic a palavra: ')
# print(f'A palavra "{variavel}" possui {len(variavel)} letras.')
# selection_position = input('Escolha a posição de uma letra partindo-a do zero: ')

# print(f'A letra da posição escolhida foi: {variavel[int(selection_position)]}')

variavel = ('Ola mundo')
print(variavel[0:len(variavel):1])

# inverteu a string
variavel = ('Ola mundo')
print(variavel[-1: :-1])

