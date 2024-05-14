from abc import ABC, abstractmethod
    

class FiguraGeometrica(ABC):

    @abstractmethod
    def calcular_area(self): ...


    @abstractmethod
    def calcular_perimetro(self): ...

class Retangulo(FiguraGeometrica):
    def __init__(self, b, h):
        super().__init__()
        self._b = b
        self._h = h

    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, b):
        self._b = b

    @property
    def h(self):
        return self._h
    
    @h.setter
    def h(self, h):
        self._h = h

    def calcular_area(self): 
        return self.b * self.h


    def calcular_perimetro(self): 
        return 2*(self.b + self.h)
    
r1 = Retangulo(6, 3)
print(r1.calcular_area())
print(r1.calcular_perimetro())
