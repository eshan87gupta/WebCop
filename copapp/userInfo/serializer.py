from rest_framework import serializers
from ..models import UserInfo


class SerializerUserInfoAddress(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('phone_number', 'name', 'role')