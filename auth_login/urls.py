from django.contrib import admin
from django.urls import path

from auth_login import views

urlpatterns = [
    path('',views.index),

]