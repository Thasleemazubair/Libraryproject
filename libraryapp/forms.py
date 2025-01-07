from django import forms
from django.contrib.auth.management.commands.changepassword import UserModel
from django.contrib.auth.models import User
from django.db import  models
from . import models


class AdminSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', ' password']

class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password']

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = models.StudentExtra
        fields = ['enrollment','branch']




