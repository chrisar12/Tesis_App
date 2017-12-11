from django.conf.urls import include, url
from django.contrib.auth.views import login
from . import views


urlpatterns = [
   # url(r'^$', login, {'template_name':'login.html'}, name='login'),
    #url(r'^$', views.login),
    url(r'^$', views.index, name='index'),
   # url(r'^index/$', views.index, name='index'),
    url(r'^factorescondicionantes/$', views.factorescondicionantes, name='factorescondicionantes'),


]