"""Module contenant les vues de l'application lettings."""
import logging
from django.shortcuts import render
from .models import Letting

logger = logging.getLogger(__name__)

def index(request):
    """Vue affichant la liste de toutes les locations."""
    logger.info('Affichage de la liste des locations')
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Vue affichant le détail d'une location."""
    try:
        letting = Letting.objects.get(id=letting_id)
        logger.info(f'Affichage de la location {letting_id}')
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.error(f'Location {letting_id} non trouvée')
        raise