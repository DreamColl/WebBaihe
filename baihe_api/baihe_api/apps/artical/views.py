from django.db.models import F
from rest_framework import viewsets
from rest_framework.response import Response

from baihe_api.permissions import IsAdminOrReadOnly

from .models import Artical
from .serializers import ArticalSerializers


class ArticalViewSet(viewsets.ModelViewSet):
    queryset = Artical.objects.all()
    serializer_class = ArticalSerializers
    permission_classes = (IsAdminOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.read_count = F('read_count') + 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
