from EXERCICIOS.ex009.ex009 import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao("Pedro", "Matemática")
    av1.set_nota(10)
    inspect(av1, private=True)


if __name__ == '__main__':
    main()