from rich import print, inspect
from classesex005 import Aluno, Professor, Funcionario


a1 = Aluno("José", 17, "Informática", "T01")
a1.fazer_aniversario()
inspect(a1)

p1 = Professor("Samuel", 37, "Biologia", "Mestre")
inspect(p1)

f1 = Funcionario("Claudia",27, "Secretária", "Secretaria de Ensino")
inspect(f1)