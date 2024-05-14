class Retangulo():
    def __init__(self, length, height, nome):
        self.length = length
        self.height = height
        self.nome = nome

    def calculate_perimeter(self):
        print((self.height * self.length)*2)
    
    def calculate_area(self):
        print(self.height * self.length)


re1 = Retangulo(10, 10, 'Maior')
print(f'Retãngulo {re1.nome}')
print(f'Length {re1.length}')
re1.calculate_perimeter()
re1.calculate_area()

print()

re2 = Retangulo(7, 3, 'Menor')
print(f'Retãngulo {re2.nome}')
print(f'Length {re2.length}')
re2.calculate_perimeter()
re2.calculate_area()


