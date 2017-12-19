from django.conf.urls import url

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/$', views.authentication, name="authentication"),
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name="logout", ),
    url(r'^reportes/$', views.reportes, name='reportes'),
    url(r'^report/$', views.report, name='report'),



    # url(r'^$', views.login),
    # url(r'^$', views.index, name='index'),
    # url(r'^index/$', views.index, name='index'),
    # url(r'^factorescondicionantes/$', views.factorescondicionantes, name='factorescondicionantes'),

]
