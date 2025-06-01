from django.conf import settings
from django.urls import path,  include
from django.conf.urls.static import static
from .views import list, client_edit




urlpatterns = \
    [
        path('', list, name='list-clients'),
        path('edit/', client_edit, name="client-edit"),
        path('edit/<pk>', client_edit, name="client-edit"),
    ]
