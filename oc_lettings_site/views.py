"""Module contenant les vues principales de l'application oc_lettings_site."""
import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """Vue affichant la page d'accueil du site."""
    logger.info('Affichage de la page d accueil')
    return render(request, 'index.html')


def page_not_found(request, exception):
    """Vue affichant la page d'erreur 404 - page non trouvée."""
    logger.warning(f'Page non trouvée: {request.path}')
    return render(request, '404.html', status=404)


def server_error(request):
    """Vue affichant la page d'erreur 500 - erreur interne du serveur."""
    logger.error(f'Erreur serveur sur: {request.path}')
    return render(request, '500.html', status=500)
