from django.db import models
from datetime import date

# Create your models here.
class RestritoAtividade(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    titulo = models.CharField(db_column='Titulo', max_length=20, null=True,blank=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, null=True,blank=True)  # Field name made lowercase.
    conteudo = models.CharField(db_column='Conteudo', max_length=200, null=True,blank=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=200, null=True,blank=True)  # Field name made lowercase.
    idprofessores = models.ForeignKey('contas.ContasProfessores', models.DO_NOTHING, db_column='IdProfessores_id', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restrito_atividade'


class RestritoAtividadevinculada(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    rotulo = models.CharField(db_column='Rotulo', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, null=True,blank=True)  # Field name made lowercase.
    dtiniciorespostas = models.DateField(db_column='DtInicioRespostas', null=True,blank=True)  # Field name made lowercase.
    dtfimrespostas = models.DateField(db_column='DtFimRespostas', null=True,blank=True)  # Field name made lowercase.
    idatividade = models.ForeignKey('RestritoAtividade', models.DO_NOTHING, db_column='IdAtividade_id', null=True,blank=True)  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('curriculo.CurriculoDisciplinaofertada', models.DO_NOTHING, db_column='IdDisciplinaOfertada_id', null=True,blank=True)  # Field name made lowercase.
    idprofessores = models.ForeignKey('contas.ContasProfessores', models.DO_NOTHING, db_column='IdProfessores_id', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restrito_atividadevinculada'


class RestritoEntrega(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    titulo = models.CharField(db_column='Titulo', max_length=200, null=True,blank=True)  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=1500, null=True,blank=True)  # Field name made lowercase.
    dtentrega = models.DateTimeField(db_column='DtEntrega', null=True,blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, null=True,blank=True)  # Field name made lowercase.
    nota = models.FloatField(db_column='Nota', null=True,blank=True)  # Field name made lowercase.
    dtavaliacao = models.DateField(db_column='DtAvaliacao', null=True,blank=True)  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=1000)  # Field name made lowercase.
    idaluno = models.ForeignKey('contas.ContasAluno', models.DO_NOTHING, db_column='IdAluno_id', null=True,blank=True)  # Field name made lowercase.
    idcoordenador = models.ForeignKey('contas.ContasCoordenador', models.DO_NOTHING, db_column='IdCoordenador_id', null=True,blank=True)  # Field name made lowercase.
    idprofessor = models.ForeignKey('contas.ContasProfessores', models.DO_NOTHING, db_column='IdProfessor_id', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restrito_entrega'


class RestritoSolicitacaomatricula(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    status = models.CharField(db_column='Status', max_length=20, null=True,blank=True)  # Field name made lowercase.
    idaluno = models.ForeignKey('contas.ContasAluno', models.DO_NOTHING, db_column='IdAluno_id', null=True,blank=True)  # Field name made lowercase.
    idcoordenador = models.ForeignKey('contas.ContasCoordenador', models.DO_NOTHING, db_column='IdCoordenador_id', null=True,blank=True)  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('curriculo.CurriculoDisciplinaofertada', models.DO_NOTHING, db_column='IdDisciplinaOfertada_id', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restrito_solicitacaomatricula'
