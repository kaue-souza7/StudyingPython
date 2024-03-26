"""

Iterando strings com while
"""

string = 'Kaue costa' # Iteraveis

indices = 0
nova_letra = ''
while indices < len(string):

    nova_string = string[indices]

    nova_letra += f'*{nova_string}'
    
    indices += 1

print(nova_letra)

    
    




# letra = 'k'
# print(letra)

# letra = f'*{letra}*'
# print(letra)



