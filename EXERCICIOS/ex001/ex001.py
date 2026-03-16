#Declaração das classes
class Gafanhoto:
    def __init__(self): #Método Construtor
        #Atributos de Instância
        self.nome = ""
        self.idade = 0

    #Métodos de Instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return (f"\n{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade")


#Declaração de objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 17

g2 = Gafanhoto()
g2.nome = "João"
g2.idade = 18


#Manipulação dos objetos
print(g1.mensagem())
g1.aniversario()
print(f"Após aniversário, {g1.nome} tem {g1.idade} anos de idade")

print(g2.mensagem())
g2.aniversario()
print(f"Após aniversário, {g2.nome} tem {g2.idade} anos de idade")

