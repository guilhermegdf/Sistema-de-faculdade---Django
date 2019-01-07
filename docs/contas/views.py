from django.shortcuts import render, redirect, get_object_or_404
from contas.models import alunos, professores, coordenadores, mensagens

# Create your views here.

def lista_contas(request):
    context_contas = {
        'conta':[
            'Aluno',
            'Coordenador',
            'Professor',
            'Mensagem',
        ]
    }
    return render(request, 'lista_contas.html', context_contas)

def Aluno(request):

    context_Aluno = {
        "aluno":alunos.Aluno.objects.all()
    }
    return render(request, "aluno.html", context_Aluno)

def incluirAluno(request):
    context = {}
    if request.POST:
        alunos.Aluno.objects.create(
            login=request.POST.get("login"),
            senha=request.POST.get("senha"),
            nome=request.POST.get("nome"),
            email=request.POST.get("email"),
            celular=request.POST.get("celular"),
            ra=request.POST.get("ra"),
            dtexpiracao=request.POST.get("dtexpiracao"),
            foto=request.POST.get("foto"),
        )
        return redirect('/contas/Aluno/')
    else:
        return render(request, "novo_aluno.html", context)

def alterarAluno(request, id):
    context = {}
    if request.POST:
        aluno = alunos.Aluno.objects.get(id=id)

        aluno.login=request.POST.get("login")
        aluno.senha=request.POST.get("senha")
        aluno.nome=request.POST.get("nome")
        aluno.email=request.POST.get("email")
        aluno.celular=request.POST.get("celular")
        aluno.ra=request.POST.get("ra")
        aluno.dtexpiracao=request.POST.get("dtexpiracao")
        aluno.foto=request.POST.get("foto")
        aluno.save()
        return redirect('/contas/Aluno/')
    else:
        context['aluno'] = alunos.Aluno.objects.get(id=id)
        return render(request,'novo_aluno.html', context)

def removerAluno(request, id):
    context = {}
    aluno = get_object_or_404(alunos.Aluno, id=id)
    
    if request.POST:
        aluno.delete()
        return redirect("/contas/Aluno/")
    else:
        context['nome'] = alunos.Aluno.objects.get(id=id)
        return render(request,'remover.html',context)

def Professor(request):

    context_Professor = {
        "professor":professores.Professores.objects.all()
    }
    return render(request, "professor.html", context_Professor)

def incluirProfessor(request):
    context = {}
    if request.POST:
        professores.Professores.objects.create(
            login=request.POST.get("login"),
            senha=request.POST.get("senha"),
            nome=request.POST.get("nome"),
            email=request.POST.get("email"),
            celular=request.POST.get("celular"),
            apelido=request.POST.get("apelido"),
            dtexpiracao=request.POST.get("dtexpiracao")
        )
        return redirect("/contas/Professor/")
    else:
        return render(request, "novo_professor.html", context)

def alterarProfessor(request, id):
    context = {}
    if request.POST:
        professor = professores.Professores.objects.get(id=id)

        professor.login=request.POST.get("login")
        professor.senha=request.POST.get("senha")
        professor.nome=request.POST.get("nome")
        professor.email=request.POST.get("email")
        professor.celular=request.POST.get("celular")
        professor.apelido=request.POST.get("apelido")
        professor.dtexpiracao=request.POST.get("dtexpiracao")
        professor.save()
        return redirect("/contas/Professor/")
    else:
        context['professor'] = professores.Professores.objects.get(id=id)
        return render(request,'novo_professor.html', context)

def removerProfessor(request, id):
    context = {}
    professor = get_object_or_404(professores.Professores, id=id)
    
    if request.POST:
        professor.delete()
        return redirect("/contas/Professor/")
    else:
        context['nome'] = professores.Professores.objects.get(id=id)
        return render(request,'remover.html',context)

def Coordenador(request):

    context_Coordenador = {
        "coordenador":coordenadores.Coordenador.objects.all()
    }
    return render(request, "coordenador.html", context_Coordenador)

