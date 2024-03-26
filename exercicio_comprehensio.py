lista_com_dict = [
    {'produto': 'Notebook', 'valor': 2000},
    {'produto': 'Notebook', 'valor': 2040},
    {'produto': 'Notebook', 'valor': 2800},
    {'produto': 'Notebook', 'valor': 2156},
    {'produto': 'Notebook', 'valor': 2000},
    {'produto': 'Notebook', 'valor': 2200},
    {'produto': 'Notebook', 'valor': 1800},
   {'produto': 'Notebook', 'valor': 1990},
   {'produto': 'Notebook', 'valor': 2005},
   {'produto': 'Notebook', 'valor': 2900},
   {'produto': 'Notebook', 'valor': 1790},
   {'produto': 'Notebook', 'valor': 3300},
   {'produto': 'Notebook', 'valor': 3000},
   {'produto': 'Notebook', 'valor': 2900},
]


lista_com_tuple = [
    (produto['produto'], produto['valor'])
    # (chave, valor)
    for produto in lista_com_dict
        # for chave, valor in produto.items()
]

# print(lista_com_tuple)

# for produto in lista_com_tuple:

nova_lista = sorted(lista_com_tuple)

# print(nova_lista)

for produto in nova_lista:
    print(produto)

