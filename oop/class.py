class Carro:

    quantidadeRodas = 4
    cor = "azul"

    def __init__(self, quantidadeRodas, cor):
        self.quantidadeRodas = quantidadeRodas
        self.cor = cor

    def setQuantidadeRodas(self, quantidadeRodas):
        self.quantidadeRodas = quantidadeRodas


meuCarro1 = Carro(10, "azul")
meuCarro1.quantidadeRodas
