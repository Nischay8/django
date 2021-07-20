from django import forms
from django.db import models
from django.forms import fields
from .models import login,signup

class login_regis(forms.ModelForm):
    class Meta:
        model=login
        fields='__all__'


class signup_form(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'
        