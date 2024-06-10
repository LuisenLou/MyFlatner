from rest_framework import serializers
from models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id'
            'via_class'
            'via_name'
            'via_number'
            'floor'
            'door'
            'postal_code'
            'city'
            'province_or_state'
            'country'
        ]