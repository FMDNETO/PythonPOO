from rich import print

class Caneta:

    def __init__(self, cor):
        cor=cor.lower().strip()
        self.cor = cor
        if cor == "azul":
            self.cor = "blue"
        if cor == "verde":
            self.cor = "green"
        if cor == "vermelho":
            self.cor = "red"

        self.tampada = 1

    def destampar(self):
        self.tampada = 0

    def escrever(self, texto):
        if not self.tampada:
            print(f"[{self.cor}]{texto}[/] ", end='')

        else:
            print(f":prohibited: A[{self.cor}] caneta[/] esta tampada!")

    def quebrar_linha(self, linhas):
        print("\n"*linhas, end='')


c1=Caneta("azul")
c2=Caneta("Vermelho")
c3=Caneta("verde")

#c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(2)

c2.escrever("Olá, Gafanhoto!")


c3.escrever("Vamos exercitar!")
