#Declaração das classes
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto que tem nome e idade.
    Para criar uma nova classe use:
    Variável = Gafanhoto(nome,idade)
    """
    def __init__(self, nome = "vazio", idade=0): #Método Construtor
        #Atributos de Instância
        self.nome = nome
        self.idade = idade

    #Métodos de Instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self):
        return (f"\n{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade")

    def __getstate__(self):
        return (f"\nEstado do Objeto:\nNome: {self.nome}\nIdade: {self.idade}")


#Declaração de objetos

g1 = Gafanhoto("Maria",17)
print(g1)

print(g1.__getstate__())

g2 = Gafanhoto("João",18)
print(g2)

g3 = Gafanhoto()
print(g3)


#Manipulação dos objetos
g1.aniversario()
print(f"Após aniversário, {g1.nome} tem {g1.idade} anos de idade")

g2.aniversario()
print(f"Após aniversário, {g2.nome} tem {g2.idade} anos de idade")

