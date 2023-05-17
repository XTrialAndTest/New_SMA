
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/sign-up', views.sign_up),
    path('create-post', views.create_post, name='create-post'),
    path('create-photo', views.create_photo, name='create-photo'),

]
