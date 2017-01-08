from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import BaiheUser
from .serializers import UserSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = BaiheUser.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsAdminUser, )
