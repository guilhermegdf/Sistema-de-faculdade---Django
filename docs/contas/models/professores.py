from django.db import models
from .pessoas import Pessoa

class Professores(Pessoa):

    apelido = models.CharField(db_column='Apelido', max_length=20, null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contas_professores'