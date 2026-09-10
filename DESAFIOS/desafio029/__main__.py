from DESAFIOS.desafio029.diario import Diario
from rich import print


def main():
    d = Diario() #Cria o objeto d da Classe Diario

    #Qualquer pessoa pode escrever no diario
    d.escrever("Alo voce")
    d.escrever("Python é legal")

    # Aqui vamos tentar mudar a senha:
    try:
        d.senha = "Master"
    except Exception as e:
        print(f"Erro: {e}")

    #Só é possivel escrever no diario fornecendo a senha (padrão: Master)
    try:
        d.ler()
    except Exception as e:
        print(f"[red]ERRO: {e}")


if __name__ == '__main__':
    main()