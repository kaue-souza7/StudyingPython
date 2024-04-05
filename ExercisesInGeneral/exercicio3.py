import random
produtos = []

# Gerar dados de vendas aleatórios para cada produto
for i in range(1, 1001):  # Gerar 1000 produtos
    vendas = []  # Lista para armazenar as vendas nos últimos 6 meses
    for _ in range(6):  # Gerar dados de vendas para os últimos 6 meses
        vendas.append(random.randint(50, 200))  # Vendas aleatórias entre 50 e 200 unidades
    produtos.append({'produto_id': i, 'vendas_ultimos_meses': vendas})

# Exemplo de como acessar os dados de um produto específico
# print("Exemplo de dados de um produto:")
# print("ID do produto:", produtos[0]['produto_id'])
# print("Vendas nos últimos 6 meses:", produtos[0]['vendas_ultimos_meses'])

# print(produtos)

# {'produto_id': 1, 'vendas_ultimos_meses': [186, 72, 68, 51, 168, 110]}
total_vendas = [
        
]

print(total_vendas)


copia = {

}





for dados_produto in produto:
    total_vendas.append(dados_produto.values())

for produto in total_vendas:
    copia.setdefault(produto)

for produtos in copia.items:
    print(produto)

# print(total_vendas)

# for dados_produto in produtos


