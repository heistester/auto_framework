from django.db import models

# Create your models here.

class Type(models.Model):
    name=models.CharField(max_length=32,unique=True)
    def __str__(self):
        return self.name

class ApiTest(models.Model):
    name=models.CharField(max_length=32,unique=True)
    type=models.ForeignKey("Type",on_delete=models.PROTECT)
    url = models.CharField(max_length=200)
    headers = models.CharField(max_length=2000)
    parameters = models.CharField(max_length=2000)