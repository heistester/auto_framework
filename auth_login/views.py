from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    return render(request,'index.html')

def page_not_found(request,expection):
    return render(request,'404.html')