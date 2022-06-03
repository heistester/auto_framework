from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class ImgMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        print("img中间件request")

    def process_response(self,request,response):
        print("img中间件response")
        return response