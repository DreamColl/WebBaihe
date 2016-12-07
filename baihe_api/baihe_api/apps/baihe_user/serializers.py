from rest_framework import serializers

# from baihe_api.apps.artical.models import Artical

from .models import BaiheUser


class UserSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BaiheUser
        fields = ('id', 'username', 'nickname', 'articals', 'password')
        read_only_fields = ('articals',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        username = validated_data['username']
        nickname = validated_data['nickname']
        password = validated_data['password']
        user = BaiheUser.objects.create_user(username, nickname, password)
        user.save()
        return user
