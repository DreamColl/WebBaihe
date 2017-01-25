from django.utils import timezone
from rest_framework import serializers

from .models import BaiheForm, FormData

FIELD_TYPE_CHOICES = ['text', 'phone', 'email', 'textarea',
                      'radio', 'select', 'checkbox', 'file', 'image']
VALIDATION_CHOICES = ['max_length', 'min_length']


class FormFieldSerializers(serializers.Serializer):
    field_type = serializers.ChoiceField(FIELD_TYPE_CHOICES)
    label_name = serializers.CharField(max_length=100)
    placeholder = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True
    )
    choices = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True
    )
    default = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True
    )
    required = serializers.BooleanField(initial=True, required=False)
    validation = serializers.ChoiceField(
        VALIDATION_CHOICES,
        required=False,
        allow_blank=True
    )
    addable = serializers.BooleanField(required=False)

    def validate(self, data):
        if data['field_type'] in ['radio', 'select', 'checkbox'] and not data.get('choices'):
            raise serializers.ValidationError(
                'choices not provided for `%s` field' % data['field_type']
            )
        return data


class BaiheFormSerializers(serializers.HyperlinkedModelSerializer):
    # fields = FormFieldSerializers(many=True)

    class Meta:
        model = BaiheForm
        fields = '__all__'

    # def create(self, validated_data):
    #     structure = validated_data.pop('structure')
    #     form = BaiheForm(**validated_data)
    #     form.structure = structure
    #     form.save()

    #     return form

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
        model = FormData
        fields = '__all__'
        read_only_fields = ('user',)
