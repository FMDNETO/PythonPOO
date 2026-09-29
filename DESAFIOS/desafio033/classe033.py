from abc import ABC, abstractmethod
from datetime import date


class Pessoa(ABC):
    def __init__(self, nome:str, nascimento:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError (f"Ano {ano} é inválido!")


    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionError(f'Você nao pode definir a idade por aqui! Use a data de nascimento!')


class Aluno(Pessoa):

    cursos_oficiais = ["ADM", "ADS", "ENG", "BIO", "QUIM"]

    def __init__(self, nome:str, nascimento:int, curso:str):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O curso {curso} não está na lista oficial. Adicione o curso e depois mude!")

    def add_curso(self, curso):
        curso = curso.strip().upper()

        if 3<= len(curso) <= 5:
            if curso not in Aluno.cursos_oficiais:
                Aluno.cursos_oficiais.append(curso)
            else:
                raise IndexError (f"O curso {curso} já está na lista de cursos oficiais!")