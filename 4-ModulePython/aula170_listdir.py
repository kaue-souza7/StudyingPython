import os 
# os.listdir para navegar em caminhos

# path = r'C:\\Users\\kauek\\OneDrive\\Área de Trabalho\\EXEMPLO'
path = os.path.join('C:\\Users', 'kauek', 'OneDrive', 'Área de Trabalho', 'EXEMPLO')

# print(path)

for pasta in os.listdir(path):
    caminho_completo_pasta = os.path.join(path, pasta)
    print()
    print()
    print(pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue

    for item in os.listdir(caminho_completo_pasta):
        print('     ',item)
    print()
    print()
    print()
