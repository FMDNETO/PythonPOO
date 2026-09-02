from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def preparar(self):
        print(f"--- Iniciando o preparo ---")
        print(f"{self.ferver_agua()}")
        print(f"{self.misturar()}")
        print(f"{self.servir()}")
        print(f"--- Bebida Pronta! ---\n")


    def ferver_agua(self):
        return(f"1. Fervendo água a 100 graus Celsius")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass



class Cafe(BebidaQuente):

    def misturar(self):
        return(f"2. Passando água pressurizada pelo pó de café moído.")

    def servir(self):
        return(f"3. Servindo em xícara pequena.")

class Cha(BebidaQuente):

    def misturar(self):
        return(f"2. Mergulhando o sachê de ervas na água.")

    def servir(self):
        return(f"3. Servindo na caneca de porcelana com limão.")

class Leite(BebidaQuente):

    def misturar(self):
        return(f"2. Passando vapor pressurizado pelo bico do leite.")

    def servir(self):
        return(f"3. Servindo na caneca grande, já com café.")