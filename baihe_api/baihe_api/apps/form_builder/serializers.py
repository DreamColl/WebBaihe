from rest_framework import serializers
from .models import BaiheForm, BaiheFormData


class BaiheFormSerializers(serializers.ModelSerializer):

    class Meta:
        model = BaiheForm
        fields = '__all__'


class BaiheFormDataSerializers(serializers.ModelSerializer):

    class Meta:
        model = BaiheFormData
        fields = '__all__'
        read_only_fields = ('user',)
