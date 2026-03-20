Interfaces de programmation
============================

Cette section décrit les URLs et vues disponibles dans l'application.

Application principale
-----------------------

.. list-table::
   :header-rows: 1

   * - URL
     - Nom
     - Vue
     - Description
   * - ``/``
     - ``index``
     - ``oc_lettings_site.views.index``
     - Page d'accueil du site
   * - ``/admin/``
     - ``admin``
     - Interface d'administration Django
     - Gestion des données

Application lettings
---------------------

.. list-table::
   :header-rows: 1

   * - URL
     - Nom
     - Vue
     - Description
   * - ``/lettings/``
     - ``lettings:index``
     - ``lettings.views.index``
     - Liste de toutes les locations
   * - ``/lettings/<id>/``
     - ``lettings:letting``
     - ``lettings.views.letting``
     - Détail d'une location

Application profiles
---------------------

.. list-table::
   :header-rows: 1

   * - URL
     - Nom
     - Vue
     - Description
   * - ``/profiles/``
     - ``profiles:index``
     - ``profiles.views.index``
     - Liste de tous les profils
   * - ``/profiles/<username>/``
     - ``profiles:profile``
     - ``profiles.views.profile``
     - Détail d'un profil

Gestion des erreurs
--------------------

.. list-table::
   :header-rows: 1

   * - Erreur
     - Vue
     - Description
   * - ``404``
     - ``oc_lettings_site.views.page_not_found``
     - Page non trouvée
   * - ``500``
     - ``oc_lettings_site.views.server_error``
     - Erreur interne du serveur