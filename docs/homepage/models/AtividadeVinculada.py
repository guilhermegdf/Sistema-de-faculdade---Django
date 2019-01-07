from django.db import models
from datetime import date


class AtividadeVinculada(models.Model):

    #ID = models.AutoField("ID")
    IdAtividade = models.ForeignKey(Atividade, null=False)
    IdProfessores = models.ForeignKey(Professores, null=False)
    IdDisciplinaOfertada = models.ForeignKey(DisciplinaOfertada, null=False)
    Rotulo = models.CharField(max_length=1000, null=False)
    Status = models.CharField(max_length=10, default = 'Disponibilizada', null=False)
    DtInicioRespostas = models.DateField(null=False)
    DtFimRespostas = models.DateField( null=False)

    