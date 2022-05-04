from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UserInfo(AbstractUser):
    create_time=models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
    avatar=models.FileField(upload_to="avatars/",default="avatars/default.png",verbose_name="个人头像")