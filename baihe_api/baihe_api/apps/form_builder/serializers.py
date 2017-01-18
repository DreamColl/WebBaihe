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

    def validate_structure(self, value):
        '''
        @ field_type
        @ label_name
        @ placeholder
        @ choices
        @ default
        @ required
        @ validation
        '''

        if not isinstance(value, dict):
            raise serializers.ValidationError(
                'structure must be a dict not a `%s`' % type(value)
            )
        i = 0
        for field_order, field in value:
            if field_order != i:
                raise serializers.ValidationError(
                    'field order not consistent at `%d`' % i
                )
            i += 1

            key_has_field_type = False
            key_has_label_name = False

            for key, v in field:
                if key == 'field_type' and v:
                    key_has_field_type = True
                elif key == 'label_name' and v:
                    key_has_label_name = True

            if not (key_has_field_type and key_has_label_name):
                raise serializers.ValidationError(
                    'field_type and label_name required'
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
