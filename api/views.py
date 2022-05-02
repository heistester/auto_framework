# Create your views here.
import json

import requests
from django.http import JsonResponse
from django.shortcuts import render,redirect

from django.urls import reverse

from api.models import Type


# Create your views here.
def type_list(request):
    type_all=Type.objects.all().order_by('pk')
    return render(request,"type_list.html",{"type_all":type_all})


def type_list_add(request):
    error = ""
    if request.method=="POST":
        type_name=request.POST.get("typename")
        type_name=type_name.strip().upper()
        if not type_name:
            error="类型名不能为空"
        elif Type.objects.filter(name=type_name):
            error="类型已存在"
        else:
            Type.objects.create(name=type_name)
            return redirect(reverse('type-list'))
    return render(request,"type_edit.html",{"error":error})


def type_list_edit(request):
    error = ""
    tid = request.GET.get("id")
    type_obj = Type.objects.filter(pk=tid).first()
    if request.method == "POST":
        type_name = request.POST.get("typename")
        type_name = type_name.strip().upper()
        if not type_name:
            error = "类型名不能为空"
        elif Type.objects.exclude(pk=tid).filter(name=type_name):
            error = "类型已存在"
        else:
            Type.objects.filter(pk=tid).update(name=type_name)
            return redirect(reverse('type-list'))
    return render(request, "type_edit.html", {"error": error, "typeobj": type_obj})


def type_list_delete(request):
    if request.method=="POST":
        res={"status":"fail","msg":None}
        pk=request.POST.get("tid")
        type_obj=Type.objects.filter(pk=pk).delete()
        if type_obj:
            res["status"] = "success"
            res["msg"] = "删除成功"
        else:
            res["msg"]="删除失败"
        return JsonResponse(res)


def send_request(name,url,headers,params):
    if name=="GET":
        res=requests.get(url=url,headers=headers,params=params)
    elif name=="POST":
        res=requests.post(url=url,headers=headers,params=params)
    else:
        return 'fail'
    return res.text,res.headers,res.status_code

def apitest(request):
    type_all = Type.objects.all().order_by('pk')
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