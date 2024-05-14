class Pessoa:
    def __init__(self, nome, idade=None):
        self.nome = nome
        self._idade = idade

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        try:
            idade = int(idade)
        except ValueError:
            print('Não digitou um número')
            return 
        
        if idade >= 18 and idade <= 100:
            self._idade = idade
        else:
            print('Idade não permitida')
            return
    
joao = Pessoa('João')
joao.idade = 101
joao.idade = '2O'

print(joao.idade)





