from django.db import models


class Curso(models.Model):

    #ID = models.AutoField("ID")
    Nome = models.CharField(max_length=40, column_name='Nome')
    
    class Meta:
        managed = False
        db_table = 'Curso'