"""
Higher Order Functions
Funções de primeira classes


Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros 
 tipos de dados comuns (strings, inteiros, etc...)
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executar(funcao, *args):
    return funcao(*args)


# saudacao_2 = saudacao
 
print(
    executar(saudacao, 'Bom dia', 'Kauê')
)

print(
    executar(saudacao, 'Boa noite', 'Maria')
)