from django.shortcuts import render, redirect, get_object_or_404
from restrito.models import atividades, AtividadeVinculada, entrega, SolicitacaoMatricula
from contas.models import professores, alunos, coordenadores
from curriculo.models import disciplinas_ofertada
# Create your views here.

def lista_restrito(request):
    context_restrito = {
        'restrito':[
            'atividade',
            'atividade_vinculada',
            'solicitacao_matricula',
            'entrega',
        ]
    }
    return render(request, 'lista_restrito.html', context_restrito)
def Atividade(request):

    context_Atividade = {
        "atividade_lista":atividades.Atividade.objects.all()
    }
    return render(request, "atividade.html", context_Atividade)

def incluirAtividade(request):
    context = {
        'professores_lista':professores.Professores.objects.all(),
        'tipos':['Resposta aberta', 'Teste'],
    }
    if request.POST:
        atividades.Atividade.objects.create(
            titulo=request.POST.get("titulo"),
            descricao=request.POST.get("descricao"),
            conteudo=request.POST.get("conteudo"),
            tipo=request.POST.get("tipo"),
            idprofessores=professores.Professores.objects.get(id=request.POST.get('idprofessores')),
        )
        return redirect("/atividade/")
    else:
        return render(request, "nova_atividade.html", context)

def alterarAtividade(request, id):
    context = {
        'professores_lista':professores.Professores.objects.all(),
        'tipos':['Resposta aberta', 'Teste'],
    }
    if request.POST:
        atividade = atividades.Atividade.objects.get(id=id)

        atividade.titulo=request.POST.get("titulo")
        atividade.descricao=request.POST.get("descricao")
        atividade.conteudo=request.POST.get("conteudo")
        atividade.tipo=request.POST.get("tipo")
        atividade.idprofessores=professores.Professores.objects.get(id=request.POST.get('idprofessores'))
        
        atividade.save()
        return redirect("/atividade/")
    else:
        context['atividade'] = atividades.Atividade.objects.get(id=id)
        return render(request,'nova_atividade.html', context)
'''
def removerAtividade(request, id):
    context = {}
    atividade = get_object_or_404(atividades.Atividade, id=id)
    
    if request.POST:
        atividade.delete()
        return redirect("/atividade/")
    else:
        context['nome'] = atividades.Atividade.objects.get(id=id)
        return render(request,'remover.html',context)
'''
def removerAtividade(request, id):
    post = get_object_or_404(atividades.Atividade, id=id)
    post.delete()
    return redirect('/atividade/')

def atividade_vinculada(request):

    context_AtividadeVinc = {
        "atividade_vinc_lista":AtividadeVinculada.Atividadevinculada.objects.all()
    }
    return render(request, "atividade_vinculada.html", context_AtividadeVinc)

def incluiratividade_vinculada(request):
    context = {
        'professores_lista':professores.Professores.objects.all(),
        'disciplinaof_lista':disciplinas_ofertada.DisciplinaOfertada.objects.all(),
        'atividades_lista':atividades.Atividade.objects.all(),
        'status':['Escolha','Disponibilizada', 'Aberta', 'Fechada','Encerrada', 'Prorrogada'],
    }
    if request.POST:
        AtividadeVinculada.Atividadevinculada.objects.create(
            rotulo=request.POST.get("rotulo"),
            status=request.POST.get("status"),
            dtiniciorespostas=request.POST.get("dtiniciorespostas"),
            dtfimrespostas=request.POST.get("dtfimrespostas"),
            idatividade=atividades.Atividade.objects.get(id=request.POST.get('idatividade')),
            iddisciplinaofertada=disciplinas_ofertada.DisciplinaOfertada.objects.get(id=request.POST.get('iddisciplinaofertada')),
            idprofessores=professores.Professores.objects.get(id=request.POST.get('idprofessores')),
        )
        return redirect("/atividade_vinculada/")
    else:
        return render(request, "nova_atividade_vinculada.html", context)

