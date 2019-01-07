from django.db import models

class Pessoa(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    login = models.CharField(db_column='Login', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=10, null=True,blank=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=20, null=True,blank=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=15, null=True,blank=True)  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        abstract = True