from django.conf import settings
from django.urls import path,  include
from django.conf.urls.static import static
from wkhtmltopdf.views import PDFTemplateView
from django.contrib import admin

from django.views.generic import TemplateView






# admin doc and panel
urlpatterns = [
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls'))
]


urlpatterns += \
    [

        path('', include("authentication.urls")),
        path("proprietaires/", include("proprietaires.urls")),
        path("clients/", include("clients.urls")),
        path("proprietes/", include("proprietes.urls")),
        path("operations/", include("operations.urls")),
        path("settings/", include("settings.urls")),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)