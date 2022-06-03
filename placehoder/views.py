import hashlib

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest
from rest_framework.views import APIView

from django.views.decorators.http import etag

from placehoder import myforms

# Create your views here.
from utils.vaild_img import get_png

def png_generate(request,width,height): #浏览器缓存机制
    content="png:{}x{}".format(width,height)
    return hashlib.sha1(content.encode('utf8')).hexdigest()

@etag(png_generate)
def placehoder(request,width,height):
    form=myforms.ImageForm({"width":width,"height":height})
    if form.is_valid():
        width=form.cleaned_data.get("width")
        height=form.cleaned_data.get("height")
        img=get_png(width,height)
        return HttpResponse(img,content_type="image/png")
    return HttpResponseBadRequest("不正确的请求")

