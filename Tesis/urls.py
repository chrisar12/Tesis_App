from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^', include('SituacionSalud.urls', namespace='situacionsalud')),


    # Admin
    url('admin/', admin.site.urls),



]
