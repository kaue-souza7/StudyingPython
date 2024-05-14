# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    try:
        print('open path')
        file = open(path, mode, encoding="utf8")
        yield file
        print('ABERTO')
    finally: # ERRO É LANÇADO DEPOIS DE FECHAR O ARQUIVO
        file.close()
        print('fechando arquivo - FINALLY')
    


with my_open('3-POO/aula150.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n', 123)
    file.write('Linha 3\n')
    print('WITH', file)