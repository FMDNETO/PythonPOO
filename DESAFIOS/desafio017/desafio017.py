from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome="Sem nome", preco = 0):
        self.nome=nome
        self.preco=preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30,'.')}"
        etiqueta = Panel(conteudo,
                       title=f"PRODUTO",
                       style="blue",
                       width=34)
        print(etiqueta)


p1=Produto("iPhone 17 PRO MAX", 25_000.85)
p2=Produto("Notebook Gamer", 8_000)

p1.etiqueta()
p2.etiqueta()
