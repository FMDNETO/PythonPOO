from classe030 import *

def main():
    c = Credencial()
    c.senha = str(input("Digite sua senha: "))

    print(c.senha)

    c.validar('123456')

if __name__ == '__main__':
    main()
