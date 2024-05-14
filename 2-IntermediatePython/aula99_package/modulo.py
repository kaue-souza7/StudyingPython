from aula99_package.modulo_b import esta_correto

num = 100

def soma(x, y):
    
    if isinstance(x, int):
        esta_correto()
        return x + y
    else:
        print('Nao digitou numero')

print(esta_correto())