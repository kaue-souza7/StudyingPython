# Dictionary Comprehension e set Comprehension

produto = {
    'nome': 'Caneta Azul', 
    'preco': 2.5, 
    'categoria': 'Escritorio',

}

# dc = {
#     chave: valor.upper()
#     if isinstance(valor, str) else valor
#     for chave, valor in produto.items()
#     if chave == 'categoria'
# }

lista = [
    ('a', 'valor a'), 
    ('b', 'valor b'), 
    ('c', 'valor c'), 
]

dc = {
    chave: valor
    for chave, valor in lista
        
}

s1 = {    
    i ** 2
    for i in range(10)

}
# print(s1)



# print(dc)

teste = [
    [letra for letra in 'Rebecca']
    for n in range(3)
]

print(teste, sep="\n")