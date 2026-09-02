from abc import ABC, abstractmethod

from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0
        self.sal_min = 1612
        self.inss = 7.5


    def analisar_salario(self):
            analise=self.salario/self.sal_min
            conteudo = (f"O salario de [blue]{self.nome}[/]({self.__class__.__name__}) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{analise:.2f} salários mínimos![/]")
            etiqueta = Panel(conteudo,
                             title=f"[red]ANALISE DE SALARIO[/]",
                             style="",
                             width=50)
            print(etiqueta)


    @abstractmethod
    def calcular_salario(self):
        pass


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, qtd_horas=220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas

    def calcular_salario(self):
        self.salario_bruto = self.valor_hora * self.qtd_horas
        self.inss = (self.salario_bruto * self.inss) / 100
        self.salario = self.salario_bruto - self.inss
        return self.salario

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calcular_salario(self):
        self.inss = (self.salario_bruto * self.inss) / 100
        self.salario = self.salario_bruto - self.inss
        return self.salario


