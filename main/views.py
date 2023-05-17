from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.


@login_required(login_url='/accounts/login')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login')
def create_post(request):
    if request.method == 'POST':
        form = Post(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = Post()
    return render(request, 'create-post.html', {'form': form})


@login_required(login_url='/accounts/login')
def create_photo(request):
    if request.method == 'POST':
        form = Photo(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = Photo()
    return render(request, 'create-photo.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign-up.html', {'form': form})
