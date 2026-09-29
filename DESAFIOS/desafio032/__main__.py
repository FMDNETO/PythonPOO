from DESAFIOS.desafio032.classe032 import *

def main():
    cc = ContaBancaria(111, "Josenildo", 10_000)

    print("Vou tentar sacar")
    cc.sacar(500)

    cc.nome = "Maricota"

if __name__ == '__main__':
    main()