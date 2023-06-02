

from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# from cloudinary.forms import cl_init_js_callbacks


from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from .models import *

from .serializers import *


# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):

    return render(request, 'index.html')


@login_required(login_url='/accounts/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'create-post.html', {'form': form})


@login_required(login_url='/accounts/login')
def create_photo(request):

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES,)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = PhotoForm()

    return render(request, 'create-photo.html', {'form': form})


def sign_up(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign-up.html', {'form': form})


def user(request):
    return render(request, 'user/login.html')


class PostView(APIView):

    def get(self, request, *args, **kwargs):

        result = PostModel.objects.all()

        serializers = PostSerializer(result, many=True)

        return Response({'status': 'success', "post": serializers.data}, status=200)

    def post(self, request):

        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        else:

            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):

        result = PostModel.objects.get(id=id)

        serializer = PostSerializer(result, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response({"status": "success", "data": serializer.data})

        else:

            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):

        result = get_object_or_404(Post, id=id)

        result.delete()

        return Response({"status": "success", "data": "Record Deleted"})


class PhotoView(APIView):

    def get(self, request, *args, **kwargs):

        result = PhotoModel.objects.all()

        serializers = PhotoSerializer(result, many=True)

        return Response({'status': 'success', "photo": serializers.data}, status=200)

    def post(self, request):

        serializer = PhotoSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        else:

            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):

        result = PhotoModel.objects.get(id=id)

        serializer = PhotoSerializer(result, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response({"status": "success", "data": serializer.data})

        else:

            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):

        result = get_object_or_404(Photo, id=id)

        result.delete()

        return Response({"status": "success", "data": "Record Deleted"})
