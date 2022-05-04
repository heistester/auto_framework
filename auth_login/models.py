from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UserInfo(AbstractUser):
    create_time=models.DateTimeField(auto_now_add=True)