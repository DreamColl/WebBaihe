from rest_framework import viewsets, mixins

from .models import FileModel, ImageModel
from .serializers import FileSerializers, ImageSerializers


class FileViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializers


class ImageViewSet(mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializers
