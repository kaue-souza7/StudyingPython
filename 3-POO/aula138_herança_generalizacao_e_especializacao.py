# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('DENTRO DA CLASS PESSOA ')
        
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('DENTRO DA CLASS CLIENTE ')

        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    ...



c1 = Cliente('Kaue', 'Souza')
c1.falar_nome_classe()
a1 = Aluno('Ana', 'Maria')
a1.falar_nome_classe()

# help(Cliente)
# help(Aluno)
