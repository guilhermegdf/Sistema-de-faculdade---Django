from django.shortcuts import render
from django.http import HttpResponse

def index(request):

     context = {
         'title_doc': 'Home',
         'title_page': 'Welcome',
     }
     return render(request, "index.html", context)


def login(request):
    context_login = {

    }
    return render(request, 'login.html', context_login)
