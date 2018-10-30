from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

# 首页
from WYKL.models import User


def index(request):
    # 获取 cookie

    return render(request, "index.html")

# 详情
def detail(request):
    return render(request, "detail.html")


# 购物车
def cart(request):
    return render(request, "cart.html")


# 加密
def encryption(password):
    pass


# 注册
def register(request):
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
                return HttpResponse("账号已存在")
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
            return HttpResponse("账号应在6～18位")


# 登陆
def login(request):

    return render(request, "login.html")
    # return HttpResponse('登陆')


# 购买
def shop(request):
    return render(request, "shop.html")