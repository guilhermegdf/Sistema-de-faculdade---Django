# Generated by Django 2.0 on 2018-05-01 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curriculo', '0001_initial'),
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(db_column='Titulo', max_length=20)),
                ('descricao', models.CharField(db_column='Descricao', max_length=100)),
                ('conteudo', models.CharField(db_column='Conteudo', max_length=200)),
                ('tipo', models.CharField(db_column='Tipo', max_length=200)),
                ('idprofessores', models.ForeignKey(db_column='IdProfessores_id', on_delete=django.db.models.deletion.DO_NOTHING, to='contas.Professores')),
            ],
        ),
        migrations.CreateModel(
            name='Atividadevinculada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rotulo', models.CharField(db_column='Rotulo', max_length=1000)),
                ('status', models.CharField(db_column='Status', max_length=10)),
                ('dtiniciorespostas', models.DateField(db_column='DtInicioRespostas')),
                ('dtfimrespostas', models.DateField(db_column='DtFimRespostas')),
                ('idatividade', models.ForeignKey(db_column='IdAtividade_id', on_delete=django.db.models.deletion.DO_NOTHING, to='restrito.Atividade')),
                ('iddisciplinaofertada', models.ForeignKey(db_column='IdDisciplinaOfertada_id', on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.Disciplinaofertada')),
                ('idprofessores', models.ForeignKey(db_column='IdProfessores_id', on_delete=django.db.models.deletion.DO_NOTHING, to='contas.Professores')),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(db_column='Titulo', max_length=200)),
                ('resposta', models.CharField(db_column='Resposta', max_length=1500)),
                ('dtentrega', models.DateTimeField(db_column='DtEntrega')),
                ('status', models.CharField(db_column='Status', max_length=10)),
                ('nota', models.FloatField(db_column='Nota')),
                ('dtavaliacao', models.DateField(db_column='DtAvaliacao')),
                ('obs', models.CharField(db_column='Obs', max_length=1000)),
                ('idaluno', models.ForeignKey(db_column='IdAluno_id', on_delete=django.db.models.deletion.DO_NOTHING, to='contas.Aluno')),
                ('idcoordenador', models.ForeignKey(db_column='IdCoordenador_id', on_delete=django.db.models.deletion.DO_NOTHING, to='contas.Coordenador')),
                ('idprofessor', models.ForeignKey(db_column='IdProfessor_id', on_delete=django.db.models.deletion.DO_NOTHING, to='contas.Professores')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitacaomatricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(db_column='Status', max_length=20)),
                ('idaluno', models.ForeignKey(db_column='IdAluno_id', on_delete=django.db.models.deletion.DO_NOTHING, to='contas.Aluno')),
                ('idcoordenador', models.ForeignKey(db_column='IdCoordenador_id', on_delete=django.db.models.deletion.DO_NOTHING, to='contas.Coordenador')),
                ('iddisciplinaofertada', models.ForeignKey(db_column='IdDisciplinaOfertada_id', on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.Disciplinaofertada')),
            ],
        ),
    ]
