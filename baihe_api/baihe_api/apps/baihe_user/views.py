from rest_framework import viewsets

from .models import BaiheUser
from .serializers import UserSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = BaiheUser.objects.all()
    serializer_class = UserSerializers
