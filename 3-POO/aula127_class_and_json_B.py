import json
from aula127_class_and_json_A import Pessoa, path, fazer_dump


with open(path, 'r') as file:
    pessoas = json.load(file)

    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)


