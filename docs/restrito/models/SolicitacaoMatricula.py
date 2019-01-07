from django.db import models

class Solicitacaomatricula(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    status = models.CharField(db_column='Status', max_length=20, null=True,blank=True)  # Field name made lowercase.
    dtsolicitacao = models.DateField(db_column='DtSolicitacao', null=True,blank=True)
    idaluno = models.ForeignKey('contas.Aluno', models.DO_NOTHING, db_column='IdAluno_id', null=True,blank=True)  # Field name made lowercase.
    idcoordenador = models.ForeignKey('contas.Coordenador', models.DO_NOTHING, db_column='IdCoordenador_id', null=True,blank=True)  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('curriculo.Disciplinaofertada', models.DO_NOTHING, db_column='IdDisciplinaOfertada_id', null=True,blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restrito_solicitacaomatricula'