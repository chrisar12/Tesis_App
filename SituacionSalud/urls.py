from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.login),
    #url(r'^$', views.login),
    # url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^factorescondicionantes/$', views.factorescondicionantes, name='factorescondicionantes'),


]