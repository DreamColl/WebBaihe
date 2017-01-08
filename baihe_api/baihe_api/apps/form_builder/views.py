from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from baihe_api.permissions import IsAdminOrReadOnly, IsOwner

from .models import BaiheForm, BaiheFormData
from .serializers import BaiheFormDataSerializers, BaiheFormSerializers


class BaiheFormViewSet(viewsets.ModelViewSet):
    queryset = BaiheForm.objects.all()
    serializer_class = BaiheFormSerializers
    permission_classes = (IsAdminOrReadOnly, )


class BaiheFormDataViewSet(viewsets.ModelViewSet):
    queryset = BaiheFormData.objects.all()
    serializer_class = BaiheFormDataSerializers
    permission_classes = (IsOwner, IsAdminUser)

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            serializer.save(user=self.request.user)

    def perform_destroy(self, serializer):
        serializer.save(deleted=timezone.now())
