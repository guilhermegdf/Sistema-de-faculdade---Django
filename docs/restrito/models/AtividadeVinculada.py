from django.db import models

class Atividadevinculada(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    rotulo = models.CharField(db_column='Rotulo', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, null=True,blank=True)  # Field name made lowercase.
    dtiniciorespostas = models.DateField(db_column='DtInicioRespostas', null=True,blank=True)  # Field name made lowercase.
    dtfimrespostas = models.DateField(db_column='DtFimRespostas', null=True,blank=True)  # Field name made lowercase.
    idatividade = models.ForeignKey('Atividade', models.DO_NOTHING, db_column='IdAtividade_id', null=True,blank=True)  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('curriculo.Disciplinaofertada', models.DO_NOTHING, db_column='IdDisciplinaOfertada_id', null=True,blank=True)  # Field name made lowercase.
    idprofessores = models.ForeignKey('contas.Professores', models.DO_NOTHING, db_column='IdProfessores_id', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restrito_atividadevinculada'