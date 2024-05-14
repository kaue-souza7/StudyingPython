class Automovel:
    def __init__(self, nome):
        self.nome = nome
        self.automoveis = []


    def add_automovel(self, automovel):
        self.automoveis.append(automovel)

    def list_automoveis(self):
        for automovel in self.automoveis:
            print(
                automovel.marca,
                automovel.modelo,
                automovel.cor,
                automovel.ano,
            )
            


class Motorcycle:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

motorcycle = Automovel('motorcycle')

moto1 = Motorcycle("Honda", "CBR 1000RR", "Vermelho", 2023)
moto2 = Motorcycle("Yamaha", "MT-07", "Preto", 2022)
moto3 = Motorcycle("Kawasaki", "Ninja 650", "Verde", 2021)
moto4 = Motorcycle("Suzuki", "GSX-R1000", "Azul", 2020)
moto5 = Motorcycle("Ducati", "Panigale V4", "Branco", 2024)

motorcycle.add_automovel(moto1)
motorcycle.add_automovel(moto2)
motorcycle.add_automovel(moto3)
motorcycle.add_automovel(moto4)
motorcycle.add_automovel(moto5)

print('Motorcycle: ')
motorcycle.list_automoveis()
print()
print()
print()


class Car:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

car = Automovel('car')

car1 = Car("Toyota", "Corolla", "Prata", 2020)
car2 = Car("Ford", "Fiesta", "Azul", 2018)
car3 = Car("Chevrolet", "Onix", "Branco", 2022)
car4 = Car("Honda", "Civic", "Preto", 2019)
car5 = Car("Volkswagen", "Golf", "Vermelho", 2021)

car.add_automovel(car1)
car.add_automovel(car2)
car.add_automovel(car3)
car.add_automovel(car4)
car.add_automovel(car5)

print('Car: ')
car.list_automoveis()
print()
print()
print()



class Bicyclce:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

bicycle = Automovel('bicycle')

bicy1 = Bicyclce("Caloi", "Elite Carbon", "Preto", 2022)
bicy2 = Bicyclce("Specialized", "Roubaix", "Vermelho", 2021)
bicy3 = Bicyclce("Trek", "Marlin", "Azul", 2023)
bicy4 = Bicyclce("Giant", "Trance", "Verde", 2020)
bicy5 = Bicyclce("Scott", "Spark", "Branco", 2024)

bicycle.add_automovel(bicy1)
bicycle.add_automovel(bicy2)
bicycle.add_automovel(bicy3)
bicycle.add_automovel(bicy4)
bicycle.add_automovel(bicy5)

print('Bicyclce: ')
bicycle.list_automoveis()
print()
print()
print()




