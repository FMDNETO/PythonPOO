from personagem import *

def Jogo():
    numjog = 0
    personagens = []

    while True:
        nome = input(f"Digite o nome do {numjog+1}º personagem: ")
        numjog += 1

        # Escolha da classe
        while True:
            try:
                classe = int(input("Escolha a classe: 1 - Guerreiro | 2 - Mago [1/2]: "))
                if classe == 1:
                    tipo = "Guerreiro"
                    break
                elif classe == 2:
                    tipo = "Mago"
                    break
                else:
                    print("Digite 1 ou 2.")
            except ValueError:
                print("Digite apenas números.")

        # Vida
        while True:
            try:
                vida = int(input(f"Digite a vida do(a) {nome} classe {tipo}: "))
                if vida > 0:
                    break
                else:
                    print("A vida precisa ser maior que 0.")
            except ValueError:
                print("Digite apenas números.")

        # Criar objeto do personagem
        if tipo == "Guerreiro":
            personagem = Guerreiro(nome, vida)
        else:
            personagem = Mago(nome, vida)

        personagens.append(personagem)

        if numjog >= 2:
            char = input("Cadastrar mais jogadores? [S/N]: ").strip().upper()
            if char == 'N':
                break

    return personagens
