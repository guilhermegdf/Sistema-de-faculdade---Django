from django.db import models


class DisciplinaOfertada(models.Model):

    #ID = models.AutoField("ID")
    IdCoordenador = models.ForeignKey(Coordenador, null=False)
    IdDisciplina = models.ForeignKey(Disciplina, null=False)
    DtInicnioMatricula = models.DateField()
    DtFimMatricula = models.DateField()
    IdCurso = models.ForeignKey(Curso, null=False)
    Ano = models.IntegerField(null=False)
    Semestre = models.IntegerField(null=False)
    Turma = models.CharField(max_length=5, null=False)
    IdProfessor = models.ForeignKey(Professor)    
    Metodologia = models.CharField(max_length=1000)
    Recursos = models.CharField(max_length=1000)
    CriterioAvaliacao = models.CharField(max_length=1000)
    PlanoDeAulas = models.CharField(max_length=1000)
