from django.db import models
from datetime import date


class Mensagem(models.Model):

    #ID = models.AutoField("ID")
    IdAluno = models.ForeignKey(Aluno, null=False)
    IdProfessores = models.ForeignKey(Professores, null=False)
    Assunto = models.CharField(max_length=1000, null=False)
    Referência = models.CharField(max_length=1000, null=False)
    Conteúdo = models.CharField(max_length=100, null=False)
    Status = models.CharField(max_length=10, default = 'Enviado', null=False)
    DtEnvio = models.DateField(_("Data"), auto_now_add=True, null=False)
    DtResposta = models.DateField()
    Resposta = models.CharField(max_length=1000)
    