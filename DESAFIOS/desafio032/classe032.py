from hashlib import sha256

class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id:int, nome:str = None, saldo:float = 0, chave:str = None):
        self._id = id #protegido (-)
        self._titular = nome #protegido (#)
        self.__saldo = saldo #privado (-)
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()
        print(f"A conta {self._id} criada com sucesso! Saldo atual de R${self.__saldo:,.2f}")

    def pede_senha(self):
        from pwinput import pwinput

        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break
        return senha

    def validar_senha(self, chave):
        chave = sha256(chave.encode()).hexdigest()
        if chave == self.__hash:
            print("Senha confere!")
            return True
        else:
            print("Senha não confere!")
            return False


    def __str__(self):
        return f"Estado atual da conta: {self.__dict__}"

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self._id} ")

    def sacar(self,valor:float,chave:str = None):
        valor = abs(valor)

        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f"Saque NEGADO de {valor:,.2f} na conta {self._id} - SALDO INSUFICIENTE!")
            else:
                self.__saldo -= valor
                print(f"Saque de R${valor:,.2f} autorizado na conta {self._id} ")
        else:
            print("Senha não confere! Saque não realizado!")

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novonome:str):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            if len(novonome) >=5:
                self._titular = novonome
        else:
            print("Senha não confere! Não é possivel validar o nove nome")
