
from personagem import *
from engine import *

def main():


        p1=Guerreiro("Kratos",2000)
        p2=Mago("Merlin",3000)
        print(f"{p1.nome} VS {p2.nome}")

        p1.atacar(p2,1000)

        p1.curar()
        p2.curar()

        p1.verificar_vida()
        p2.verificar_vida()




if __name__=="__main__":
    main()