from rich import print
from poligono import *


def main():
    c1 = Circulo(20)

    print(f"Perímetro do {c1.nomepolig} = {c1.perimetro():.1f}")
    print(f"Área do {c1.nomepolig} = {c1.area():.1f}")

    q1 = Quadrado(20)
    print(f"Perímetro do {q1.nomepolig} = {q1.perimetro():.1f}")
    print(f"Área do {q1.nomepolig} = {q1.area():.1f}")


if __name__ == "__main__":
    main()