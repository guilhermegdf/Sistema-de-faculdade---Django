from django.db import models
from datetime import date


class Disciplina(models.Model):

    #ID = models.AutoField("ID")
    Nome = models.CharField(max_length=20, null=False)
    Data = models.DateField(_("Data"), auto_now_add=True, null=False)
    Status = models.CharField(max_length=10, default = 'Aberta', null=False)
    PlanoDeEnsino = models.CharField(max_length=1000, null=False)
    CargaHoraria = models.IntegerField(null=False)
    Competencias = models.CharField(max_length=100, null=False)
    Habilidades = models.CharField(max_length=100, null=False)
    Ementa = = models.CharField(max_length=1000, null=False)
    ConteudoPogramatico = models.CharField(max_length=1000, null=False)
    BibliografiaBasica = models.CharField(max_length=1000, null=False)
    BibliografiaComplementar = models.CharField(max_length=1000, null=False)
    PercentualPratico = models.IntegerField(null=False)
    PercentualTeorico = models.IntegerField(null=False)
