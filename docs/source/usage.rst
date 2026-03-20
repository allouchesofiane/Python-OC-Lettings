Guide d'utilisation
====================

Ce guide décrit les cas d'utilisation du site OC Lettings.

Cas d'utilisation 1 — Consulter les locations
-----------------------------------------------

1. Ouvrir le navigateur sur **http://127.0.0.1:8000**
2. Cliquer sur le bouton **Lettings**
3. La liste de toutes les locations s'affiche
4. Cliquer sur une location pour voir son détail :

   - Titre de la location
   - Adresse complète
   - Ville, état, code postal
   - Code pays

Cas d'utilisation 2 — Consulter les profils
---------------------------------------------

1. Ouvrir le navigateur sur **http://127.0.0.1:8000**
2. Cliquer sur le bouton **Profiles**
3. La liste de tous les profils s'affiche
4. Cliquer sur un profil pour voir son détail :

   - Nom d'utilisateur
   - Prénom et nom
   - Email
   - Ville favorite

Cas d'utilisation 3 — Utiliser l'interface d'administration
-------------------------------------------------------------

1. Aller sur **http://127.0.0.1:8000/admin**
2. Se connecter avec :

   - Identifiant : ``admin``
   - Mot de passe : ``Abc1234!``

3. Gérer les données :

   - **Addresses** : ajouter, modifier, supprimer des adresses
   - **Lettings** : ajouter, modifier, supprimer des locations
   - **Profiles** : ajouter, modifier, supprimer des profils
   - **Users** : gérer les utilisateurs

Cas d'utilisation 4 — Naviguer entre les pages
------------------------------------------------

Le site dispose d'une barre de navigation avec :

- **Logo** : retour à la page d'accueil
- **Profiles** : accéder à la liste des profils
- **Lettings** : accéder à la liste des locations