from rest_framework import serializers
from ..models import VictimCoordinates


class SerializerVictimAddress(serializers.ModelSerializer):
    class Meta:
        model = VictimCoordinates
        fields = ('latitude', 'longitude', 'phone_number')