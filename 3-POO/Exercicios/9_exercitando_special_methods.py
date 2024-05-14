from typing import Any


class Ponto:
     
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # REPRESENTAÇÃO OFICIAL
    def __repr__(self) -> str:
        return f'Pontos({self.x!r}, {self.y!r})'

    # REPRESENTAÇÃO AMIGAVEL
    # def __str__(self):
    #     return f'Value X={self.x}, Value Y={self.y}'

    def __add__(self, other):
        new_value_x = self.x + other.x 
        new_value_y = self.y + other.y 
        new_points = new_value_x + new_value_y
        return new_points + 0.5

    
    def __eq__(self, other) -> bool:
        new_value_x = self.x + other.x 
        new_value_y = self.y + other.y 
        new_points = new_value_x < new_value_y
        return new_points


p1 = Ponto(2, 5)
p2 = Ponto(10, 2.5)

print(p1 == p2)