def alteraratividade_vinculada(request, id):
    context = {
        'professores_lista':professores.Professores.objects.all(),
        'disciplinaof_lista':disciplinas_ofertada.DisciplinaOfertada.objects.all(),
        'atividades_lista':atividades.Atividade.objects.all(),
        'status':['Disponibilizada', 'Aberta', 'Fechada','Encerrada', 'Prorrogada'],
    }
    if request.POST:
        atividadevinc = AtividadeVinculada.Atividadevinculada.objects.get(id=id)
        atividadevinc.rotulo=request.POST.get("rotulo")
        atividadevinc.status=request.POST.get("status")
        atividadevinc.dtiniciorespostas=request.POST.get("dtiniciorespostas")
        atividadevinc.dtfimrespostas=request.POST.get("dtfimrespostas")
        atividadevinc.idatividade=atividades.Atividade.objects.get(id=request.POST.get('idatividade'))
        atividadevinc.iddisciplinaofertada=disciplinas_ofertada.DisciplinaOfertada.objects.get(id=request.POST.get('iddisciplinaofertada'))
        atividadevinc.idprofessores=professores.Professores.objects.get(id=request.POST.get('idprofessores'))
        atividadevinc.save()
        return redirect("/atividade_vinculada/")
    else:
        context['atividadevinc'] = AtividadeVinculada.Atividadevinculada.objects.get(id=id)
        return render(request,'nova_atividade_vinculada.html', context)

def removeratividade_vinculada(request, id):
    context = {}
    ativinc = get_object_or_404(AtividadeVinculada.Atividadevinculada, id=id)
    
    if request.POST:
        ativinc.delete()
        return redirect("/atividade_vinculada/")
    else:
        context['nome'] = AtividadeVinculada.Atividadevinculada.objects.get(id=id)
        return render(request,'remover.html',context)


def entrega_lista(request):

    context_Entrega = {
        "entrega_lista":entrega.Entrega.objects.all()
    }
    return render(request, "entrega.html", context_Entrega)

def incluir_entrega(request):
    context = {
        'professores_lista':professores.Professores.objects.all(),
        'aluno_lista':alunos.Aluno.objects.all(),
        'coordenador_lista':coordenadores.Coordenador.objects.all(),
        'status':['Entregue', 'Corrigido'],
    }
    if request.POST:
        entrega.Entrega.objects.create(
            titulo=request.POST.get("titulo"),
            resposta=request.POST.get("resposta"),
            dtentrega=request.POST.get("dtentrega"),
            status=request.POST.get("status"),
            nota=request.POST.get("nota"),
            dtavaliacao=request.POST.get("dtavaliacao"),
            obs=request.POST.get("obs"),
            idaluno=alunos.Aluno.objects.get(id=request.POST.get('idaluno')),
            idcoordenador=coordenadores.Coordenador.objects.get(id=request.POST.get('idcoordenador')),
            idprofessores=professores.Professores.objects.get(id=request.POST.get('idprofessores')),
        )
        return redirect("/entrega/")
    else:
        return render(request, "nova_entrega.html", context)

def alterar_entrega(request, id):
    context = {
        'professores_lista':professores.Professores.objects.all(),
        'aluno_lista':alunos.Aluno.objects.all(),
        'coordenador_lista':coordenadores.Coordenador.objects.all(),
        'status':['Entregue', 'Corrigido'],
    }
    if request.POST:
        altentrega = entrega.Entrega.objects.get(id=id)
        altentrega.titulo=request.POST.get("titulo")
        altentrega.resposta=request.POST.get("resposta")
        altentrega.dtentrega=request.POST.get("dtentrega")
        altentrega.status=request.POST.get("status")
        altentrega.nota=request.POST.get("nota")
        altentrega.dtavaliacao=request.POST.get("dtavaliacao")
        altentrega.obs=request.POST.get("obs")
        altentrega.idaluno=alunos.Aluno.objects.get(id=request.POST.get('idaluno'))
        altentrega.idcoordenador=coordenadores.Coordenador.objects.get(id=request.POST.get('idcoordenador'))
        altentrega.idprofessores=professores.Professores.objects.get(id=request.POST.get('idprofessores'))
        altentrega.save()
        return redirect("/atividade_vinculada/")
    else:
        context['altentrega'] = entrega.Entrega.objects.get(id=id)
        return render(request,'nova_entrega.html', context)

