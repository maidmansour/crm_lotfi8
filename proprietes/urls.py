from django.conf import settings
from django.urls import path,  include
from django.conf.urls.static import static
from .views import list, propriete_edit, delete_image, quartiers_load, address_load




urlpatterns = \
    [
        path('', list, name='list-proprietes'),
        path('edit/', propriete_edit, name="propriete-edit"),
        path('edit/<pk>', propriete_edit, name="propriete-edit"),
        path('delete_image/<int:image_id>/', delete_image, name='delete_image'),
        path('quartiers/get', quartiers_load, name="quartier-load"),
        path('residence/address/get', address_load, name="address_load")
       
    ]
