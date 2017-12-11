from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    url(r'', include('SituacionSalud.urls')),
    # Admin
    url('admin/', admin.site.urls),



]
