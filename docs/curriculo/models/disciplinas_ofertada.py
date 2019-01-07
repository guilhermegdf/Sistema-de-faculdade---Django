from django.db import models

class DisciplinaOfertada(models.Model):
   # id = models.IntegerField(primary_key=True)  # AutoField?
    dtinicniomatricula = models.DateField(db_column='DtInicnioMatricula')  # Field name made lowercase.
    dtfimmatricula = models.DateField(db_column='DtFimMatricula')  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano')  # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre')  # Field name made lowercase.
    turma = models.CharField(db_column='Turma', max_length=5)  # Field name made lowercase.
    metodologia = models.CharField(db_column='Metodologia', max_length=1000)  # Field name made lowercase.
    recursos = models.CharField(db_column='Recursos', max_length=1000)  # Field name made lowercase.
    criterioavaliacao = models.CharField(db_column='CriterioAvaliacao', max_length=1000)  # Field name made lowercase.
    planodeaulas = models.CharField(db_column='PlanoDeAulas', max_length=1000)  # Field name made lowercase.
    idcoordenador = models.ForeignKey('contas.Coordenador', models.DO_NOTHING, db_column='IdCoordenador_id')  # Field name made lowercase.
    idcurso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='IdCurso_id')  # Field name made lowercase.
    iddisciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='IdDisciplina_id')  # Field name made lowercase.
    idprofessor = models.ForeignKey('contas.Professores', models.DO_NOTHING, db_column='IdProfessor_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curriculo_disciplinaofertada'