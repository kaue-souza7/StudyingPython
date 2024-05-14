import contas


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.nome!r}, {self.idade!r}'
        return f'{class_name}({attrs})'

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


    @property
    def agencia(self):
        return self.agencia
    
    @property
    def number_conta(self):
        return self.number_conta
    
    @property
    def saldo(self):
        return self.saldo
    
if __name__ == '__main__':
    c1 = Cliente('Luiz', 30)
    c1.conta = contas.ContaCorrente(111, 222, 0)
    print(c1)
    print(c1.conta)
    print()
    print()
    c2 = Cliente('Maria', 33)
    c2.conta = contas.ContaCorrente(101, 202, 110)
    print(c2)
    print(c2.conta)
    print()
    print()
    c2 = Cliente('Maria', 33)
    c2.conta = contas.ContaPoupanca(101, 202, 110)
    print(c2)
    print(c2.conta)
