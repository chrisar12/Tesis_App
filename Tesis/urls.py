from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('SituacionSalud.urls', namespace='situacionsalud'), name='situacionsalud'),
    url(r'^admin/', admin.site.urls),

]
