import enum
# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value


# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA', ])
class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2
    ACIMA = 3
    ABAIXO = 4

# print(Direcoes(1), Direcoes['ESQUERDA'])
# print(Direcoes(2), Direcoes['DIREITA'])
# print(Direcoes.ESQUERDA.value, Direcoes.ESQUERDA.name)
# print(Direcoes.DIREITA.value, Direcoes.DIREITA.name)


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    
    
    
    print(f'Movendo para {direcao.name} ({direcao.value})')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
# mover('abaixo')


# class Menu(Enum):
#     CREATE = 1
#     READ = 2
#     UPDATE = 3
#     DELETE = 4
#     SAIR = 5


# for option in Menu:
#     print(option.value, '-', option.name)
#     print()

# print('CHOOSE A OPTION')

