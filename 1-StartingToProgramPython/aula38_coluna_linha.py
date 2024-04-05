"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um codigo nao tem fim
"""

# qtd_linhas = 5
# qtd_colunas = 5

# linha = 1

# while linha <= qtd_linhas:
#     coluna =  1
#     while coluna <= qtd_colunas:
#         print(f'{linha=}, {coluna=}')
#         coluna += 1

#     linha += 1





qtd_coluna = 10
qtd_linha = 3 

coluna = 1

while coluna <= qtd_coluna:
    print(f'{coluna=}')
    linha = 1

    while linha <= qtd_linha:
        print(f'{linha=}')

        linha += 1

    coluna += 1

