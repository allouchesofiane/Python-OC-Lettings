
from django.shortcuts import render


def index(request):
    """Vue affichant la page d'accueil du site."""
    return render(request, 'index.html')


def page_not_found(request):
    """Vue affichant la page d'erreur 404 - page non trouvée."""
    return render(request, '404.html', status=404)


def server_error(request):
    """Vue affichant la page d'erreur 500 - erreur interne du serveur."""
    return render(request, '500.html', status=500)