def incluirCoordenador(request):
    context = {}
    if request.POST:
        coordenadores.Coordenador.objects.create(
            login=request.POST.get("login"),
            senha=request.POST.get("senha"),
            nome=request.POST.get("nome"),
            email=request.POST.get("email"),
            celular=request.POST.get("celular"),
            dtexpiracao=request.POST.get("dtexpiracao"),

        )
        return redirect("/contas/Coordenador/")
    else:
        return render(request, "novo_coordenador.html", context)

def alterarCoordenador(request, id):
    context = {}
    if request.POST:
        coordenador = coordenadores.Coordenador.objects.get(id=id)

        coordenador.login=request.POST.get("login")
        coordenador.senha=request.POST.get("senha")
        coordenador.nome=request.POST.get("nome")
        coordenador.email=request.POST.get("email")
        coordenador.celular=request.POST.get("celular")
        coordenador.dtexpiracao=request.POST.get("dtexpiracao")
        coordenador.save()
        return redirect("/contas/Coordenador/")
    else:
        context['coordenador'] = coordenadores.Coordenador.objects.get(id=id)
        return render(request,'novo_coordenador.html', context)

def removerCoordenador(request, id):
    context = {}
    coordenador = get_object_or_404(coordenadores.Coordenador, id=id)
    
    if request.POST:
        coordenador.delete()
        return redirect("/contas/Coordenador/")
    else:
        context['nome'] = coordenadores.Coordenador.objects.get(id=id)
        return render(request,'remover.html',context)

def Mensagem(request):

    context_Mensagem = {
        "mensagem_lista":mensagens.Mensagem.objects.all()
    }
    return render(request, "mensagem.html", context_Mensagem)

def incluirMensagem(request):
    context = {
        'professores_lista':professores.Professores.objects.all(),
        'alunos':alunos.Aluno.objects.all(),
        'status':['Enviado', 'Lido', 'Respondido']
    }
    if request.POST:
        mensagens.Mensagem.objects.create(
            assunto=request.POST.get("assunto"),
            referencia=request.POST.get("referencia"),
            conteudo=request.POST.get("conteudo"),
            status=request.POST.get("status"),
            dtenvio=request.POST.get("dtenvio"),
            dtresposta=request.POST.get("dtresposta"),
            resposta=request.POST.get("resposta"),
            idaluno=alunos.Aluno.objects.get(id=request.POST.get("idaluno")),
            idprofessores=professores.Professores.objects.get(id=request.POST.get("idprofessor")),
        )
        return redirect("/contas/Mensagem/")
    else:
        return render(request, "nova_mensagem.html", context)

def alterarMensagem(request, id):
    context = {
        'professores_lista':professores.Professores.objects.all(),
        'alunos':alunos.Aluno.objects.all(),
        'status':['Enviado', 'Lido', 'Respondido']
    }
    if request.POST:
        mensagem = mensagens.Mensagem.objects.get(id=id)

        mensagem.assunto=request.POST.get("assunto")
        mensagem.referencia=request.POST.get("referencia")
        mensagem.conteudo=request.POST.get("conteudo")
        mensagem.status=request.POST.get("status")
        mensagem.dtenvio=request.POST.get("dtenvio")
        mensagem.dtresposta=request.POST.get("dtresposta")
        mensagem.resposta=request.POST.get("resposta")
        mensagem.idaluno=alunos.Aluno.objects.get(id=request.POST.get("idaluno"))
        mensagem.idprofessores=professores.Professores.objects.get(id=request.POST.get("idprofessor"))

        mensagem.save()
        return redirect("/contas/Mensagem/")
    else:
        context['mensagem'] = mensagens.Mensagem.objects.get(id=id)
        return render(request,'nova_mensagem.html', context)

def removerMensagem(request, id):
    context = {}
    mensagem = get_object_or_404(mensagens.Mensagem, id=id)
    
    if request.POST:
        mensagem.delete()
        return redirect("/contas/Mensagem/")
    else:
        context['nome'] = mensagens.Mensagem.objects.get(id=id)
        return render(request,'remover.html',context)