from django.urls import path,re_path
from placehoder import views

urlpatterns = [
    re_path(r'image/(?P<width>\d+)X(?P<height>\d+)$',views.placehoder,name='placehoder'),
]