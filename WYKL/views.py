import hashlib
from audioop import reverse

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from WYKL.models import *

# 首页
def index(request):
    # 获取轮播图数据
    wheels = Wheel.objects.all()
    # print(len(wheels))
    # for wheel in wheels:
    #     print(type(wheel.imgpath), wheel.imgpath)
    navs = Nav.objects.all()
    # print(111111)
    # if request.method == "GET":
    #     print(2222222)
    #     return render(request, "index.html")
    # elif request.method == "POST":
    #     print(333333)
    goods = Goods.objects.all()
    # 获取 cookie
    account = request.COOKIES.get("account")
    data = {
        'account': account,
        'wheels': wheels,
        'navs': navs,
        'goods': goods
    }
    return render(request, "index.html", context=data)

# 详情
def detail(request):

    return render(request, "detail.html")


# 购物车
def cart(request):

    return render(request, "cart.html")


# 加密
def encryption(password):
    m = hashlib.md5()
    m.update(password.encode())
    return m.hexdigest()


# 注册
def register(request):
    reg_data = {
        "register_error": ""
    }
    if request.method == "GET": # 获取注册页面
        # return HttpResponse("11111")
        return render(request, "register.html")
    elif request.method == "POST": # 进行注册操作
        # return HttpResponse("222222")
        # 获取表单数据
        account = request.POST.get("account")
        password = request.POST.get("password")
        tel = request.POST.get("tel")
        # 验证账号
        if 5<len(account)<19:
            name_list =[]
            users = User.objects.all()
            for user in users:
                name_list.append(user.account)
            if account in name_list:
                reg_data["register_error"] = "账号已存在"
                return render(request, "register.html", reg_data)
            else:
                # 验证通过，存入数据库
                user = User()
                user.account = account
                user.password = password
                user.tel = tel
                user.save()
                # 重定向到首页
                response = redirect("wykl:index")
                # 设置 cookie
                response.set_cookie("account",account)
                return response
                # return render(request, "index.html")
        else:
            reg_data["register_error"] = "账号已存在"
            return render(request, "login.html", reg_data)


# 登陆
def login(request):
    log_data= {
        "login_error": ""
    }
    if request.method == "GET":
        print("GET")
        return render(request, "login.html")
    elif request.method == "POST":
        print("POST")
        account = request.POST.get("account")
        password = request.POST.get("password")
        user = User.objects.filter(account=account).filter(password=password)
        if user.exists():
            response = redirect("wykl:index")
            # 设置 cookie
            response.set_cookie("account", account)
            return response
        else:
            log_data["login_error"] = "用户名或密码错误"
            return render(request,"login.html", log_data)


def logout(request):
    response = redirect("wykl:index")
    response.delete_cookie("account")
    return response


# 购买
def shop(request, goodsid):
    good = Goods.objects.get(goodsid=goodsid)
    return render(request, "shop.html", context={'good': good})