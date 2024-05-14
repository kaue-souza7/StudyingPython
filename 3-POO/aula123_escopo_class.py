class Animal():
    def __init__(self, nome):
        self.nome = nome 

    def comendo(self, alimento):
        return (f'{self.nome} está comendo {alimento}')

    def executar(self, *args):
        return self.comendo(*args)



leao = Animal('Leão Juba')
print(leao.executar('Maça'))
