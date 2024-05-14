# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
path = "3-POO/aula127.json"

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    
p1 = Pessoa('Kaue', 18)
p2 = Pessoa('Sabrina', 19)
p3 = Pessoa('Ryan', 20)

pessoas = [
    p1.__dict__, 
    p2.__dict__, 
    p3.__dict__
]

# print(pessoas)

def fazer_dump():
    with open(path, 'w', encoding="utf8") as file:
        json.dump(
            pessoas,
            file,
            indent=2
        )

if __name__ == '__main__':
    fazer_dump()
