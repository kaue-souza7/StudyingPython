# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class


# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU O UPPER')
#         return super().upper()
    
# string = MinhaString('Julia')
# print(string.upper())



class A:
    atributo_a = 'valor A'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')
    
class B(A):
    atributo_b= 'valor B'
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor C'

    def __init__(self, *args, **kwargs):
        print('ESTOU EM C')
        super().__init__(*args, **kwargs)

    def metodo(self):
        super().metodo() # B
        super(B, self).metodo() # A
        print('C')  # CLASSE ATUAL

c = C('atributo', 'qualquer')
print(c.atributo)
print(c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
c.metodo()