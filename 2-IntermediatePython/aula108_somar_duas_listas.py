"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]
l_soma = [l1 + l2 for l1, l2 in zip(l1, l2)]
print(l_soma)

# def soma_lista(lista1, lista2):
#     smaller_list = min(len(lista1), len(lista2))

#     return [
#         lista1[i] + lista2[i]  for i in range(smaller_list)
#     ]


# listas_somadas = soma_lista(l1, l2)
# print(listas_somadas)