# Generated by Django 2.2.27 on 2022-05-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]