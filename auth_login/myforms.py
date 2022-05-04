from django.contrib.auth.forms import forms
from django.core.exceptions import ValidationError

from auth_login.models import UserInfo
from utils.encry_data import descrypt_passwd

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=32,label="用户名",
                             error_messages={"required":"用户名不能为空"},
                             widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=64,label="密码",
                             error_messages={"required":"密码不能为空"},
                             widget=forms.PasswordInput(attrs={"class":"form-control"}))
    re_password=forms.CharField(max_length=64,label="确认密码",
                             error_messages={"required":"确认密码不能为空"},
                             widget=forms.PasswordInput(attrs={"class":"form-control"}))

    email=forms.EmailField(label="邮箱地址",
                           error_messages={"required":"邮箱不能为空"},
                           widget=forms.EmailInput(attrs={"class":"form-control"}))

    def clean_username(self):
        username=self.cleaned_data.get("username")
        user=UserInfo.objects.filter(username=username).first()
        if user:
            raise ValidationError("用户名已存在")
        return username

    def clean(self):
        password =self.cleaned_data.get("password")
        re_password =self.cleaned_data.get("re_password")
        if password and re_password:
            password = descrypt_passwd(password)
            re_password = descrypt_passwd(re_password)
            if re_password!=password:
                raise ValidationError("两次密码不一致！")
            self.cleaned_data["password"]=password
        return self.cleaned_data
