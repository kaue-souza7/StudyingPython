# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)



# Teste = type('Teste', (object,), {})

# teste1 = Teste()

# print(teste1)
# print(type(teste1))
# print()
# print(object)
# print(type(object))
# print()
# print(type)
# print(type(type))

from typing import Any


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('NEW METACLASS')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 'ATTR'
        # print(cls.__dict__)
        return cls
    
    def __call__(self, *args, **kwds):
        print()
        print()
        print()
        instance = super().__call__(*args, **kwds)
        if 'nome' not in instance.__dict__:
            raise NotImplementedError('Crie o attr nome')
        print(instance.__dict__)
        return instance
    


class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('NEW INSTÃNCIA METACLASS')
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome


p1 = Pessoa('Kauê')
print(p1.instance)
# p1.intancia = 'INSTANCIA'
# print(p1.intancia)