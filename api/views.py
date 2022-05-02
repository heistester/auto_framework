# Create your views here.
import json

import requests
from django.http import JsonResponse
from django.shortcuts import render,redirect

from django.urls import reverse

from api import models


# Create your views here.
def type_list(request):
    type_all=models.Type.objects.all().order_by('pk')
    return render(request,"type_list.html",{"type_all":type_all})


def type_list_add(request):
    error = ""
    if request.method=="POST":
        type_name=request.POST.get("typename")
        type_name=type_name.strip().upper()
        if not type_name:
            error="类型名不能为空"
        elif models.Type.objects.filter(name=type_name):
            error="类型已存在"
        else:
            models.Type.objects.create(name=type_name)
            return redirect(reverse('type-list'))
    return render(request,"type_edit.html",{"error":error})


def type_list_edit(request):
    error = ""
    tid = request.GET.get("id")
    type_obj = models.Type.objects.filter(pk=tid).first()
    if request.method == "POST":
        type_name = request.POST.get("typename")
        type_name = type_name.strip().upper()
        if not type_name:
            error = "类型名不能为空"
        elif models.Type.objects.exclude(pk=tid).filter(name=type_name):
            error = "类型已存在"
        else:
            models.Type.objects.filter(pk=tid).update(name=type_name)
            return redirect(reverse('type-list'))
    return render(request, "type_edit.html", {"error": error, "typeobj": type_obj})


def type_list_delete(request):
    if request.method=="POST":
        res={"status":"fail","msg":None}
        pk=request.POST.get("tid")
        type_obj=models.Type.objects.filter(pk=pk).delete()
        if type_obj:
            res["status"] = "success"
            res["msg"] = "删除成功"
        else:
            res["msg"]="删除失败"
        return JsonResponse(res)

def delete_api(request):
    if request.method == "POST":
        res = {"status": "fail", "msg": None}
        pk = request.POST.get("aid")
        type_obj = models.ApiTest.objects.filter(pk=pk).delete()
        if type_obj:
            res["status"] = "success"
            res["msg"] = "删除成功"
        else:
            res["msg"] = "删除失败"
        return JsonResponse(res)

def send_request(name,url,headers,params):
    if name=="GET":
        res=requests.get(url=url,headers=headers,params=params)
    elif name=="POST":
        res=requests.post(url=url,headers=headers,params=params)
    else:
        return 'fail'
    return res.text,res.headers,res.status_code

def api_test(request):
    type_all = models.Type.objects.all().order_by('pk')
    if request.method=="POST":
        resp = {"body": None, "headers": None, "status": None}
        type_id=request.POST.get("typeId")
        req_url=request.POST.get("reqUrl")
        headers=request.POST.get("headers")
        params=request.POST.get("parameters")
        name=type_all.get(pk=type_id).name
        res=send_request(name,req_url,headers,params)
        if res=='fail':
            return JsonResponse(res)
        res_body, res_headers, res_status=res
        resp["body"]=res_body
        resp["headers"]=dict(res_headers)
        resp["status"]=res_status
        return JsonResponse(dict(resp))
    return render(request, "api_test.html", {"type_all": type_all})


def api_save(request):
    api_tests = models.ApiTest.objects.all().order_by("pk")
    if request.method=="POST":
        req={"status":"fail","msg":"添加失败"}
        pk=request.POST.get("typeId")
        req_url=request.POST.get("reqUrl")
        headers=request.POST.get("headers")
        params=request.POST.get("parameters")
        name=request.POST.get("name")
        api_name=models.ApiTest.objects.filter(name=name)
        if api_name:
            req["status"]="name_repeated"
            req["msg"]="名称重复"
            return JsonResponse(req)
        if models.ApiTest.objects.create(url=req_url,headers=headers,parameters=params,name=name,type_id=pk):
            req["status"] = "success"
            req["msg"] = "添加成功"
        return JsonResponse(req)
    return render(request,'api_save.html',locals())


def api_test_edit(request):
    pk=request.GET.get("id")
    api_test=models.ApiTest.objects.filter(pk=pk).first()
    type_all=models.Type.objects.all().order_by("pk")
    if request.method=="POST":
        req = {"status": "fail", "msg": "更新失败"}
        type_id = request.POST.get("typeId")
        req_url = request.POST.get("reqUrl")
        headers = request.POST.get("headers")
        params = request.POST.get("parameters")
        name = request.POST.get("name")

        if models.ApiTest.objects.filter(pk=pk).update(url=req_url,headers=headers,parameters=params,name=name,type_id=type_id):
            req["status"]="success"
            req["msg"]="更新成功"
        return JsonResponse(req)
    return render(request,"api_test_edit.html",locals())