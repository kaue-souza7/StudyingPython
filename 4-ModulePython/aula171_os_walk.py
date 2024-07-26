# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

path = os.path.join('C:\\Users', 'kauek', 'OneDrive', 'Área de Trabalho', 'EXEMPLO')
counter = count()

for root, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(the_counter, 'Pasta Atual: ', root)
    
    for dir_ in dirs:
        print(' ', the_counter, 'Dir: ', root)
    
    for file_ in files:
        print(file_)