def remover_entrega(request, id):
    context = {}
    entrega = get_object_or_404(entrega.Entrega, id=id)
    
    if request.POST:
        entrega.delete()
        return redirect("/entrega/")
    else:
        context['nome'] = entrega.Entrega.objects.get(id=id)
        return render(request,'remover.html',context)


def solicitacao_matricula_lista(request):

    context_Entrega = {
        "solic_matri":SolicitacaoMatricula.Solicitacaomatricula.objects.all()
    }
    return render(request, "solicitacao_matricula.html", context_Entrega)

def incluir_solicitacao_matricula(request):
    context = {
        'discof_lista':disciplinas_ofertada.DisciplinaOfertada.objects.all(),
        'aluno_lista':alunos.Aluno.objects.all(),
        'coordenador_lista':coordenadores.Coordenador.objects.all(),
        'status':['Solicitada', 'Aprovada', 'Rejeitada', 'Cancelada'],
    }
    if request.POST:
        SolicitacaoMatricula.Solicitacaomatricula.objects.create(
            status=request.POST.get("status"),
            dtsolicitacao=request.POST.get("dtsolicitacao"),
            idaluno=alunos.Aluno.objects.get(id=request.POST.get('idaluno')),
            idcoordenador=coordenadores.Coordenador.objects.get(id=request.POST.get('idcoordenador')),
            iddisciplinaofertada=disciplinas_ofertada.DisciplinaOfertada.objects.get(id=request.POST.get('iddisciplinaofertada')),
        )
        return redirect("/solicitacao_matricula/")
    else:
        return render(request, "nova_solicitacao_matricula.html", context)

def alterar_solicitacao_matricula(request, id):
    context = {
        'discof_lista':disciplinas_ofertada.DisciplinaOfertada.objects.all(),
        'aluno_lista':alunos.Aluno.objects.all(),
        'coordenador_lista':coordenadores.Coordenador.objects.all(),
        'status':['Solicitada', 'Aprovada', 'Rejeitada', 'Cancelada'],
    }
    if request.POST:
        solicitmatricula = SolicitacaoMatricula.Solicitacaomatricula.objects.get(id=id)
        solicitmatricula.status=request.POST.get("status")
        solicitmatricula.dtsolicitacao=request.POST.get("dtsolicitacao")
        solicitmatricula.idaluno=alunos.Aluno.objects.get(id=request.POST.get('idaluno'))
        solicitmatricula.idcoordenador=coordenadores.Coordenador.objects.get(id=request.POST.get('idcoordenador'))
        solicitmatricula.iddisciplinaofertada=disciplinas_ofertada.DisciplinaOfertada.objects.get(id=request.POST.get('iddisciplinaofertada'))
        solicitmatricula.save()
        return redirect("/solicitacao_matricula/")
    else:
        context['solicitmatricula'] = SolicitacaoMatricula.Solicitacaomatricula.objects.get(id=id)
        return render(request,'nova_solicitacao_matricula.html', context)

def remover_solicitacao_matricula(request, id):
    context = {}
    solic_matricula = get_object_or_404(SolicitacaoMatricula.Solicitacaomatricula, id=id)
    
    if request.POST:
        solic_matricula.delete()
        return redirect("/solicitacao_matricula/")
    else:
        context['nome'] = SolicitacaoMatricula.Solicitacaomatricula.objects.get(id=id)
        return render(request,'remover.html',context)