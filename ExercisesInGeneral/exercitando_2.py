vendas_meses = {
    'Janeiro': {'produto1': 100, 
                'produto2': 150, 
                'produto3': 80,
                'produto4': 110,
                'produto5': 50,
                'produto6': 55,
                'produto7': 70,
                'produto8': 80,
                'produto9': 85,
                'produto10': 110,
    },

    'Fevereiro': {'produto1': 120, 
                  'produto2': 130, 
                  'produto3': 110,
                  'produto4': 105,
                  'produto5': 100,
                  'produto6': 125,
                  'produto7': 115,
                  'produto8': 110,
                  'produto9': 800,
                  'produto10': 75,
    },

    'Março': {'produto1': 90, 
              'produto2': 170, 
              'produto3': 110,
              'produto4': 90,
              'produto5': 150,
              'produto6': 70,
              'produto7': 130,
              'produto8': 80,
              'produto9': 95,
              'produto10': 100,
    }
}

# print(vendas_meses, sep="\n")

"""
Traga os 4 produtos mais vendidos nos 3 meses
"""
'''
total_vendas = {

}

# total_vendas['produto1'] = 100
# total_vendas['produto1'] += 20
# print(total_vendas)

for mes, venda_mes in vendas_meses.items():
    for produto, qtd_vendas in venda_mes.items():
        if produto in total_vendas:
            total_vendas[produto] += qtd_vendas
        else:
            total_vendas[produto] = qtd_vendas



print(total_vendas)

print()
print()

produto_mais_vendido = max(total_vendas, key=total_vendas.get)
# print(produto_mais_vendido)


qtd_produto_mais_vendido = total_vendas[produto_mais_vendido]
# print(qtd_produto_mais_vendido)

print(f'O produto mias vendido foi o {produto_mais_vendido}, '
      f'vendendo {qtd_produto_mais_vendido}, no ultimo mês.')






'''

vendas_meses = {
    'Janeiro': {'produto1': 100, 'produto2': 150, 'produto3': 80, 'produto4': 110, 'produto5': 50, 'produto6': 55, 'produto7': 70, 'produto8': 80, 'produto9': 85, 'produto10': 110},
    'Fevereiro': {'produto1': 120, 'produto2': 130, 'produto3': 110, 'produto4': 105, 'produto5': 100, 'produto6': 125, 'produto7': 115, 'produto8': 110, 'produto9': 80, 'produto10': 75},
    'Março': {'produto1': 90, 'produto2': 170, 'produto3': 110, 'produto4': 90, 'produto5': 150, 'produto6': 70, 'produto7': 130, 'produto8': 80, 'produto9': 95, 'produto10': 100}
}

# Dicionário para armazenar o total de vendas de cada produto
total_vendas = {}

# Calcula o total de vendas de cada produto nos três meses
for mes, vendas_mes in vendas_meses.items():
    for produto, quantidade in vendas_mes.items():
        if produto in total_vendas:
            total_vendas[produto] += quantidade
        else:
            total_vendas[produto] = quantidade

# # Encontra o produto mais vendido
# produto_mais_vendido = max(total_vendas, key=total_vendas.get)
# quantidade_vendida = total_vendas[produto_mais_vendido]

# print("O produto mais vendido nos três meses foi:", produto_mais_vendido)
# print("Quantidade vendida:", quantidade_vendida)

            




        









































vendas_produtos = {
    "produto1": [100, 120, 90],  # Vendas nos últimos 3 meses para o produto 1
    "produto2": [150, 130, 170], # Vendas nos últimos 3 meses para o produto 2
    "produto3": [80, 90, 110],   # Vendas nos últimos 3 meses para o produto 3
    "produto4": [200, 180, 210], # Vendas nos últimos 3 meses para o produto 4
    "produto5": [90, 100, 120],  # Vendas nos últimos 3 meses para o produto 5
    "produto6": [150, 140, 160], # Vendas nos últimos 3 meses para o produto 6
    "produto7": [80, 70, 85],    # Vendas nos últimos 3 meses para o produto 7
    "produto8": [130, 110, 140], # Vendas nos últimos 3 meses para o produto 8
    "produto9": [95, 105, 115],  # Vendas nos últimos 3 meses para o produto 9
    "produto10": [180, 160, 190] # Vendas nos últimos 3 meses para o produto 10
}
'''

total_vendas = {}


for produto, qtd_produto in vendas_produtos.items():
    # print(produto, qtd_produto)
    # print(len(qtd_produto))
    total_vendas[produto] = sum(qtd_produto)

# print(total_vendas)
    
produto_mais_vendido = max(total_vendas, key=total_vendas.get)
print(produto_mais_vendido)

qtd_produto_mais_vendido = total_vendas[produto_mais_vendido]
print(qtd_produto_mais_vendido)


'''    
        
        


vendas_produtos = [
    [100, 150, 90],   # Vendas do produto 1 em janeiro, fevereiro e março, respectivamente
    [120, 130, 170],  # Vendas do produto 2 em janeiro, fevereiro e março, respectivamente
    [80, 90, 110],    # Vendas do produto 3 em janeiro, fevereiro e março, respectivamente
    [200, 180, 210],  # Vendas do produto 4 em janeiro, fevereiro e março, respectivamente
    [90, 100, 120],   # Vendas do produto 5 em janeiro, fevereiro e março, respectivamente
    [150, 140, 160],  # Vendas do produto 6 em janeiro, fevereiro e março, respectivamente
    [80, 70, 85],     # Vendas do produto 7 em janeiro, fevereiro e março, respectivamente
    [130, 110, 140],  # Vendas do produto 8 em janeiro, fevereiro e março, respectivamente
    [95, 105, 115],   # Vendas do produto 9 em janeiro, fevereiro e março, respectivamente
    [180, 160, 190]   # Vendas do produto 10 em janeiro, fevereiro e março, respectivamente
]

total_vendas = {

}


for i, produto in enumerate(vendas_produtos):
    # sum(produto)
    total_vendas['Produto'+str(i)] = sum(produto)


print(total_vendas)


produto_mais_vendido = max(total_vendas, key=total_vendas.get)
# print(produto_mais_vendido)

qtd_produto_mais_vendido = total_vendas[produto_mais_vendido]
# print(qtd_produto_mais_vendido)

print(produto_mais_vendido, qtd_produto_mais_vendido)

