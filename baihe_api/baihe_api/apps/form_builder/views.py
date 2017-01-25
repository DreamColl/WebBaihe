from rest_framework import viewsets
from rest_framework.decorators import detail_route

from baihe_api.permissions import IsAdminOrReadOnly
from baihe_api.common.excel import get_form_excel_response

from .models import BaiheForm
from .serializers import BaiheFormSerializers


class BaiheFormViewSet(viewsets.ModelViewSet):
    queryset = BaiheForm.objects.all()
    serializer_class = BaiheFormSerializers
    permission_classes = (IsAdminOrReadOnly, )

    @detail_route(methods=['get'])
    def export(self, request, *args, **kwargs):
        instance = self.get_object()
        response = get_form_excel_response(instance)
        return response

# class BaiheFormDataViewSet(viewsets.ModelViewSet):
#     queryset = FormData.objects.all()
#     serializer_class = BaiheFormDataSerializers
#     permission_classes = (IsOwner, IsAdminUser)

#     def perform_create(self, serializer):
#         if self.request.user.is_anonymous:
#             serializer.save(user=self.request.user)

#     def perform_destroy(self, serializer):
#         serializer.save(deleted=timezone.now())
