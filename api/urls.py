from django.urls import path
from api import views

urlpatterns = [
    path('',views.index),
    path('typelist/', views.type_list,name='type-list'),
    path('typelist/add/', views.type_list_add,name='type-list-add'),
    path('typelist/edit/', views.type_list_edit,name='type-list-edit'),
    path('typelist/delete/', views.type_list_delete,name='type_list_delete'),
    path('apitest/', views.api_test,name='api-test'),
    path('apisave/', views.api_save,name='api-save'),
    path('delete_api/', views.delete_api,name='delete-api'),
    path('apitest_edit/', views.api_test_edit,name='api-test-edit'),

]