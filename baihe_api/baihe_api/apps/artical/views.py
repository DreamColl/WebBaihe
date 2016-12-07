from rest_framework import viewsets

from .models import Artical
from .serializers import ArticalSerializers


class ArticalViewSet(viewsets.ModelViewSet):
    queryset = Artical.objects.all()
    serializer_class = ArticalSerializers

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)
