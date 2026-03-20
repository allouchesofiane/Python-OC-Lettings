Guide de démarrage rapide
==========================

Ce guide vous permet de lancer le site en quelques minutes.

Lancer le site en local
------------------------

.. code-block:: bash

    git clone https://github.com/allouchesofiane/Python-OC-Lettings.git
    cd Python-OC-Lettings
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Le site est accessible sur **http://127.0.0.1:8000**

Lancer le site avec Docker
---------------------------

.. code-block:: bash

    docker-compose up

Le site est accessible sur **http://localhost:8000**

Accéder à l'interface d'administration
----------------------------------------

- URL : http://127.0.0.1:8000/admin
- Identifiant : ``admin``
- Mot de passe : ``Abc1234!``

Lancer les tests
-----------------

.. code-block:: bash

    pytest --cov=. --cov-report=term-missing

Lancer le linting
------------------

.. code-block:: bash

    flake8