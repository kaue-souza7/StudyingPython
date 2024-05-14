# Métodos em instãncias de classes Python
# Classe - Molde (geralmente sem dados)
# Instãncia da class (objeto) - Tem os dados
# Uma classe pode gerar várias instãncia
# Na classe o self é a própria instãncia
class Carro:
    def __init__(self, cor, ano, nome):
        self.cor = cor
        self.ano = ano
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')



fusca = Carro('Azul', 1975, nome='Fusca')
print(fusca.cor)
print(fusca.ano)
print(fusca.nome)
fusca.acelerar()

print()
palio = Carro('Preto', 1998, nome='Palio')
print(palio.cor)
print(palio.ano)
print(palio.nome)
fusca.acelerar()






