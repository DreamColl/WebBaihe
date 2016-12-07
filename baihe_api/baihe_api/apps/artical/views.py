from rest_framework import viewsets

from baihe_api.permissions import IsAdminOrReadOnly

from .models import Artical
from .serializers import ArticalSerializers


class ArticalViewSet(viewsets.ModelViewSet):
    queryset = Artical.objects.all()
    serializer_class = ArticalSerializers
    permission_classes = (IsAdminOrReadOnly, )

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)
