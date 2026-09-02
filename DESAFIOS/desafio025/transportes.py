from abc import ABC,abstractmethod


class Transporte(ABC):

    def __init__(self, distancia):
        self.distancia=distancia
        self.frete=0

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):

        super().__init__(distancia)  # fator fixo da moto
        self.distancia=distancia

    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return f"R${self.frete:.2f}"


class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia < 50:
            self.frete = 0
            return f"A distância mínima para fretes com caminhão são 50 km"
        else:
            self.frete = self.distancia * Caminhao.fator
            return f"R${self.frete:.2f}"

class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia > 10:
            self.frete = 0
            return f"A distância máxima para fretes com Drones são 10 km"
        else:
            self.frete = self.distancia * Drone.fator
            return f"R${self.frete:.2f}"
