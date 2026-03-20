Installation
============

Prérequis
---------

- Compte GitHub
- Git CLI
- Python 3.13 ou supérieur
- Docker Desktop

Cloner le repository
--------------------

.. code-block:: bash

    git clone https://github.com/allouchesofiane/Python-OC-Lettings.git
    cd Python-OC-Lettings

Créer l'environnement virtuel
------------------------------

.. code-block:: bash

    python -m venv venv

Activer l'environnement virtuel
--------------------------------

Sur Windows :

.. code-block:: bash

    venv\Scripts\activate

Sur macOS/Linux :

.. code-block:: bash

    source venv/bin/activate

Installer les dépendances
--------------------------

.. code-block:: bash

    pip install -r requirements.txt

Configurer les variables d'environnement
-----------------------------------------

Crée un fichier ``.env`` à la racine du projet :

.. code-block:: bash

    SECRET_KEY=ta_clé_secrète
    SENTRY_DSN=ton_dsn_sentry
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1

Lancer les migrations
----------------------

.. code-block:: bash

    python manage.py migrate

Lancer le site
---------------

.. code-block:: bash

    python manage.py runserver