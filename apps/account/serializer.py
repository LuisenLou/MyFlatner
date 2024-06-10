from rest_framework import serializers
from models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id'
            'username'
            'birth_date'
            'genre'
            'country'
            'province_or_state'
            'city'
            'ocupation'
            'profile_photo'
            'description'
            'role'
        ]