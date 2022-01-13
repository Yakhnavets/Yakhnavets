from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import *


def index(request):
    proj = Projects.objects.all()
    return render (request, 'Main/index.html', {'proj': proj})

    #<!--ul>
    #{% for p in proj%}
    #<li>
     #   <h2>{{%p.title%}}</h2>
      #  <p>{{%p.content%}}</p>
       # <hr>
    #</li>
#</ul>



def about(request):
    return render (request, 'Main/about.html')

def galery(request):
    return render (request, 'Main/galery.html')

def contacts(request):
    return render (request, 'Main/contacts.html')

def login(request):
    return render (request, 'Main/login.html')

def singup(reqest):
    return render (reqest, 'Main/singup.html')

def pageNotFound(request, exeption):
    return HttpResponseNotFound ('<h1>Page not Found</h1>')