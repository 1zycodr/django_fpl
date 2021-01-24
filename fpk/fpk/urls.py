from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# from web.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/', )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)