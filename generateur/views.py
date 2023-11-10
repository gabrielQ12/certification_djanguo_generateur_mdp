from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render (request, 'generateur/home.html', {'mdp':'bonjour35'})


def motdepasse(request):
     return render (request, 'generateur/motdepasse.html')