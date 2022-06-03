
from django.urls import path, re_path

from webui import views

urlpatterns = [
   path('report/',views.report,name='report')
]