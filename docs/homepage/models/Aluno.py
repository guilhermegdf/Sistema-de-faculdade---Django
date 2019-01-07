from django.db import models
from .Pessoa import Pessoa

class Aluno(Pessoa):

    #ID = models.AutoField("ID")
    RA = models.IntegerField("RA", null=False)
    Foto = models.CharField("Foto", max_length=1000)

    def adicionaDisciplina(self, disciplina):
        if disciplina.getAluno().getRa() == self.__ra:
            self.__disciplinas.append(disciplina)
        else:
            return 'Aluno não associado a disciplina'

    def aumentaDesconto(self, desconto):
        self.__desconto=self.__desconto+desconto
    
    def diminuiDesconto(self, desconto):
        self.__desconto=self.__desconto-desconto
    
    def retornaValorMensalidade(self, desconto):
        valor_final=0
        for d in self.__disciplinas:
            valor_final += d.getMensalidade()*desconto
        return valor_final
        
