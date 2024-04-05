# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# # print(dentro2())

def concatenar(string_inicial):
    texto_a = string_inicial
    def interna(string_a_concatenar):
        nonlocal texto_a
        texto_a += string_a_concatenar
        return texto_a
    return interna

c = concatenar('Kauê')
print(c('Souza'))