
from django.shortcuts import render


def index(request):
    """Vue affichant la page d'accueil du site."""
    return render(request, 'index.html')
