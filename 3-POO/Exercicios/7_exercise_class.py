class Empresa:
    def __init__(self, nome):
        self.nome = nome
        

class Google(Empresa):
    def __init__(self, nome):
        super().__init__(nome)
        self._lista_funcionarios = []

    def contratar(self, *args, **kwargs):
        for funcionario in args:
            self._lista_funcionarios.append(funcionario)
    
    def demitir(self, *args, **kwargs):
        nao_achados = []
        for funcionario in args:
            if funcionario in self._lista_funcionarios:
                self._lista_funcionarios.remove(funcionario)
            else:
                nao_achados.append(funcionario)
        if len(nao_achados) == 0:
            print('Todos os funcionários demitidos com sucesso.')    
        else:
            print(f'{len(nao_achados)} funcionário(s) não achado(s).')
        

    def list_funcionarios(self):
        print('Funcionários: ')
        print()
        for funcionario in self._lista_funcionarios:
            print(funcionario)
        print()

google = Google('Google')
# google.contratar('João', 'Caio', 'Caroline', 'Kaue')


class Funcionario(Google):
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self._idade  = idade
        self._salario = salario

    def calcular_salario(self):
        ...

    def imprimir_info(self):
        print('Informações sobre o funcionário: ')
        print()
        print(self.nome)
        print(self._idade)
        print(self._salario)

f1 = Funcionario('Vanessa', 26, 1500.00)
f2 = Funcionario('Paulo', 30, 2000.00)
f3 = Funcionario('Maria', 35, 1800.00)
f4 = Funcionario('Pedro', 28, 1700.00)
f5 = Funcionario('Ana', 33, 1900.00)
f6 = Funcionario('Lucas', 29, 1600.00)
f7 = Funcionario('Carla', 27, 1750.00)
f8 = Funcionario('Marcos', 31, 2100.00)
f9 = Funcionario('Julia', 34, 1950.00)
f10 = Funcionario('Rafael', 32, 1850.00)


google.list_funcionarios()
google.contratar(
            f1.nome,
            f2.nome,
            f3.nome,
            f4.nome,
            f5.nome,
            f6.nome,
            f7.nome,
            f8.nome,
            f9.nome,
            f10.nome,
        )
google.list_funcionarios()
f4.imprimir_info()