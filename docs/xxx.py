# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ContasAluno(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    login = models.CharField(db_column='Login', max_length=1000)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=10)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=1000)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=15)  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao')  # Field name made lowercase.
    ra = models.IntegerField(db_column='RA')  # Field name made lowercase.
    foto = models.CharField(db_column='Foto', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contas_aluno'


class ContasCoordenador(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    login = models.CharField(db_column='Login', max_length=1000)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=10)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=1000)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=15)  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contas_coordenador'


class ContasMensagem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    assunto = models.CharField(db_column='Assunto', max_length=1000)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=1000)  # Field name made lowercase.
    conteudo = models.CharField(db_column='Conteudo', max_length=100)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    dtenvio = models.DateField(db_column='DtEnvio')  # Field name made lowercase.
    dtresposta = models.DateField(db_column='DtResposta')  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=1000)  # Field name made lowercase.
    idaluno = models.ForeignKey(ContasAluno, models.DO_NOTHING, db_column='IdAluno_id')  # Field name made lowercase.
    idprofessores = models.ForeignKey('ContasProfessores', models.DO_NOTHING, db_column='IdProfessores_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contas_mensagem'


class ContasProfessores(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    login = models.CharField(db_column='Login', max_length=1000)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=10)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=1000)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=15)  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao')  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contas_professores'


class CurriculoCurso(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(db_column='Nome', max_length=40)  # Field name made lowercase.
    sigla = models.CharField(db_column='Sigla', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curriculo_curso'


class CurriculoDisciplina(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(db_column='Nome', max_length=20)  # Field name made lowercase.
    data = models.DateField(db_column='Data')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    planodeensino = models.CharField(db_column='PlanoDeEnsino', max_length=1000)  # Field name made lowercase.
    cargahoraria = models.IntegerField(db_column='CargaHoraria')  # Field name made lowercase.
    competencias = models.CharField(db_column='Competencias', max_length=100)  # Field name made lowercase.
    habilidades = models.CharField(db_column='Habilidades', max_length=100)  # Field name made lowercase.
    ementa = models.CharField(db_column='Ementa', max_length=1000)  # Field name made lowercase.
    conteudopogramatico = models.CharField(db_column='ConteudoPogramatico', max_length=1000)  # Field name made lowercase.
    bibliografiabasica = models.CharField(db_column='BibliografiaBasica', max_length=1000)  # Field name made lowercase.
    bibliografiacomplementar = models.CharField(db_column='BibliografiaComplementar', max_length=1000)  # Field name made lowercase.
    percentualpratico = models.IntegerField(db_column='PercentualPratico')  # Field name made lowercase.
    percentualteorico = models.IntegerField(db_column='PercentualTeorico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curriculo_disciplina'


class CurriculoDisciplinaofertada(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    dtinicniomatricula = models.DateField(db_column='DtInicnioMatricula')  # Field name made lowercase.
    dtfimmatricula = models.DateField(db_column='DtFimMatricula')  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano')  # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre')  # Field name made lowercase.
    turma = models.CharField(db_column='Turma', max_length=5)  # Field name made lowercase.
    metodologia = models.CharField(db_column='Metodologia', max_length=1000)  # Field name made lowercase.
    recursos = models.CharField(db_column='Recursos', max_length=1000)  # Field name made lowercase.
    criterioavaliacao = models.CharField(db_column='CriterioAvaliacao', max_length=1000)  # Field name made lowercase.
    planodeaulas = models.CharField(db_column='PlanoDeAulas', max_length=1000)  # Field name made lowercase.
    idcoordenador = models.ForeignKey(ContasCoordenador, models.DO_NOTHING, db_column='IdCoordenador_id')  # Field name made lowercase.
    idcurso = models.ForeignKey(CurriculoCurso, models.DO_NOTHING, db_column='IdCurso_id')  # Field name made lowercase.
    iddisciplina = models.ForeignKey(CurriculoDisciplina, models.DO_NOTHING, db_column='IdDisciplina_id')  # Field name made lowercase.
    idprofessor = models.ForeignKey(ContasProfessores, models.DO_NOTHING, db_column='IdProfessor_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curriculo_disciplinaofertada'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RestritoAtividade(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titulo = models.CharField(db_column='Titulo', max_length=20)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100)  # Field name made lowercase.
    conteudo = models.CharField(db_column='Conteudo', max_length=200)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=200)  # Field name made lowercase.
    idprofessores = models.ForeignKey(ContasProfessores, models.DO_NOTHING, db_column='IdProfessores_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restrito_atividade'


class RestritoAtividadevinculada(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    rotulo = models.CharField(db_column='Rotulo', max_length=1000)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    dtiniciorespostas = models.DateField(db_column='DtInicioRespostas')  # Field name made lowercase.
    dtfimrespostas = models.DateField(db_column='DtFimRespostas')  # Field name made lowercase.
    idatividade = models.ForeignKey(RestritoAtividade, models.DO_NOTHING, db_column='IdAtividade_id')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(CurriculoDisciplinaofertada, models.DO_NOTHING, db_column='IdDisciplinaOfertada_id')  # Field name made lowercase.
    idprofessores = models.ForeignKey(ContasProfessores, models.DO_NOTHING, db_column='IdProfessores_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restrito_atividadevinculada'


class RestritoEntrega(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titulo = models.CharField(db_column='Titulo', max_length=200)  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=1500)  # Field name made lowercase.
    dtentrega = models.DateTimeField(db_column='DtEntrega')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    nota = models.FloatField(db_column='Nota')  # Field name made lowercase.
    dtavaliacao = models.DateField(db_column='DtAvaliacao')  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=1000)  # Field name made lowercase.
    idaluno = models.ForeignKey(ContasAluno, models.DO_NOTHING, db_column='IdAluno_id')  # Field name made lowercase.
    idcoordenador = models.ForeignKey(ContasCoordenador, models.DO_NOTHING, db_column='IdCoordenador_id')  # Field name made lowercase.
    idprofessor = models.ForeignKey(ContasProfessores, models.DO_NOTHING, db_column='IdProfessor_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restrito_entrega'


class RestritoSolicitacaomatricula(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.
    idaluno = models.ForeignKey(ContasAluno, models.DO_NOTHING, db_column='IdAluno_id')  # Field name made lowercase.
    idcoordenador = models.ForeignKey(ContasCoordenador, models.DO_NOTHING, db_column='IdCoordenador_id')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(CurriculoDisciplinaofertada, models.DO_NOTHING, db_column='IdDisciplinaOfertada_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restrito_solicitacaomatricula'
