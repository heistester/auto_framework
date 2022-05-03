from django.contrib import admin
from api import models
# Register your models here.

admin.site.register(models.Type)
admin.site.register(models.ApiTest)