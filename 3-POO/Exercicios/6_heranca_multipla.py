

class Veiculos:
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo

    def ligar(self):
        print('LIGUEI')

    def desligar(self):
        print('DESLIGUEI')

class Terrestre(Veiculos):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def acelerar(self):
        print('ACELERANDO')

    def frear(self):
        print('FREANDO')

class Aquatico(Veiculos):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def navegar(self):
        print('NAVEGANDO')

    def ancorar(self):
        print('ANCORANDO')

class Anfibio(Veiculos):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def entrar_na_agua(self):
        print('ENTREI')

    def sair_da_agua(self):
        print('SAI')


terrestre1 = Terrestre('Honda', 'City')
terrestre1.ligar()
terrestre1.acelerar()
terrestre1.frear()
terrestre1.desligar()


    
    
    
 