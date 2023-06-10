from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import FriendRequest


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username']


class ChatSerializer(serializers.Serializer):
    pass


class FriendRequestSerializer(serializers.ModelSerializer):
    first_user_detail = UserSerializer(read_only=True, source='first_user')
    second_user_detail = UserSerializer(read_only=True, source='second_user')

    class Meta:
        model = FriendRequest
        fields = ['id', 'first_user', 'second_user', 'first_user_detail', 'second_user_detail', 'is_active',
                  'is_accepted']
        extra_kwargs = {
            'first_user': {'write_only': True},
            'second_user': {'write_only': True}
        }
