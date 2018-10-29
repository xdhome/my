from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 首页
def index(request):

    # return render(request, "index.html")
    return HttpResponse('首页')

# 详情
def detail(request):
    return None


# 购物车
def cart(request):
    return None


# 登陆
def login(request):
    # return render(request, "login.html")
    return HttpResponse('登陆')

# 注册
def register(request):
    return None


# 购买
def shop(request):
    return None