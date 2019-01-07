from django.db import models
from .pessoas import Pessoa

# Create your models here.

class Aluno(Pessoa):

    ra = models.IntegerField(db_column='RA', null=True,blank=True)  # Field name made lowercase.
    foto = models.CharField(db_column='Foto', max_length=1000, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contas_aluno'