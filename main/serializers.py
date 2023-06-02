from rest_framework import serializers

from .models import *


class PostSerializer(serializers.ModelSerializer):

    # title = serializers.CharField(max_length=200)
    # description = serializers.CharField(max_length=140)
    # date_created = serializers.DateTimeField()
    # date_updated = serializers.DateTimeField()

    class Meta:

        model = PostModel

        fields = ('__all__')


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:

        model = PhotoModel

        fields = ('__all__')
