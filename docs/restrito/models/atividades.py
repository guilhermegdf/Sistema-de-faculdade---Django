from django.db import models

# Create your models here.
class Atividade(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    titulo = models.CharField(db_column='Titulo', max_length=20, null=True,blank=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, null=True,blank=True)  # Field name made lowercase.
    conteudo = models.CharField(db_column='Conteudo', max_length=200, null=True,blank=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=200, null=True,blank=True)  # Field name made lowercase.
    idprofessores = models.ForeignKey('contas.Professores', models.DO_NOTHING, db_column='IdProfessores_id', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restrito_atividade'