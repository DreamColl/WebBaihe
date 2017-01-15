from rest_framework import serializers
from .models import Artical


class ArticalSerializers(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='nickname'
    )
    author_detail = serializers.HyperlinkedIdentityField(
        view_name='baiheuser-detail',
    )

    class Meta:
        model = Artical
        fields = '__all__'
        read_only_fields = ('author', 'author_detail',
                            'read_count', 'share_count')
