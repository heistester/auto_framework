import uuid

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import JsonResponse,HttpResponse


from auth_login import models
from auth_login import myforms
from utils.vaild_img import get_vaild_code
from utils.encry_data import descrypt_passwd

def index(request):
    return render(request, "auth_login/index.html")

def login(request):
    if request.method == "POST":
        res = {"user": None, "msg": None}
        username = request.POST.get("username")
        password = request.POST.get("password")
        password = descrypt_passwd(password)
        validcode = request.POST.get("validCode")
        validcode_str = request.session.get("validcode")
        if validcode.upper() == validcode_str.upper():
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                res["user"] = request.user.username
                res["msg"] = "success"
                return JsonResponse(res)
            else:
                res["msg"] = "用户名或密码错误"
                return JsonResponse(res)
        else:
            res["msg"] = "验证码错误"
            return JsonResponse(res)
    return render(request, "auth_login/login.html")

def get_validcode_img(request):
    '''
    返回一张验证码图片
    :param request:
    :return:
    '''
    data, valid_code = get_vaild_code()
    request.session["validcode"] = valid_code
    return HttpResponse(data)

def register(request):
    if request.is_ajax():
        response = {"user": None, "msg": None}
        res_form=myforms.RegisterForm(request.POST)
        if res_form.is_valid():
            response["user"]=username = res_form.cleaned_data.get("username")
            password=res_form.cleaned_data.get("password")
            email = res_form.cleaned_data.get("email")
            avatar=request.FILES.get("avatar")
            avatar.name="img"+uuid.uuid4().hex+".jpg"
            kwargs={}
            if avatar:
                kwargs["avatar"]=avatar
            models.UserInfo.objects.create_user(username=username,password=password,email=email,**kwargs)
        else:
            response["msg"]=res_form.errors
        return JsonResponse(response)
    forms=myforms.RegisterForm()
    return render(request, "auth_login/register.html", {"forms":forms})

@login_required
def logout(request):
    auth.logout(request)
    return render(request,'auth_login/index.html')
















def page_not_found(request,expection):
    return render(request, 'auth_login/404.html')
handler404='auth_login.views.page_not_found'