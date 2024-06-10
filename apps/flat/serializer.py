from rest_framework import serializers
from models import *


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id'
            'title'
            'description'
            'published'
            'num_rooms'
            'num_bathrooms'
            'area'
            'renovated'
            'elevator'
            'latitude'
            'longitude'
            'photos'
            'views'
        ]