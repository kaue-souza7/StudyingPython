


class FiguraGeometrica:

    def calcular_area(self):
        return 0
    
class Retangulo(FiguraGeometrica):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return area
    
class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.pi = 3.14
        self.raio = raio

    def calcular_area(self):
        area = self.pi * (self.raio**2)
        return area
    
c1 = Circulo(10)
print(c1.calcular_area())

r1 = Retangulo(15, 8)
print(r1.calcular_area())

