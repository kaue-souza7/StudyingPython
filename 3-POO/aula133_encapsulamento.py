# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial

class Poo:
    def __init__(self):
        self.public = 'isso é PÚBLICO'
        self._protected = 'isso é PROTECTED'
        self.__private = 'isso é PRIVATE'

    def metodo_publico(self):
        print('metodo_publico')
        self._metodo_protected()
        self.__metodo_private()

    def _metodo_protected(self):
        print('_metodo_protected')

    def __metodo_private(self):
        print('__metodo_private')

f1 = Poo()

print(f1.metodo_publico())
