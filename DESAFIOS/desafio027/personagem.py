from abc import ABC, abstractmethod
import random
from rich import print
from rich.panel import Panel



class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome=nome
        self.vida=vida
        self.golpes={"Guerreiro":["Machado","Chute Giratório", "Racha Cuca", "Soco", "Ferramenta Roda Gira"],"Mago":["Bola de Fogo","Magia Negra", "Cajado da Justiça","Golpe de Judô", "Ataque das Corujas"]}

    def receber_dano(self, alvo, dano):
        self.vida -= dano
        print(f"{alvo.nome} recebeu {dano} de dano! ", end="")
        if self.vida <= 0:
            print(f"\n{self.nome} morreu! [red]GAME OVER![/]")
            exit(0)
        else:
            print(f"Esta com {self.vida} de vida!")

    def atacar(self, alvo, forca):

        dano=random.randint(1,forca)
        golpe = self.golpes[(self.__class__.__name__)][random.randint(0, len(self.golpes[self.__class__.__name__]) - 1)]
        print(f"{self.nome} - VIDA:({self.vida}) atacou {alvo.nome} - VIDA:({alvo.vida}) com {golpe} de força {forca} e o atingiu com {dano} dano!")

        alvo.receber_dano(alvo, dano)

    def verificar_vida(self):
        print(f"{self.nome} está com {self.vida} de vida!")


    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)



    def curar(self):
        pocao = random.randint(1,100)
        print(f"{self.nome} enrolou uma atadura nos ferimentos e recuperou {pocao} pontos de vida!")
        self.vida += pocao


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)


    def curar(self):
        pocao = random.randint(1,100)
        print(f"{self.nome} usou uma magia de cura nos ferimentos e recuperou {pocao} pontos de vida!")
        self.vida += pocao