from django.shortcuts import render, redirect, get_object_or_404
from curriculo.models import cursos, disciplinas, disciplinas_ofertada
from contas.models import professores, coordenadores

# Create your views here.

def lista_curriculo(request):
    context_curriculo = {
        'curriculo':[
            'cursos',
            'disciplina',
            'disciplina_ofertada',
        ]
    }
    return render(request, 'lista_curriculo.html', context_curriculo)

def cursos_lista(request):

    context_cursos_lista = {
        "cursos_lista":cursos.Curso.objects.all(),
        "img":'http://lorempixel.com/300/100/',
    }
    return render(request, "cursos.html", context_cursos_lista)

def alterarCurso(request, id):
    context = {}
    if request.POST:
        curso = cursos.Curso.objects.get(id=id)

        curso.nome=request.POST.get("nome")
        curso.sigla=request.POST.get("sigla")

        curso.save()
        return redirect("/cursos/")
    else:
        context['curso'] = cursos.Curso.objects.get(id=id)
        return render(request,'novo_curso.html', context)

def incluirCurso(request):
    context = {}
    if request.POST:
        cursos.Curso.objects.create(
            nome=request.POST.get("nome"),
            sigla=request.POST.get("sigla")
        )
        return redirect("/cursos/")
    else:
        return render(request, "novo_curso.html", context)

def removerCurso(request, id):
    context = {}
    curso = get_object_or_404(cursos.Curso, id=id)
    
    if request.POST:
        curso.delete()
        return redirect("/cursos/")
    else:
        context['nome'] = cursos.Curso.objects.get(id=id)
        return render(request,'remover.html',context)
    


def disciplina(request):

    context_disciplina = {
        "disciplina":disciplinas.Disciplina.objects.all(),
    }
    return render(request, "disciplina.html", context_disciplina)

def incluirDisciplina(request):
    context = {
        'status':['Aberta', 'Fechada']
    }
    if request.POST:
        disciplinas.Disciplina.objects.create(
            nome=request.POST.get("nome"),
            data=request.POST.get("data"),
            status=request.POST.get("status"),
            planodeensino=request.POST.get("planodeensino"),
            cargahoraria=request.POST.get("cargahoraria"),
            competencias=request.POST.get("competencias"),
            habilidades=request.POST.get("habilidades"),
            ementa=request.POST.get("ementa"),
            conteudoprogramatico=request.POST.get("conteudoprogramatico"),
            bibliografiabasica=request.POST.get("bibliografiabasica"),
            bibliografiacomplementar=request.POST.get("bibliografiacomplementar"),
            percentualpratico=request.POST.get("percentualpratico"),
            percentualteorico=request.POST.get("percentualteorico"),
        )
        return redirect("/disciplina/")
    else:
        return render(request, "nova_disciplina.html", context)

def alterarDisciplina(request, id):
    context = {
        'status':['Aberta', 'Fechada']
    }

    if request.POST:
        disciplina = disciplinas.Disciplina.objects.get(id=id)

        disciplina.nome=request.POST.get("nome")
        disciplina.data=request.POST.get("data")
        disciplina.status=request.POST.get("status")
        disciplina.planodeensino=request.POST.get("planodeensino")
        disciplina.cargahoraria=request.POST.get("cargahoraria")
        disciplina.competencias=request.POST.get("competencias")
        disciplina.habilidades=request.POST.get("habilidades")
        disciplina.ementa=request.POST.get("ementa")
        disciplina.conteudoprogramatico=request.POST.get("conteudoprogramatico")
        disciplina.bibliografiabasica=request.POST.get("bibliografiabasica")
        disciplina.bibliografiacomplementar=request.POST.get("bibliografiacomplementar")
        disciplina.percentualpratico=request.POST.get("percentualpratico")
        disciplina.percentualteorico=request.POST.get("percentualteorico")

        disciplina.save()
        return redirect("/disciplina/")
    else:
        context['disciplina'] = disciplinas.Disciplina.objects.get(id=id)
        return render(request,'nova_disciplina.html', context)

