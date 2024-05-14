# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str


from typing import Any


class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        class_name = type(self).__name__
        return f'Pontos(x={self.x!r}, y={self.y!r}, z={self.z!r})'
    
    def __add__(self, other):
        ...
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return novo_x, novo_y

    def __gt__(self, other):
        ...
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other

if __name__ == '__main__':
    p1 = Ponto(10, 20) # 30
    p2 = Ponto(5, 8) # 13
    p3 = p1 + p2
    print(p3)
    print(f'P1 maior que P2: {p1 > p2}')
    print(f'P2 maior que P1: {p2 > p1}')