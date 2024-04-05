"""
Exercise 
Crie funções que duplicam, triplicam e quadriplicam
o numero recebiudo como parâmetro
"""


# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4



def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(quadruplicar(4))





