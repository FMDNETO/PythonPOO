from rich import print
from rich.panel import Panel

class Churrasco:
    consumo_por_pessoa:float = 0.4  # converte para kg
    preco_por_kg:float = 82.40

    def __init__(self, titulo="Sem nome", quantidade = 1):
        self.titulo = titulo
        self.quantidade = quantidade

    def analisar(self):
        total_carne = self.quantidade * Churrasco.consumo_por_pessoa
        custo_total = total_carne * Churrasco.preco_por_kg
        preco_pessoa = custo_total / self.quantidade

        resultado = f"Analisando o [green]{self.titulo}[/green] com [blue]{self.quantidade}[/blue] participantes:\n"
        resultado += f"Cada participante consome aproximadamente [yellow]{Churrasco.consumo_por_pessoa * 1000:.0f}g[/yellow] de carne.\n"
        resultado += f"O custo total do churrasco será de [blue]R${custo_total:.2f}[/blue].\n"
        resultado += f"Recomendo comprar [blue]{(self.quantidade*Churrasco.consumo_por_pessoa):,.2f}Kg[/] de Carne.\n"
        resultado += f"Cada pessoa deverá pagar [blue]R${preco_pessoa:.2f}[/blue]."

        analise = Panel(resultado,title=f"{self.titulo}", width=70)
        
        print(analise)

c1 = Churrasco("Churrasco do João", 15)
c1.analisar()

#Considere:
# Consumo padrão por pessoa: 400g de carne
# Preço da carne: R$82,40 por kg

