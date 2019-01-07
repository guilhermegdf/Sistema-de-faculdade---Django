from django.db import models


class Entrega(models.Model):

    #ID = models.AutoField("ID")
    IdAluno = models.ForeignKey(Aluno, null=False)
    IdCoordenador = models.ForeignKey(Coordenador, null=False)
    Titulo = models.CharField(max_length=200, null=False)
    Resposta = models.CharField(max_length=1500, null=False)
    DtEntrega = models.DateTimeField(null=False)
    Status = models.CharField(max_length=10, default = 'Entregue', null=False)
    IdProfessor = models.ForeignKey(Professor)  
    Nota = FloatField()
    DtAvaliacao = models.DateField(_("Data"), auto_now_add=True, null=False)
    Obs = models.CharField(max_length=1000)
