from django.db import models


class SolicitacaoMatricula(models.Model):

    #ID = models.AutoField("ID")
    IdAluno = models.ForeignKey(Aluno, null=False)
    IdDisciplinaOfertada = models.ForeignKey(DisciplinaOfertada, null=False)
    IdCoordenador = models.ForeignKey(Coordenador)
    Status = models.CharField(max_length=20, default = 'Solicitada', null=False)