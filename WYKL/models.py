from django.db import models

# Create your models here.

# 用户数据
class User(models.Model):
    account = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=40)
    tel = models.CharField(max_length=20)


# 轮播图数据
class Wheel(models.Model):
    imgpath = models.CharField(max_length=30)
    class Meta:
        db_table = "wheel"


# 导航栏数据
class Nav(models.Model):
    imgpath = models.CharField(max_length=30)
    class Meta:
        db_table = "nav"


# 首页商品展示数据
class Goods(models.Model):
    goodsid = models.CharField(max_length=5)
    goodsimg = models.CharField(max_length=100)
    goodsname = models.CharField(max_length=256)
    price = models.IntegerField()
    descript = models.CharField(max_length=100)
    class Meta:
        db_table = "goods"