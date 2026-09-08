class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError(f"Temperatura de {valor}º é inválida!")
        if valor < 16:
            self.__temperatura = 16
            self.fteperatura = f"{self.temperatura}ºC"
        elif valor > 30:
            self.__temperatura = 30
            self.fteperatura = f"{self.temperatura}ºC"
        else:
            self.__temperatura = valor
            self.fteperatura = f"{valor}ºC"

    @property
    def ftemperatura(self):
        return f"{self.temperatura}ºC"
