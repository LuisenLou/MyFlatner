from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'title'
            'description'
            'month_price'
            'room_class'
            'photos'
            'available'
            'available_date'
        ]
