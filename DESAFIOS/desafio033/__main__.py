from DESAFIOS.desafio033.classe033 import *


def main():
    a = Aluno("Marcia", 2010, "ENG")
    a.add_curso("MODA")

    print(a.cursos_oficiais)

    a.add_curso("ADM")

    print(a)

    print (a.__dict__)
    a.add_curso("ADM")


if __name__=='__main__':
    main()