class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
    
    def adcionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(
                f'Nome: {funcionario.nome},'
                f'Idade: {funcionario.idade},' 
                f'Cargo: {funcionario.cargo},'
                f'Salário: R${funcionario.salario:.2f}'
            )




class Funcionarios:
    def __init__(self, nome, idade, cargo, salario):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario

    def aumentar_salario(self, percentual):
        percentual = percentual/100
        self.salario += (self.salario * percentual)

    
    

f1 = Funcionarios('Kaue', 18, "Cientista de Dados", 2880.0)
f2 = Funcionarios('Marcela', 18, "Web Design", 2480.0)
f3 = Funcionarios('João', 25, "Analista de Dados", 3500.0)
f4 = Funcionarios('Ana', 30, "Engenheira de Software", 4000.0)
f5 = Funcionarios('Pedro', 35, "Gerente de Projetos", 5000.0)
f6 = Funcionarios('Carla', 28, "Designer UX/UI", 3800.0)
f7 = Funcionarios('Fernando', 40, "Analista de Marketing", 4500.0)
f8 = Funcionarios('Maria', 22, "Analista de Dados", 3000.0)
f8.aumentar_salario(5)
print(f8.salario)

f9 = Funcionarios('Rafael', 27, "Cientista de Dados", 3800.0)
f10 = Funcionarios('Camila', 33, "Analista Financeiro", 4600.0)
f11 = Funcionarios('Lucas', 29, "Administrador de Redes", 4200.0)
f12 = Funcionarios('Julia', 26, "Especialista em RH", 3700.0)
f13 = Funcionarios('Gustavo', 35, "Desenvolvedor", 4900.0)
f14 = Funcionarios('Isabela', 31, "Analista de Dados", 4300.0)
f15 = Funcionarios('Renata', 37, "Gerente de Projetos", 5500.0)
f16 = Funcionarios('Diego', 24, "Designer UX/UI", 3500.0)
f17 = Funcionarios('Marcos', 29, "Cientista de Dados", 4200.0)
f18 = Funcionarios('Aline', 32, "Analista Financeiro", 4800.0)
f19 = Funcionarios('Luiz', 28, "Desenvolvedor", 4100.0)
f20 = Funcionarios('Pedro', 36, "Gerente de Projetos", 5200.0)


departamento = Departamento('Departamento de TI')
departamento.adcionar_funcionario(f1)
departamento.adcionar_funcionario(f2)
departamento.adcionar_funcionario(f3)
departamento.adcionar_funcionario(f4)
departamento.adcionar_funcionario(f5)
departamento.adcionar_funcionario(f6)
departamento.adcionar_funcionario(f7)
departamento.adcionar_funcionario(f8)
departamento.adcionar_funcionario(f9)
departamento.adcionar_funcionario(f10)
departamento.adcionar_funcionario(f11)
departamento.adcionar_funcionario(f12)
departamento.adcionar_funcionario(f13)
departamento.adcionar_funcionario(f14)
departamento.adcionar_funcionario(f15)
departamento.adcionar_funcionario(f16)
departamento.adcionar_funcionario(f17)
departamento.adcionar_funcionario(f18)
departamento.adcionar_funcionario(f19)
departamento.adcionar_funcionario(f20)

# departamento.listar_funcionarios()



