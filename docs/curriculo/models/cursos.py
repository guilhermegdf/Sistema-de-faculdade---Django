from django.db  import models

# Create your models here.
class Curso(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(db_column='Nome', max_length=40, null=True,blank=True)  # Field name made lowercase.
    sigla = models.CharField(db_column='Sigla', max_length=3, null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curriculo_curso'