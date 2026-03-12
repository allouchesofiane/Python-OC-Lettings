"""Module contenant les vues de l'application profiles."""
from django.shortcuts import render
from .models import Profile


def index(request):
    """Vue affichant la liste de tous les profils."""
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Vue affichant le détail d'un profil utilisateur."""
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
