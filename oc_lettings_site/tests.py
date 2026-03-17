"""Module contenant les tests de l'application oc_lettings_site."""

import pytest
from django.urls import reverse
from django.test import Client


@pytest.fixture
def mon_client():
    """Fixture qui crée un client de test pour simuler un navigateur."""
    return Client()


@pytest.mark.django_db
def test_index_url():
    """Test que l'URL de la page d'accueil est bien '/'."""
    url = reverse('index')
    assert url == '/'


@pytest.mark.django_db
def test_index_vue_retourne_200(mon_client):
    """Test que la page d'accueil s'affiche correctement."""
    reponse = mon_client.get('/')
    assert reponse.status_code == 200


@pytest.mark.django_db
def test_index_utilise_bon_template(mon_client):
    """Test que la page d'accueil utilise le bon fichier HTML."""
    reponse = mon_client.get('/')
    assert 'index.html' in [t.name for t in reponse.templates]
