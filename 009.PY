from curses import REPORT_MOUSE_POSITION


class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.nivelCombustivel = 0

    def andar(self, distancia):
        temp = distancia/self.consumo
        self.nivelCombustivel += temp

    def adicionarGasolina(self, qtd):
        self.nivelCombustivel += qtd

meuFusca  = Carro(8)
meuFusca.adicionarGasolina(50)
meuFusca.andar(300)