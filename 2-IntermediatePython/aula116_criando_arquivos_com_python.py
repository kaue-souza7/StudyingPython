# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
# caminho_arquivo = '\\Users\\kauek\\OneDrive\\Área de Trabalho\\CURSO_PYTHON\\'
caminho_arquivo = 'aula116.txt'
# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     print(type(arquivo))
#     arquivo.write('linha1\n')
#     arquivo.write('linha2\n')
#     arquivo.writelines(
#         ('linha3\n', 'linha4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end="")
#     print(arquivo.readline(), end="")
#     print(arquivo.readline(), end="")
#     print(arquivo.readline(), end="")

#     print('READLINES')
#     arquivo.seek(0, 0)

#     for row in arquivo.readlines():
#         print(row.strip())

# print("#" * 20)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())



with open(caminho_arquivo, 'r+', encoding='utf-8') as arquivo:
    print(arquivo.read())
    arquivo.write('Atenção\n')
    arquivo.write('linha1\n')
    arquivo.write('linha2\n')
    arquivo.writelines(
        ('linha3\n', 'linha4\n')
    )
    arquivo.seek(0,0)
    print(arquivo.read())
