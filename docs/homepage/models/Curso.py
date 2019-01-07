from django.db import models


class Curso(models.Model):

    #ID = models.AutoField("ID")
    Nome = models.CharField(max_length=40, null=False)

    def __str__(self):
        return self.nome
    
    class Meta:
        managed = False
        db_table = 'Curso'