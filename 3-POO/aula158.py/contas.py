import abc

class Conta(abc.ABC):
    def __init__(self, agencia, number_conta, saldo):
        super().__init__()
        self.agencia = agencia
        self.number_conta = number_conta
        self.saldo = saldo
    
    @abc.abstractmethod
    def sacar(self, value):
        ...

    def depositar(self, value: int | float):
        ...


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.number_conta!r}, {self.saldo!r}'
        return f'{class_name}({attrs})'


class ContaCorrente(Conta):
    def __init__(self, agencia: int, number_conta: int, saldo: float):
        super().__init__(agencia, number_conta, saldo)

    
    def sacar(self, value: float) -> float:
        if (self.saldo - value) < -1000:
            print('Você não possui mais saldo para sacar!')
            return self.saldo
        
        self.saldo -= value
        print(f'Você sacou R${value}, saldo atual da sua conta é de R${self.saldo}')
        return self.saldo


    def depositar(self, value: int | float) -> float:
        self.saldo += value
        print(f'Você depositou R${value}, seu saldo atual é de R${self.saldo}')
        return self.saldo
    
    
    

class ContaPoupanca(Conta):
    def __init__(self, agencia: int, number_conta: int, saldo: float):
        super().__init__(agencia, number_conta, saldo)


    
    def depositar(self, value: int | float) -> float:
        self.saldo += value
        print(f'Você depositou R${value}, seu saldo atual é de R${self.saldo}')
        return self.saldo

    def sacar(self, value: float) -> float:
        if (self.saldo - value) < 0:
            print('Você não tem saldo para sacar!')
            return self.saldo
        
        self.saldo -= value
        print(f'Você sacou R${value}, saldo atual da sua conta é de R${self.saldo}')
        return self.saldo
    
        
if __name__ == '__main__':
    # cp1 = ContaPoupanca(111, 222, 0)
    # cp1._sacar(1)
    # cp1._depositar(1)
    # cp1._sacar(1)

    cc1 = ContaCorrente(111, 222, 0)
    cc1.sacar(500)
    cc1.depositar(500)
    cc1.sacar(501)
