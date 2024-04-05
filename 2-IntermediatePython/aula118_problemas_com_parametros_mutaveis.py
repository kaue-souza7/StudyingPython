# problemas com parametros mutaveis em funções python

def add_client(name, lista=None):
    if lista is None:
        lista = []
    lista.append(name)
    return lista


client1 = add_client('Luiz')
add_client('Rebecca', client1)
add_client('Fernando', client1)
client1.append('Duardo')


client2 = add_client('Kaue')
add_client('Joana', client2)
client2.append('Vini')


client3 = add_client('Claudia')
add_client('Evelyn', client3)
client3.append('Gi')



print(client1)
print(client2)
print(client3)


