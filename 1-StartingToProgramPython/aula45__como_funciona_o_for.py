"""
Iteravel -> str, range, etc (__inter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
"""
# numeros = range(0, 100, 11)

# for numero in numeros:
#     print(numero)

"""
O que eu entendi 

o iter chama o interador para interar a string, ou seja,
o iter serve para percorrer cada elemento um a um.



e o next é o que vai passar pro proximo elemento, ou seja,
vai passar pra proxima letra no caso de uma string 
"""
# *** O QUE O FOR É***
texto = 'Luiz'
for letra in texto:
    print(letra)

# ***O QUE O FOR FAZ POR TRÁS***
    
# for letra in texto
  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)


