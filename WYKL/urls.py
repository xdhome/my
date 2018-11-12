from django.conf.urls import url

from WYKL import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^index/$', views.index, name="index"),  # 首页

    url(r'^detail/$', views.detail, name="detail"),  # 商品展示

    url(r'^cart/$', views.cart, name="cart"),  # 购物车

    url(r'^login/$', views.login, name="login"),  # 登陆

    url(r'^register/$', views.register, name="register"),  # 注册

    url(r'^shop/(\d+)/$', views.shop, name='shop'),  # 商品详情展示

    url(r'^logout/$', views.logout, name='logout'),  # 退出

    url(r"^verify/$", views.verify, name='verify'),  # 注册账号验证

    url(r'^addcart/$', views.addcart, name='addcart'),  # 加入购物车

    url(r'^subtract/(\d+)$', views.subtract, name='subtract'),  # 购物车减操作

]