from django.db import models

# Create your models here.

class ContasAluno(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    login = models.CharField(db_column='Login', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=10, null=True,blank=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=20, null=True,blank=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=15, null=True,blank=True)  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao', null=True,blank=True)  # Field name made lowercase.
    ra = models.IntegerField(db_column='RA', null=True,blank=True)  # Field name made lowercase.
    foto = models.CharField(db_column='Foto', max_length=1000, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contas_aluno'


class ContasCoordenador(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    login = models.CharField(db_column='Login', max_length=1000,null=True,blank=True )  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=10, null=True,blank=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=20, null=True,blank=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=15, null=True,blank=True)  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contas_coordenador'


class ContasMensagem(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    assunto = models.CharField(db_column='Assunto', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    conteudo = models.CharField(db_column='Conteudo', max_length=100, null=True,blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, null=True,blank=True)  # Field name made lowercase.
    dtenvio = models.DateField(db_column='DtEnvio', null=True,blank=True)  # Field name made lowercase.
    dtresposta = models.DateField(db_column='DtResposta', null=True,blank=True)  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    idaluno = models.ForeignKey('ContasAluno', models.DO_NOTHING, db_column='IdAluno_id', null=True,blank=True)  # Field name made lowercase.
    idprofessores = models.ForeignKey('ContasProfessores', models.DO_NOTHING, db_column='IdProfessores_id', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contas_mensagem'


class ContasProfessores(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    login = models.CharField(db_column='Login', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=10, null=True,blank=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=20, null=True,blank=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=15, null=True,blank=True)  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao', null=True,blank=True)  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', max_length=20, null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contas_professores'

