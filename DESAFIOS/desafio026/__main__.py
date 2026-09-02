from funcionarios import *


def main():
    pass

    f1=FuncionarioHorista("Paulo", 12,200)
    f1.calcular_salario()
    f1.analisar_salario()

    f2 = FuncionarioMensalista("Amanda", 9500)
    f2.calcular_salario()
    f2.analisar_salario()


if __name__=="__main__":
    main()