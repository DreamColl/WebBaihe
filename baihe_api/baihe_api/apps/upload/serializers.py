from rest_framework import serializers
from .models import ImageModel, FileModel


class FileSerializers(serializers.ModelSerializer):

    class Meta:
        model = FileModel
        fields = '__all__'


class ImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = ImageModel
        fields = '__all__'
