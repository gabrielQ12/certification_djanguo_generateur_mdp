from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render (request, 'generateur/home.html')


def apropos(request):
    return render (request, 'generateur/apropos.html')


def motdepasse(request):


    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    longueur = int(request.GET.get('longueur',12 ))
    if request.GET.get('majuscule'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        caracteres.extend(list('&éèç_çù^$*#'))
    if request.GET.get('nombres'):
        caracteres.extend(list('0123456789'))
    lemotdepasse = ''
    for x in range(longueur) :
        lemotdepasse += random.choice(caracteres)

    return render (request, 'generateur/motdepasse.html', { 'motdepasse':lemotdepasse })