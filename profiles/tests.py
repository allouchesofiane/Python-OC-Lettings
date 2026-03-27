"""Module contenant les tests de l'application profiles."""

import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.fixture
def mon_client():
    """Fixture qui crée un client de test pour simuler un navigateur."""
    return Client()


@pytest.fixture
def un_utilisateur():
    """Fixture qui crée un utilisateur de test."""
    return User.objects.create_user(
        username='testuser',
        password='testpass123',
        first_name='John',
        last_name='Doe',
        email='john@test.com'
    )


@pytest.fixture
def un_profil(un_utilisateur):
    """Fixture qui crée un profil de test."""
    return Profile.objects.create(
        user=un_utilisateur,
        favorite_city='Paris'
    )


@pytest.mark.django_db
def test_index_url():
    """Test que l'URL de la liste des profils est correcte."""
    url = reverse('profiles:index')
    assert url == '/profiles/'


@pytest.mark.django_db
def test_index_vue_retourne_200(mon_client):
    """Test que la page liste des profils s'affiche correctement."""
    reponse = mon_client.get('/profiles/')
    assert reponse.status_code == 200


@pytest.mark.django_db
def test_index_utilise_bon_template(mon_client):
    """Test que la page liste des profils utilise le bon fichier HTML."""
    reponse = mon_client.get('/profiles/')
    assert 'profiles/index.html' in [t.name for t in reponse.templates]


@pytest.mark.django_db
def test_profile_url(un_profil):
    """Test que l'URL du détail d'un profil est correcte."""
    url = reverse(
        'profiles:profile',
        kwargs={'username': un_profil.user.username}
        )
    assert url == f'/profiles/{un_profil.user.username}/'


@pytest.mark.django_db
def test_profile_vue_retourne_200(mon_client, un_profil):
    """Test que la page détail d'un profil s'affiche correctement."""
    reponse = mon_client.get(f'/profiles/{un_profil.user.username}/')
    assert reponse.status_code == 200


@pytest.mark.django_db
def test_profile_utilise_bon_template(mon_client, un_profil):
    """Test que la page détail d'un profil utilise le bon fichier HTML."""
    reponse = mon_client.get(f'/profiles/{un_profil.user.username}/')
    assert 'profiles/profile.html' in [t.name for t in reponse.templates]


@pytest.mark.django_db
def test_profile_str(un_profil):
    """Test la représentation textuelle d'un profil."""
    assert str(un_profil) == 'testuser'
