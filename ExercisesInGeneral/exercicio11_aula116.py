import os
caminho = 'dados.txt'

with open(caminho, 'w') as arquivo:
    arquivo.writelines(
        'linha1\n'
        'linha2\n'
        'linha3\n'
        'linha4\n'
        'linha5\n'
        'linha6\n'
    )

with open(caminho, 'a') as arquivo:
    arquivo.writelines(
        'linha6\n'
        'linha7\n'
        'linha8\n'
        'linha9\n'
                       
    )
with open(caminho, 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha.strip())


# os.remove(caminho)
# os.rename(caminho, nome a ser renomeado)