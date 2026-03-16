from rich import print
from rich import inspect


class Funcionario:
    #Atributos da classe - Todos os objetos terão
    empresa = "Curso em Vídeo"

    def __init__(self, nome = "Sem Nome", setor = "Sem Setor", cargo = "Sem Cargo"):
        #Atributos de Instancia - Cada objeto terá o seu
        self.nome=nome
        self.setor=setor
        self.cargo=cargo

    def apresentacao(self) -> str:
        return (f":handshake: Olá, eu sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}\n")


f1=Funcionario("Maria","Administração","Diretora")
print(f1.apresentacao())

f2=Funcionario("Pedro", "TI","Programador")
print(f2.apresentacao())

