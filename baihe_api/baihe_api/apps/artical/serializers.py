from rest_framework import serializers
from .models import Artical


class ArticalSerializers(serializers.ModelSerializer):

    class Meta:
        model = Artical
        fields = '__all__'
        read_only_fields = ('author', 'read_count', 'share_count')
