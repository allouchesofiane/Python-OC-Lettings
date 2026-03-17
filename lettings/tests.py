"""Module contenant les tests de l'application lettings."""

import pytest
from django.urls import reverse
from django.test import Client
from lettings.models import Address, Letting


@pytest.fixture
def mon_client():
    """Fixture qui crée un client de test pour simuler un navigateur."""
    return Client()


@pytest.fixture
def une_adresse():
    """Fixture qui crée une adresse de test."""
    return Address.objects.create(
        number=123,
        street='Rue de la Paix',
        city='Paris',
        state='75',
        zip_code=75000,
        country_iso_code='FRA'
    )


@pytest.fixture
def une_location(une_adresse):
    """Fixture qui crée une location de test."""
    return Letting.objects.create(
        title='Bel appartement',
        address=une_adresse
    )


@pytest.mark.django_db
def test_index_url():
    """Test que l'URL de la liste des locations est correcte."""
    url = reverse('lettings:index')
    assert url == '/lettings/'


@pytest.mark.django_db
def test_index_vue_retourne_200(mon_client):
    """Test que la page liste des locations s'affiche correctement."""
    reponse = mon_client.get('/lettings/')
    assert reponse.status_code == 200


@pytest.mark.django_db
def test_index_utilise_bon_template(mon_client):
    """Test que la page liste des locations utilise le bon fichier HTML."""
    reponse = mon_client.get('/lettings/')
    assert 'lettings/index.html' in [t.name for t in reponse.templates]


@pytest.mark.django_db
def test_letting_url(une_location):
    """Test que l'URL du détail d'une location est correcte."""
    url = reverse('lettings:letting', kwargs={'letting_id': une_location.id})
    assert url == f'/lettings/{une_location.id}/'


@pytest.mark.django_db
def test_letting_vue_retourne_200(mon_client, une_location):
    """Test que la page détail d'une location s'affiche correctement."""
    reponse = mon_client.get(f'/lettings/{une_location.id}/')
    assert reponse.status_code == 200


@pytest.mark.django_db
def test_letting_utilise_bon_template(mon_client, une_location):
    """Test que la page détail d'une location utilise le bon fichier HTML."""
    reponse = mon_client.get(f'/lettings/{une_location.id}/')
    assert 'lettings/letting.html' in [t.name for t in reponse.templates]


@pytest.mark.django_db
def test_adresse_str(une_adresse):
    """Test la représentation textuelle d'une adresse."""
    assert str(une_adresse) == '123 Rue de la Paix'


@pytest.mark.django_db
def test_letting_str(une_location):
    """Test la représentation textuelle d'une location."""
    assert str(une_location) == 'Bel appartement'
