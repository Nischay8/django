from django.db import models

# Create your models here.
class login(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=70)


class signup(models.Model):
    username=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    password=models.CharField(max_length=70)
    confirm_password=models.CharField(max_length=70)
    Address=models.CharField(max_length=70)
    