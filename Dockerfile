# Image de base Python
FROM python:3.13-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code
COPY . .

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer le port
EXPOSE 8000

# Lancer le serveur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]