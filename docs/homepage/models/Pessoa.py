from django.db import models

# Create your models here.

class Pessoa(models.Model):

    Login = models.CharField(max_length=1000, null=False)
    Senha = models.CharField(max_length=10, null=False)
    Nome = models.CharField(max_length=20, null=False)
    Email = models.EmailField(max_length=1000, null=False)
    Celular = models.CharField(max_length=15, null=False)
    DtExpiracao = models.DateField(default = '01-01-1900', null=False)

    def retornaSobrenome(self):
        return "Astolfo"
    
    def retornacargaHoraria(self):
        return "Metodo não criado(ainda)"
    
    class Meta:
        abstract = True
