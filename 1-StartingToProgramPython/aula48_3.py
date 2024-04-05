"""
Cuidados com dados mutáveis
= - copiado o valor (imutável)
= - aponta para o mesmo alor na memoria (mutável)
"""

lista_a = ['Luiz', 'Maria', 1, True, 1.1]
lista_b = lista_a.copy()


lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)