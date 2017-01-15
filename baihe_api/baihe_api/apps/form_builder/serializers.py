from django.utils import timezone
from rest_framework import serializers
from .models import BaiheForm, BaiheFormData


class BaiheFormSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BaiheForm
        fields = '__all__'

    def validate_start_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                'start_time must be after current time'
            )
        return value

    def validate_end_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                'end_time must be after current time'
            )
        return value

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError(
                'start_time must be before end_time'
            )
        return data


class BaiheFormDataSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BaiheFormData
        fields = '__all__'
        read_only_fields = ('user',)
