from django.urls import path
from api import views

urlpatterns = [
    path('typelist/', views.type_list,name='type-list'),
    path('typelist/add/', views.type_list_add,name='type-list-add'),
    path('typelist/edit/', views.type_list_edit,name='type-list-edit'),
    path('typelist/delete/', views.type_list_delete,name='type_list_delete'),
    path('apitest/', views.apitest,name='api-test'),

]