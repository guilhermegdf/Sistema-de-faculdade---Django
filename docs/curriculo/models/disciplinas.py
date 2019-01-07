from django.db import models

class Disciplina(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(db_column='Nome', max_length=20, null=True,blank=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', null=True,blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, null=True,blank=True)  # Field name made lowercase.
    planodeensino = models.CharField(db_column='PlanoDeEnsino', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    cargahoraria = models.IntegerField(db_column='CargaHoraria', null=True,blank=True)  # Field name made lowercase.
    competencias = models.CharField(db_column='Competencias', max_length=100, null=True,blank=True)  # Field name made lowercase.
    habilidades = models.CharField(db_column='Habilidades', max_length=100, null=True,blank=True)  # Field name made lowercase.
    ementa = models.CharField(db_column='Ementa', max_length=1000)  # Field name made lowercase.
    conteudoprogramatico = models.CharField(db_column='ConteudoProgramatico', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    bibliografiabasica = models.CharField(db_column='BibliografiaBasica', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    bibliografiacomplementar = models.CharField(db_column='BibliografiaComplementar', max_length=1000, null=True,blank=True)  # Field name made lowercase.
    percentualpratico = models.IntegerField(db_column='PercentualPratico', null=True,blank=True)  # Field name made lowercase.
    percentualteorico = models.IntegerField(db_column='PercentualTeorico', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curriculo_disciplina'