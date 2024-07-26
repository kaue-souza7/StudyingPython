# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w', encoding="utf8") as file:
    columns_name = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        file,
        fieldnames=columns_name,
        lineterminator='\r'
    )
    escritor.writeheader()

    for client in lista_clientes:
        escritor.writerow(client)





# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['Maria Sol', 'Av B, 3A'],
# ]

# with open(CAMINHO_CSV, 'w', encoding="utf8") as file:
#     columns_name = ['Nome', 'Endereços']

#     escritor = csv.writer(file, lineterminator='\r')

#     escritor.writerow(columns_name)
#     for client in lista_clientes:
#         escritor.writerow(client)

# print()