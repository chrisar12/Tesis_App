from django.conf.urls import url

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/$', views.authentication, name="authentication"),
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name="logout", ),
    url(r'^report/$', views.report, name='report'),
    url(r'^reportnivelsalud/$', views.reportnivelsalud, name='reportnivelsalud'),
    url(r'^reportfactorescondicionantes/$', views.reportfactorescondicionantes, name='reportfactorescondicionantes'),
    url(r'^NSr1/$', views.NSr1, name='NSr1'),
    url(r'^ingresar/$', views.ingresardatos, name='ingresar'),

    # url(r'^$', views.login),
    # url(r'^$', views.index, name='index'),
    # url(r'^index/$', views.index, name='index'),
    # url(r'^factorescondicionantes/$', views.factorescondicionantes, name='factorescondicionantes'),

]
