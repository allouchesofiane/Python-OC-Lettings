## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Pipeline CI/CD

Le pipeline CI/CD est configuré avec **GitHub Actions** et se compose de 3 étapes :

### 1. Tests et Linting
- Se déclenche sur **toutes les branches**
- Lance `flake8` pour vérifier le style du code
- Lance `pytest` avec une couverture minimum de 80%

### 2. Build et Push Docker
- Se déclenche **uniquement sur master**
- Construit l'image Docker
- Pousse l'image sur Docker Hub avec deux tags :
  - `sofianeall/oc-lettings:latest`
  - `sofianeall/oc-lettings:<hash_commit>`

### 3. Déploiement sur Render
- Se déclenche **uniquement sur master**
- Déclenche le redéploiement sur Render via un Deploy Hook

### Secrets GitHub requis

| Secret | Description |
|--------|-------------|
| `SECRET_KEY` | Clé secrète Django |
| `SENTRY_DSN` | DSN Sentry |
| `DOCKER_USERNAME` | Username Docker Hub |
| `DOCKER_PASSWORD` | Token Docker Hub |
| `RENDER_DEPLOY_HOOK` | URL de déploiement Render |

## Déploiement

### Hébergeur

L'application est déployée sur **Render** :
https://python-oc-lettings-l2ou.onrender.com

### Variables d'environnement sur Render

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Clé secrète Django |
| `SENTRY_DSN` | DSN Sentry |
| `DEBUG` | `False` en production |
| `ALLOWED_HOSTS` | `python-oc-lettings-l2ou.onrender.com` |

### Processus de déploiement

1. Modifier le code
2. Pusher sur la branche `master`
3. GitHub Actions lance automatiquement :
   - Les tests
   - Le build Docker
   - Le déploiement sur Render
4. Le site est mis à jour en quelques minutes

## Sentry

### Configuration

1. Créer un compte sur https://sentry.io
2. Créer un nouveau projet Django
3. Récupérer le DSN du projet
4. Ajouter le DSN dans :
   - Le fichier `.env` en local
   - Les secrets GitHub Actions
   - Les variables d'environnement Render

### Tester Sentry

Ajouter temporairement dans `oc_lettings_site/urls.py` :
```python
def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    ...
    path('sentry-debug/', trigger_error),
]
```

Visiter `/sentry-debug/` pour déclencher une erreur et vérifier qu'elle apparaît sur le dashboard Sentry.

## Lancer avec Docker

Récupérer et lancer l'image en une seule commande :
```bash
docker-compose up
```

Le site est accessible sur **http://localhost:8000**