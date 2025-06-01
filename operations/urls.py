from django.conf import settings
from django.urls import path,  include
from django.conf.urls.static import static
from .views import list, operation_edit




urlpatterns = \
    [
        path('', list, name='list-operations'),
        path('edit/', operation_edit, name="operation-edit"),
        path('edit/<pk>', operation_edit, name="operation-edit"),
    ]
