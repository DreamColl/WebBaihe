from rest_framework import viewsets

from baihe_api.permissions import IsAdminOrReadOnly

from .models import BaiheUser
from .serializers import UserSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = BaiheUser.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsAdminOrReadOnly, )
