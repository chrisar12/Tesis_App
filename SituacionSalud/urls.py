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
    url(r'^NSr2/$', views.NSr2, name='NSr2'),
    url(r'^NSr3/$', views.NSr3, name='NSr3'),
    url(r'^NSr4/$', views.NSr4, name='NSr4'),
    url(r'^NSr5/$', views.NSr5, name='NSr5'),
    url(r'^NSr6/$', views.NSr6, name='NSr6'),
    url(r'^NSr7/$', views.NSr7, name='NSr7'),
    url(r'^NSr8/$', views.NSr8, name='NSr8'),
    url(r'^ingresar/$', views.ingresardatos, name='ingresar'),

    # url(r'^$', views.login),
    # url(r'^$', views.index, name='index'),
    # url(r'^index/$', views.index, name='index'),
    # url(r'^factorescondicionantes/$', views.factorescondicionantes, name='factorescondicionantes'),

]
