import contas, pessoas

class Banco:
    def __init__(
            self, 
            agencias: list[int] | None = None, 
            clientes: list[pessoas.Cliente] | None = None, 
            contas: list[contas.Conta] | None = None
        ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def check_agencia(self, conta: contas.Conta):
        if conta.agencia in self.agencias:
            print('_check_agencia', True)
            return True

        print('_check_agencia', False)
        return False

    def check_cliente(self, cliente: pessoas.Pessoa):
        if cliente in self.clientes:
            print('_check_cliente', True)
            return True
        
        print('_check_cliente', False)
        return False

    def check_conta(self, conta: contas.Conta):
        if conta in self.contas:
            print('_check_conta', True)
            return True
        
        print('_check_conta', False)
        return False
    
    def check_conta_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('check_conta_cliente', True)
            return True
        
        print('check_conta_cliente', False)
        return False


        
    def authenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
         
        if not self.check_agencia(conta) or not self.check_cliente(cliente) \
              or not self.check_conta(conta) \
                or not self.check_conta_cliente(cliente, conta):
            return False

        return True
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencias!r}, {self.clientes!r}, {self.contas!r}'
        return f'{class_name}({attrs})'



if __name__ == '__main__':
    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(111, 222, 0)
    c1.conta = cc1
    print(c1)
    print(c1.conta)


    c2 = pessoas.Cliente('Angelica', 20)
    cc2 = contas.ContaPoupanca(101, 202, 230)
    c2.conta = cc2
    print(c2)
    print(c2.conta)

    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cc2])
    banco.agencias.extend([111, 101])
    print()
    print()

    if banco.authenticar(c1, cc1):
        cc1.depositar(25000.00)
        print(c1, 'depositou!!!!')

    # print('CLIENTES: ', banco.clientes)
    # print('CONTAS: ', banco.contas)
    # print('AGENCIAS: ', banco.agencias)
