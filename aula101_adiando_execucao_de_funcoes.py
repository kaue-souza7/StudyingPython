# Exercicio - Adiando execuções de funções

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y


def executa(funcao, *args):
    return funcao(*args)


soma_com_dez = executa(soma, 10, 10)

print(soma_com_dez)

