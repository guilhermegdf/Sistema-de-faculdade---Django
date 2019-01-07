from django.db import models
from .Pessoa import Pessoa

class Professores(Pessoa):
    #ID = models.AutoField("ID")
    Apelido = models.CharField("Apelido", max_length=20, null=False)


    def adicionaDisciplina(self, disciplina):
        if disciplina.getProfessor().getRa() == self.__ra:
            self.__disciplinas.append(disciplina)
        else:
            return 'Professor não associado a disciplina'



