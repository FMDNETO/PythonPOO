from DESAFIOS.desafio031.classe031 import Retangulo


def main():
    r = Retangulo()
    try:
        r.medidas = (3,9)
    except Exception as e:
        print(f"Ocorreu um erro do tipo {type(e).__name__}: {e}")

    print(r.medidas)

if __name__=='__main__':
    main()