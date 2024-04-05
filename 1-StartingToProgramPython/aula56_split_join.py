"""

split e join com  list e str
split - divide uma string (list)
join - une uma string
"""

frase = 'Olha só que   ,    coisa interessante'
lista_frase = frase.split(',')

lista_frase_atualizada = []

for i, frase in enumerate(lista_frase):
    lista_frase[i] = lista_frase[i].strip()
    
    lista_frase_atualizada.append(lista_frase[i]) 

lista_frase_atualizada = '-'.join(lista_frase)
print (lista_frase_atualizada)