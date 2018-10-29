from django.conf.urls import url

from WYKL import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index, name="index"),
    url(r'^detail/$', views.detail, name="detail"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^login/$', views.login, name="login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^shop/$', views.shop, name='shop'),
]