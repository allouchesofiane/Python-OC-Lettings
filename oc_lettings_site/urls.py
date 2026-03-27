"""Module contenant les URLs principales de l'application oc_lettings_site."""
from django.contrib import admin
from django.urls import path, include
from . import views

def trigger_error(request):
    """Vue pour déclencher une erreur 500."""
    division_by_zero = 1 / 0
    
urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]

handler404 = 'oc_lettings_site.views.page_not_found'
handler500 = 'oc_lettings_site.views.server_error'
