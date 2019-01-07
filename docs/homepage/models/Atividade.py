from django.db import models


class Atividade(models.Model):

    #ID = models.AutoField("ID")
    Titulo = models.CharField(max_length=20, null=False)
    Descricao= models.CharField(max_length=100, null=False)
    Conteudo = models.CharField(max_length=200, null=False)
    Tipo = models.CharField(max_length=200)
    IdProfessores = models.ForeignKey(Professores)