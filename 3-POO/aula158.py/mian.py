# Conta (ABC)
#     ContaCorrente
#     ContaPoupanca
# Pessoa (ABC)
#     Cliente
#         Clente -> Conta
# Banco
#     Banco -> Cliente
#     Banco -> Conta
# Dicas:
# Criar classe Cliente que herda da classe Pessoa (Herança)
#     Pessoa tem nome e idade (com getters)
#     Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
# Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
#     ContaCorrente deve ter um limite extra
#     Contas têm agência, número da conta e saldo
#     Contas devem ter método para depósito
#     Conta (super classe) deve ter o método sacar abstrato (Abstração e
#     polimorfismo - as subclasses que implementam o método sacar)
# Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
# Banco será responsável autenticar o cliente e as contas da seguinte maneira:
#     Banco tem contas e clentes (Agregação)
#     * Checar se a agência é daquele banco (se agencia )
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco
# Só será possível sacar se passar na autenticação do banco (descrita acima)
# Banco autentica por um método.

#
# """



class Banco:
    def __init__(self, cliente, conta):
        self.cliente = cliente
        self.conta = conta

# conta_cliente1 = ContaCorrente('0001', '276500-8', 1000.00)
# cliente1 = Cliente('Kaue', 18, conta_cliente1)

# print(cliente1.conta.saldo)

# cliente1.conta._sacar(500)
# cliente1.conta._depositar(3000)


# bradesco = Banco()
# itau = Banco('Itaú')
# santander = Banco('Santander')