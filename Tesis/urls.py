from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^SituacionSalud/', include('SituacionSalud.urls', namespace='SituacionSalud')),
    url(r'^$', login, {'template_name': 'situacionsalud/login.html'}, name='login'),

    # Admin
    url('admin/', admin.site.urls),



]
