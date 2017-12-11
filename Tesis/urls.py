from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^', include('SituacionSalud.urls', namespace='situacionsalud')),


    # Admin
    url('admin/', admin.site.urls),



]
