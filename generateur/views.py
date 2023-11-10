from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('bonjour')


def test(request):
    return HttpResponse('Votre page test')