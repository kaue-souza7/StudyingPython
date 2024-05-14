# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        self.carros = []

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

    def add_carro(self, *carros):
        for carro in carros:
            self.carros.append(carro)

    def list_carros(self):
        for carro in self.carros:
            print(
                carro.nome,
                carro.motor,
                carro.fabricante
            )

class Motor:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

honda = Fabricante('Honda')
volkswagem = Fabricante('Volkswagem')
nissam = Fabricante('Nissam')

motor1_6 = Motor('1.6')



carro = Carro('Carros')

gol = Carro('Gol')
gol.fabricante = volkswagem
gol.motor = motor1_6

print('Carros: ')
print()
print(gol.nome, gol.motor.nome, gol.fabricante.nome)

city = Carro('City')
city.fabricante = honda
city.motor = motor1_6
print(city.nome, city.motor.nome, city.fabricante.nome)

kicks = Carro('Kicks')
kicks.fabricante = nissam
kicks.motor = motor1_6
print(kicks.nome, kicks.motor.nome, kicks.fabricante.nome)


carro.add_carro(gol, city, kicks)







