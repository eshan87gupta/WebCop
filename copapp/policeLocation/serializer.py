from rest_framework import serializers
from ..models import PoliceCoordinates


class SerializerPoliceAddress(serializers.ModelSerializer):
    class Meta:
        model = PoliceCoordinates
        fields = ('latitude', 'longitude', 'phone_number')