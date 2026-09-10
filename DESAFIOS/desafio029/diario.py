from rich import print

class Diario:
    def __init__(self, senhamestra = 'Master'):
        self.__segredos = []
        self.__senha = senhamestra.strip()

    def escrever(self, mensagem):
        if isinstance(mensagem, str) and len(mensagem) > 0:
            self.__segredos.append(mensagem.strip())

    def ler(self,senha = None):
        if senha == self.__senha:
            print(f"[green][bold]Diário desbloqueado![/]")
            for segredo in self.__segredos:
                print(f"- {segredo}")
        else:
            raise PermissionError(f"SENHA INVÁLIDA - VOCE NÃO PODE LER O DIÁRIO")

    @property
    def senha(self):
        raise PermissionError(f"Ninguém tem permissão de ver a senha!")

    @senha.setter
    def senha(self, novasenha):
        if novasenha == self.__senha:
            raise SyntaxError(f"As senhas são iguais!")
            exit()
        else:
            self.__senha = novasenha.strip()