from django.urls import path
from api import views

urlpatterns = [
    path('api_typelist/', views.type_list,name='type-list'),
    path('api_typelist/add/', views.type_list_add,name='type-list-add'),
    path('api_typelist/edit/', views.type_list_edit,name='type-list-edit'),
    path('api_typelist/delete/', views.type_list_delete,name='type_list_delete'),
    path('apitest/', views.api_test,name='api-test'),
    path('apisave/', views.api_save,name='api-save'),
    path('delete_api/', views.delete_api,name='delete-api'),
    path('apitest_edit/', views.api_test_edit,name='api-test-edit'),
]