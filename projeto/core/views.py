from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")



def contato(request):
    if request.method == "GET":
        return render(request, "contato.html")
    else:
        print(request.POST.get("nome"))
        print(request.POST.get("email"))
        print(request.POST.get("assunto_msg"))
        print(request.POST.get("texto"))
        print(request.POST.get("palavras_chave"))
    return render(request, "contato.html")



def login(request):
    if request.method == "GET":
        # Render não redireciona, https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/#redirect
        return render(request, "login.html")
    else:
        # VOcê tneta acessar a propriedade usuário, mas ela não existe. Deveria ser email
        if request.POST.get("senha")!="teste123":
            print ("Usuário ",request.POST.get("usuario")," digitou senhaa errada.")
            return render(request, "login.html")
        else:
            print ("Usuário ",request.POST.get("usuario")," entrou com sucesso.")
            return render(request, "index.html")
