Base de données et modèles
===========================

La base de données utilisée est **SQLite** en local et en production.

Application lettings
---------------------

Address
--------

Modèle représentant une adresse postale.

.. code-block:: python

    class Address(models.Model):
        number = models.PositiveIntegerField()
        street = models.CharField(max_length=64)
        city = models.CharField(max_length=64)
        state = models.CharField(max_length=2)
        zip_code = models.PositiveIntegerField()
        country_iso_code = models.CharField(max_length=3)

| Champ | Type | Description |
|-------|------|-------------|
| number | PositiveIntegerField | Numéro de rue (max 9999) |
| street | CharField | Nom de la rue |
| city | CharField | Ville |
| state | CharField | État (2 caractères) |
| zip_code | PositiveIntegerField | Code postal (max 99999) |
| country_iso_code | CharField | Code pays ISO (3 caractères) |

Letting
~~~~~~~

Modèle représentant une location.

.. code-block:: python

    class Letting(models.Model):
        title = models.CharField(max_length=256)
        address = models.OneToOneField(Address, on_delete=models.CASCADE)

| Champ | Type | Description |
|-------|------|-------------|
| title | CharField | Titre de la location |
| address | OneToOneField | Adresse liée à la location |

Application profiles
---------------------

Profile
~~~~~~~

Modèle représentant le profil d'un utilisateur.

.. code-block:: python

    class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        favorite_city = models.CharField(max_length=64, blank=True)

| Champ | Type | Description |
|-------|------|-------------|
| user | OneToOneField | Utilisateur lié au profil |
| favorite_city | CharField | Ville favorite de l'utilisateur |

Relations entre les modèles
-----------------------------

.. code-block:: bash

    User (Django)
        │
        └── Profile (OneToOne)

    Address
        │
        └── Letting (OneToOne)