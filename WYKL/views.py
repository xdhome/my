import hashlib
import uuid
from audioop import reverse

from django.http import HttpResponse, JsonResponse
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
    # 导航栏数据
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
    # 获取 cookie
    account = request.COOKIES.get("account")
    if account:
        # 获取用户
        user = User.objects.get(account=account)
        userid = user.id
        # 获取当前用户的购物车数据
        carts = Cart.objects.filter(user_id=userid)
        data = {
            "account": account,
            "carts": carts,
        }
        return render(request, "cart.html",data)
    else:
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
        print('1',tel,'2',account,'3',password)
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
                # 验证通过，存入数据
                user = User()
                user.account = account
                user.password = encryption(password)
                user.tel = tel
                user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
                user.save()
                # 重定向到首页
                response = redirect("wykl:index")
                # 状态保持
                # request.sessino["tokon"] = user.token
                response.set_cookie("account",account)
                return response


                # return redirect("wykl:index")
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
        password = encryption(request.POST.get("password"))
        user = User.objects.filter(account=account).filter(password=password)
        if user.exists():
            response = redirect("wykl:index")
            # 设置 cookie
            response.set_cookie("account", account)
            return response
        else:
            log_data["login_error"] = "用户名或密码错误"
            return render(request,"login.html", log_data)


# 退出
def logout(request):
    response = redirect("wykl:index")
    response.delete_cookie("account")
    return response


# 详情
def shop(request, goodsid):
    good = Goods.objects.get(goodsid=goodsid)
    # print(good.goodsid,"id")
    return render(request, "shop.html", context={'good': good})


# 注册账号验证
def verify(request):
    # account = request.GET.get("_account")
    # print(account,1111111111)
    return None


def addcart(request):
    print("加++++")

    data = {
        "msg": "",
        "status": 1
    }
    account = request.COOKIES.get("account")
    # 判断登陆状态
    if account:
        print("有account")
        goodsid = request.GET.get("goodsid")
        goods = Goods.objects.get(goodsid=goodsid)
        user = User.objects.get(account=account)
        number = request.GET.get("number")
        # print(goods.goodsid, number,user.id)
        carts = Cart.objects.filter(goods=goods.id).filter(user=user.id)
        print(type(carts), carts)
        # print(type(carts.number), carts.number,carts)
        # 判断本用户是否曾添加此商品
        if carts.exists():
            print("有记录")
            cart = carts[0]
            print(type(cart.number),cart.number)
            cart.number += int(number)
            cart.save()
            data["msg"] = "添加成功"
            data["status"] = 1
            return JsonResponse(data)
        else:
            print("无记录 ")
            cart = Cart()
            cart.goods = goods
            cart.number = number
            cart.user = user

            cart.save()
            data["msg"] = "添加成功"
            data["status"] = 1
            return JsonResponse(data)
    else:
        data["msg"] = "添加失败"
        data["status"] = -1
        return JsonResponse(data)


def subtract(request, cartid):
    print("减----")
    print(cartid)
    return JsonResponse()