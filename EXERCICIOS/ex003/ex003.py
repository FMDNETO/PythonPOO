from rich import print


class ContaBancaria:
    """
    Essa classe cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f"Deposito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque no valor de R${valor:,.2f} na conta {self.id} [red bold]NEGADO - SALDO INSUFICIENTE[/]")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")


#Criação e uso de objetos
c1 = ContaBancaria(112,"Gustavo", 3000)
#print(c1.__doc__)

c1.depositar(500)
c1.sacar(2000000)

print(c1)


