from django.db  import models

class Mensagem(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    assunto = models.CharField(db_column='Assunto', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    conteudo = models.CharField(db_column='Conteudo', max_length=100, null=True,blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, null=True,blank=True)  # Field name made lowercase.
    dtenvio = models.DateField(db_column='DtEnvio', null=True,blank=True)  # Field name made lowercase.
    dtresposta = models.DateField(db_column='DtResposta', null=True,blank=True)  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    idaluno = models.ForeignKey('Aluno', models.DO_NOTHING, db_column='IdAluno_id', null=True,blank=True)  # Field name made lowercase.
    idprofessores = models.ForeignKey('Professores', models.DO_NOTHING, db_column='IdProfessores_id', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contas_mensagem'