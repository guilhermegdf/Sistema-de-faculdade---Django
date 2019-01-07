from django.db import models
from datetime import date

# Create your models here.
class CurriculoCurso(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(db_column='Nome', max_length=40, null=True,blank=True)  # Field name made lowercase.
    sigla = models.CharField(db_column='Sigla', max_length=3, null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curriculo_curso'


class CurriculoDisciplina(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(db_column='Nome', max_length=20, null=True,blank=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', null=True,blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, null=True,blank=True)  # Field name made lowercase.
    planodeensino = models.CharField(db_column='PlanoDeEnsino', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    cargahoraria = models.IntegerField(db_column='CargaHoraria', null=True,blank=True)  # Field name made lowercase.
    competencias = models.CharField(db_column='Competencias', max_length=100, null=True,blank=True)  # Field name made lowercase.
    habilidades = models.CharField(db_column='Habilidades', max_length=100, null=True,blank=True)  # Field name made lowercase.
    ementa = models.CharField(db_column='Ementa', max_length=1000)  # Field name made lowercase.
    conteudopogramatico = models.CharField(db_column='ConteudoPogramatico', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    bibliografiabasica = models.CharField(db_column='BibliografiaBasica', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    bibliografiacomplementar = models.CharField(db_column='BibliografiaComplementar', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    percentualpratico = models.IntegerField(db_column='PercentualPratico', null=True,blank=True)  # Field name made lowercase.
    percentualteorico = models.IntegerField(db_column='PercentualTeorico', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curriculo_disciplina'


class CurriculoDisciplinaofertada(models.Model):
   # id = models.IntegerField(primary_key=True)  # AutoField?
    dtinicniomatricula = models.DateField(db_column='DtInicnioMatricula')  # Field name made lowercase.
    dtfimmatricula = models.DateField(db_column='DtFimMatricula')  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano')  # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre')  # Field name made lowercase.
    turma = models.CharField(db_column='Turma', max_length=5)  # Field name made lowercase.
    metodologia = models.CharField(db_column='Metodologia', max_length=1000)  # Field name made lowercase.
    recursos = models.CharField(db_column='Recursos', max_length=1000)  # Field name made lowercase.
    criterioavaliacao = models.CharField(db_column='CriterioAvaliacao', max_length=1000)  # Field name made lowercase.
    planodeaulas = models.CharField(db_column='PlanoDeAulas', max_length=1000)  # Field name made lowercase.
    idcoordenador = models.ForeignKey('contas.ContasCoordenador', models.DO_NOTHING, db_column='IdCoordenador_id')  # Field name made lowercase.
    idcurso = models.ForeignKey('CurriculoCurso', models.DO_NOTHING, db_column='IdCurso_id')  # Field name made lowercase.
    iddisciplina = models.ForeignKey('CurriculoDisciplina', models.DO_NOTHING, db_column='IdDisciplina_id')  # Field name made lowercase.
    idprofessor = models.ForeignKey('contas.ContasProfessores', models.DO_NOTHING, db_column='IdProfessor_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curriculo_disciplinaofertada'