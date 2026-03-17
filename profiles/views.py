"""Module contenant les vues de l'application profiles."""
import logging
from django.shortcuts import render
from .models import Profile

logger = logging.getLogger(__name__)

def index(request):
    """Vue affichant la liste de tous les profils."""
    logger.info('Affichage de la liste des profils')
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Vue affichant le détail d'un profil utilisateur."""
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info(f'Affichage du profil {username}')
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        logger.error(f'Profil {username} non trouvé')
        raise
