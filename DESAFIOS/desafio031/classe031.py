class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if not isinstance(altura, float) and not isinstance(altura, int):
            raise TypeError("O valor da altura deve ser um número!")
        if altura <= 0:
            raise ValueError("A altura deve ser maior que zero")
        else:
            self._altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if not isinstance(base, float) and not isinstance(base, int):
            raise TypeError("O valor da base deve ser um número!")
        if base <= 0:
            raise ValueError("A base deve ser maior que zero")
        else:
            self._base = base

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError(f"Você não tem permissão para alterar a área do retângulo!")

    @property
    def medidas(self):
        return f'Altura: {self.altura}\nBase: {self.base}\nÁrea: {self.area}'

    @medidas.setter
    def medidas(self,valores: tuple):
        if not isinstance(valores, tuple):
            raise TypeError("As medidas devem ser informadas em uma tupla!")
        if len(valores) != 2:
            raise SyntaxError("Informe uma tupla com apenas dois valores numéricos!")
        if isinstance(valores[0],float) or isinstance(valores[0], int):
            self.base = valores[0]
        else:
            raise TypeError ("A base deve ser um número!")
        if isinstance(valores[1],float) or isinstance(valores[1], int):
            self.altura = valores[1]
        else:
            raise TypeError("A altura deve ser um número!")
