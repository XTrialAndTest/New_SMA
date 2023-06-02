from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'description']


class PhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ['title', 'photo', 'caption']
