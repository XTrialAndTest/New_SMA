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
        fields = ['firstname', 'lastname', 'username',
                  'email', 'password1', 'password2',]


class Post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']


class Photo(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'photo', 'caption']
