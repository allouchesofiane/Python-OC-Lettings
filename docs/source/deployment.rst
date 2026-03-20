Déploiement et gestion de l'application
=========================================

Cette section décrit comment déployer et gérer l'application en production.

Variables d'environnement
--------------------------

Les variables suivantes sont nécessaires pour faire fonctionner l'application :

.. list-table::
   :header-rows: 1

   * - Variable
     - Description
     - Exemple
   * - ``SECRET_KEY``
     - Clé secrète Django
     - ``fp$9^593hsriajg...``
   * - ``DEBUG``
     - Mode debug
     - ``False`` en production
   * - ``ALLOWED_HOSTS``
     - Domaines autorisés
     - ``python-oc-lettings-l2ou.onrender.com``
   * - ``SENTRY_DSN``
     - DSN Sentry pour la surveillance
     - ``https://xxx@xxx.ingest.sentry.io/xxx``

Configurer Sentry
------------------

1. Créer un compte sur **https://sentry.io**
2. Créer un nouveau projet Django
3. Récupérer le DSN du projet
4. Ajouter le DSN dans le fichier ``.env`` en local :

.. code-block:: bash

    SENTRY_DSN=https://xxx@xxx.ingest.sentry.io/xxx

5. Ajouter le DSN dans les secrets GitHub Actions :

   - Aller sur GitHub → Settings → Secrets → Actions
   - Ajouter ``SENTRY_DSN`` avec la valeur du DSN

6. Ajouter le DSN dans les variables d'environnement Render :

   - Aller sur Render → ton service → Environment
   - Ajouter ``SENTRY_DSN`` avec la valeur du DSN

Pipeline CI/CD
---------------

Le pipeline CI/CD est configuré avec GitHub Actions.
Il est composé de 3 jobs :

1. **Tests et Linting** : se déclenche sur toutes les branches

.. code-block:: bash

    flake8
    pytest --cov=. --cov-fail-under=80

2. **Build et Push Docker** : se déclenche uniquement sur master

.. code-block:: bash

    docker build
    docker push sofianeall/oc-lettings:latest

3. **Déploiement sur Render** : se déclenche uniquement sur master

.. code-block:: bash

    curl -X POST $RENDER_DEPLOY_HOOK

Déploiement manuel
-------------------

Pour déclencher un déploiement manuellement :

1. Aller sur **https://render.com**
2. Cliquer sur ton service ``Python-OC-Lettings``
3. Cliquer sur **Manual Deploy**
4. Cliquer sur **Deploy latest commit**

Lancer le site avec Docker
---------------------------

Récupérer et lancer l'image en une seule commande :

.. code-block:: bash

    docker-compose up

Le site est accessible sur **http://localhost:8000**

Ou avec la commande complète :

.. code-block:: bash

    docker run -p 8000:8000 \
      -e SECRET_KEY="ta_clé_secrète" \
      -e DEBUG="True" \
      -e ALLOWED_HOSTS="localhost,127.0.0.1" \
      -e SENTRY_DSN="ton_dsn_sentry" \
      sofianeall/oc-lettings:latest

Rollback
---------

Pour revenir à une version précédente :

1. Aller sur **https://render.com**
2. Cliquer sur ton service
3. Aller dans **Events**
4. Cliquer sur **Rollback** sur la version souhaitée