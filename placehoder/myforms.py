from django import forms

class ImageForm(forms.Form):
    height=forms.IntegerField(max_value=2000,min_value=1,error_messages={"required":"不在合适范围内"})
    width=forms.IntegerField(max_value=2000,min_value=1,error_messages={"required":"不在合适范围内"})