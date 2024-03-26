def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y

print(
    executa(
        lambda x, y: x + y,
        120, 2
    )
)


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador 
    return multiplica


duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: m * n,
    2
)

print(duplica(90))

print(cria_multiplicador(2)(10))