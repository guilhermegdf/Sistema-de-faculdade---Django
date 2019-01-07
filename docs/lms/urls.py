"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage.views import *
from curriculo.views import *
from restrito.views import *
from contas.views import *

urlpatterns = [
    path('', index),
    #path('cursos/<str:sigla>/', curso),
    # path('<str:sigla>/<str:disc>', disciplina), 
    #path('<str:sigla>/disciplinas/', listadisciplina),
    #path('nova_disciplina/', nova_disciplina),
    #path('novo_curso/', novo_curso),
########################### CONTAS ##################################
    path('lista_curriculo/', lista_curriculo),
    path('cursos/', cursos_lista),
    path("cursos/incluir/", incluirCurso),
    path("cursos/remover/<int:id>", removerCurso),
    path("cursos/alterar/<int:id>", alterarCurso),
    path('disciplina/', disciplina),
    path('disciplina/incluir/', incluirDisciplina),
    path("disciplina/alterar/<int:id>", alterarDisciplina),
    path("disciplina/remover/<int:id>", removerDisciplina),
    path("disciplina_ofertada/", disciplinaOfertada_lista),
    path("disciplina_ofertada/incluir/", incluirDisciplinaOfertada),
    path("disciplina_ofertada/alterar/<int:id>/", alterarDisciplinaOfertada),
    path("disciplina_ofertada/remover/<int:id>/", removerDisciplinaOfertada),
########################### CURRICULO ###################################
    path('lista_contas/', lista_contas),
    path('contas/Aluno/', Aluno),
    path('contas/Aluno/incluir/', incluirAluno),
    path("Aluno/alterar/<int:id>", alterarAluno),
    path("Aluno/remover/<int:id>", removerAluno),
    path('contas/Professor/', Professor),
    path('contas/Professor/incluir/', incluirProfessor),
    path("Professor/alterar/<int:id>", alterarProfessor),
    path("Professor/remover/<int:id>", removerProfessor),
    path('contas/Coordenador/', Coordenador),
    path('contas/Coordenador/incluir/', incluirCoordenador),
    path("Coordenador/alterar/<int:id>", alterarCoordenador),
    path("Coordenador/remover/<int:id>", removerCoordenador),
    path('contas/Mensagem/', Mensagem),
    path('contas/Mensagem/incluir/', incluirMensagem),
    path("Mensagem/alterar/<int:id>", alterarMensagem),
    path("Mensagem/remover/<int:id>", removerMensagem),
########################## RESTRITO #######################################
    path('lista_restrito/', lista_restrito),
    path('atividade/', Atividade),
    path("atividade/incluir/", incluirAtividade),
    path("atividade/alterar/<int:id>", alterarAtividade),
    path("atividade/remover/<int:id>", removerAtividade),
    path('atividade_vinculada/', atividade_vinculada),
    path('atividade_vinculada/incluir/', incluiratividade_vinculada),
    path('atividade_vinculada/alterar/<int:id>', alteraratividade_vinculada),
    path('atividade_vinculada/remover/<int:id>', removeratividade_vinculada),
    path('entrega/', entrega_lista),
    path('entrega/incluir/', incluir_entrega),
    path('entrega/alterar/<int:id>', alterar_entrega),
    path('entrega/remover/<int:id>', remover_entrega),
    path('solicitacao_matricula/', solicitacao_matricula_lista),
    path('solicitacao_matricula/incluir/', incluir_solicitacao_matricula),
    path('solicitacao_matricula/alterar/<int:id>', alterar_solicitacao_matricula),
    path('solicitacao_matricula/remover/<int:id>', remover_solicitacao_matricula),
    path('admin/', admin.site.urls),
    path('login/',login),
]
