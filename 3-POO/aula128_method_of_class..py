# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    @classmethod
    def sexo_feminino(cls, nome, idade):
        return cls(nome, idade, 'Feminino')
    
    @classmethod
    def sexo_masculino(cls, nome, idade):
        return cls(nome, idade, 'Maculino')
    
    @classmethod
    def sem_nome(cls, idade, sexo):
        return cls('Anônimo', idade, sexo)
    
    @classmethod
    def sem_nome_feminino(cls, idade):
        return cls('Anônimo', idade, 'Feminino')
    
    @classmethod
    def sem_nome_masculino(cls, idade):
        return cls('Anônimo', idade, 'Masculino')

    

p1 = Pessoa('Helena', 27, 'Feminino')
print('P1', p1.__dict__, '\n')

p2 = Pessoa.sexo_feminino('Gabriela', 18)
print('P2', p2.__dict__, '\n')

p3 = Pessoa.sexo_masculino('Victor', 17)
print('P3', p3.__dict__, '\n')

p4 = Pessoa.sem_nome(29, 'Masculino')
print('P4', p4.__dict__, '\n')

p5 = Pessoa.sem_nome_feminino(22)
print('P5', p5.__dict__, '\n')

p5 = Pessoa.sem_nome_masculino(33)
print('P5', p5.__dict__, '\n')


