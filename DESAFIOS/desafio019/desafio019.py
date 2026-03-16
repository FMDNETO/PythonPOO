from rich import print
import time

class Livro():

    def __init__(self, titulo = "Sem título", total_paginas=1):
        self.titulo=titulo
        self.total_paginas=total_paginas
        self.pag_atual=1

        print(f":open_book:Voce acabou de abrir o livro [blue]'{self.titulo}'[/] que tem [green]{self.total_paginas}[/] páginas. Você esta agora na página {self.pag_atual}\n")

    def avancar_paginas(self, qtd=1):
        cont = 0
        for pg in range(0, qtd,1):
            if not self.fim_do_livro():
                self.pag_atual = self.pag_atual+1
                print(f"Pág{self.pag_atual} :arrow_forward: ", end='')
                time.sleep(0.2)
                cont +=1
        print(f"Você avançou {cont} páginas e esta agora na página {self.pag_atual}\n")

        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro {self.titulo}[/]")

    def fim_do_livro(self) ->bool:
        if self.pag_atual == self.total_paginas:
            return True
        else:
            return False



l1=Livro("10 coisas que eu aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)

