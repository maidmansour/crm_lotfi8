from django.conf import settings
from django.urls import path,  include
from django.conf.urls.static import static
from .views import list, proprietaire_edit, list_proprietes




urlpatterns = \
    [
        path('', list, name='list-proprietaires'),
        path('edit/', proprietaire_edit, name="proprietaire-edit"),
        path('edit/<pk>', proprietaire_edit, name="proprietaire-edit"),
        path('proprietes/<pk>', list_proprietes, name="proprietaire-proprietes"),
    ]
