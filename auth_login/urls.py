from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from AUTO import settings
from auth_login import views

urlpatterns = [
    path('',views.index,name='index'),
    re_path('media/(?P<path>.*)',serve,{"document_root":settings.MEDIA_ROOT}),
    path('auth_login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('auth_logout/',views.logout,name='logout'),
    path('auth_register/',views.register,name='register'),
    path('auth_get_validcode_img',views.get_validcode_img,name='validcode_img')
]