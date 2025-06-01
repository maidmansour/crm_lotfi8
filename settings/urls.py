from django.conf import settings
from django.urls import path,  include
from django.conf.urls.static import static
from .views import list, secteur_edit, type_bien_edit, sous_type_bien_edit, agent_edit, intermidiaire_edit, residence_edit, quartier_edit


urlpatterns = \
    [
        path('', list, name='list-settings'),
        path('secteur/edit/', secteur_edit, name="secteur-edit"),
        path('secteur/edit/<pk>', secteur_edit, name="secteur-edit"),
        path('type-bien/edit/', type_bien_edit, name="type_bien-edit"),
        path('type-bien/edit/<pk>', type_bien_edit, name="type_bien-edit"),
        path('sous-type-bien/edit/', sous_type_bien_edit, name="sous_type_bien-edit"),
        path('sous-type-bien/edit/<pk>', sous_type_bien_edit, name="sous_type_bien-edit"),
        path('agent/edit/', agent_edit, name="agent-edit"),
        path('agent/edit/<pk>', agent_edit, name="agent-edit"),
        path('intermidiaire/edit/', intermidiaire_edit, name="intermidiaire-edit"),
        path('intermidiaire/edit/<pk>', intermidiaire_edit, name="intermidiaire-edit"),
        path('residence/edit/', residence_edit, name="residence-edit"),
        path('residence/edit/<pk>', residence_edit, name="residence-edit"),
        path('quartier/edit/', quartier_edit, name="quartier-edit"),
        path('quartier/edit/<pk>', quartier_edit, name="quartier-edit"),
    ]

