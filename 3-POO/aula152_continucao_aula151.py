# Funções decoradoras e decoradores com classes    
    
def add_repr(cls):
    def my_repr(self) -> str:
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}: {class_dict}'
        return class_repr
    cls.__repr__ = my_repr
    return cls

@add_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

def meu_planeta(metodo):
    def interna(self, *args, **kwargs):
        result = metodo(self, *args, **kwargs)
        if 'Terra' in result:
            result += '. Está em casa'
        return result
    return interna
 
@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def fala_nome(self):
        return f'O planeta é: {self.nome}'


# Time = add_repr(Time)
brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)

print(terra.fala_nome())