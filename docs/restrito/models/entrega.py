from django.db import models

class Entrega(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    titulo = models.CharField(db_column='Titulo', max_length=200, null=True,blank=True)  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=1500, null=True,blank=True)  # Field name made lowercase.
    dtentrega = models.DateTimeField(db_column='DtEntrega', null=True,blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, null=True,blank=True)  # Field name made lowercase.
    nota = models.FloatField(db_column='Nota', null=True,blank=True)  # Field name made lowercase.
    dtavaliacao = models.DateField(db_column='DtAvaliacao', null=True,blank=True)  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=1000)  # Field name made lowercase.
    idaluno = models.ForeignKey('contas.Aluno', models.DO_NOTHING, db_column='IdAluno_id', null=True,blank=True)  # Field name made lowercase.
    idcoordenador = models.ForeignKey('contas.Coordenador', models.DO_NOTHING, db_column='IdCoordenador_id', null=True,blank=True)  # Field name made lowercase.
    idprofessores = models.ForeignKey('contas.Professores', models.DO_NOTHING, db_column='IdProfessor_id', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restrito_entrega'