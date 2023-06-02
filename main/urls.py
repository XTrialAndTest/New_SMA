
from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/sign-up', views.sign_up, name='sign-up'),
    path('create-post', views.create_post, name='create-post'),
    path('create-photo', views.create_photo, name='create-photo'),
    path('user', views.user, name='user'),
    path('post/', PostView.as_view()),
    path('post/<int:id>/', PostView.as_view()),
    path('photo/', PhotoView.as_view()),
    path('photo/<int:id>/', PhotoView.as_view()),

]
