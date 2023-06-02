from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser

from cloudinary.models import CloudinaryField


class PostModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=140)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return fself.title


class PhotoModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    photo = CloudinaryField('Photo')
    caption = models.CharField(max_length=30, default='')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
