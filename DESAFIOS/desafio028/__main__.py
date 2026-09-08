from termostato import Termostato
from rich import print

def main():
    t = Termostato() #Cria o novo objeto de nome t da classe Termostato

    try:
        t.temperatura = 26
    except Exception as e:
        print(f"Houve um erro {e}")

    print(f"A temperatura é {t.ftemperatura}")

if __name__ == '__main__':
    main()