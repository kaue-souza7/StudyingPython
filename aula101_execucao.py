# Exercício - Adiando execução de funções
def soma(x, y):
    return x * y

def executa(funcao, y):
    def interna(x):
        return funcao(x, y)
    return interna

multiplica_por_dois = executa(soma, 2)

print(multiplica_por_dois(10))