def removerDisciplina(request, id):
    context = {}
    disciplina = get_object_or_404(disciplinas.Disciplina, id=id)
    
    if request.POST:
        disciplina.delete()
        return redirect("/discipina/")
    else:
        context['nome'] = discipina.Disciplinas.objects.get(id=id)
        return render(request,'remover.html',context)

def disciplinaOfertada_lista(request):
    context = {
        "Discip_of":disciplinas_ofertada.DisciplinaOfertada.objects.all(),
    }
    return render(request, "Disciplina_ofertada.html", context)

def incluirDisciplinaOfertada(request):
    context = {
        'professores_lista':professores.Professores.objects.all(),
        'coordenadores_lista':coordenadores.Coordenador.objects.all(),
        'curso_lista':cursos.Curso.objects.all(),
        'disciplina_lista':disciplinas.Disciplina.objects.all(),
    }
    if request.POST:
        disciplinas_ofertada.DisciplinaOfertada.objects.create(
            dtinicniomatricula=request.POST.get("dtinicniomatricula"),
            dtfimmatricula=request.POST.get("dtfimmatricula"),
            ano=request.POST.get("ano"),
            semestre=request.POST.get("semestre"),
            turma=request.POST.get("turma"),
            metodologia=request.POST.get("metodologia"),
            recursos=request.POST.get("recursos"),
            criterioavaliacao=request.POST.get("criterioavaliacao"),
            planodeaulas=request.POST.get("planodeaulas"),
            idcoordenador=contas.models.coordenadores.Coordenador.objects.get(id=request.POST.get("idcoordenador")),
            idcurso=cursos.Curso.objects.get(id=request.POST.get("idcurso")),
            iddisciplina=disciplinas.Disciplina.objects.get(id=request.POST.get("iddisciplina")),
            idprofessor=professores.Professores.objects.get(id=request.POST.get("idprofessor")),
        )
        return redirect("/disciplina_ofertada/")
    else:
        return render(request, "Nova_Disciplina_ofertada.html", context)

def alterarDisciplinaOfertada(request, id):
    context = {
        'professores_lista':professores.Professores.objects.all(),
        'coordenadores_lista':coordenadores.Coordenador.objects.all(),
        'curso_lista':cursos.Curso.objects.all(),
        'disciplina_lista':disciplinas.Disciplina.objects.all(),
    }

    if request.POST:
        disciplinaof = disciplinas_ofertada.DisciplinaOfertada.objects.get(id=id)

        disciplinaof.dtinicniomatricula=request.POST.get("dtinicniomatricula")
        disciplinaof.dtfimmatricula=request.POST.get("dtfimmatricula")
        disciplinaof.ano=request.POST.get("ano")
        disciplinaof.semestre=request.POST.get("semestre")
        disciplinaof.turma=request.POST.get("turma")
        disciplinaof.metodologia=request.POST.get("metodologia")
        disciplinaof.recursos=request.POST.get("recursos")
        disciplinaof.criterioavaliacao=request.POST.get("criterioavaliacao")
        disciplinaof.planodeaulas=request.POST.get("planodeaulas")
        disciplinaof.idcoordenador=coordenadores.Coordenador.objects.get(id=request.POST.get("idcoordenador"))
        disciplinaof.idcurso=cursos.Curso.objects.get(id=request.POST.get("idcurso"))
        disciplinaof.iddisciplina=disciplinas.Disciplina.objects.get(id=request.POST.get("iddisciplina"))
        disciplinaof.idprofessores=professores.Professores.objects.get(id=request.POST.get("idprofessor"))
        
        disciplinaof.save()

        return redirect("/disciplina_ofertada/")
    else:
        context['disciplinaof'] = disciplinas_ofertada.DisciplinaOfertada.objects.get(id=id)
        return render(request,'Nova_Disciplina_ofertada.html', context)

def removerDisciplinaOfertada(request, id):
    context = {}
    discof = get_object_or_404(disciplinas_ofertada.DisciplinaOfertada, id=id)
    
    if request.POST:
        discof.delete()
        return redirect("/disciplina_ofertada/")
    else:
        context['nome'] = disciplinas_ofertada.DisciplinaOfertada.objects.get(id=id)
        return render(request,'remover.html',context)