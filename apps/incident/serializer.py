from rest_framework import serializers
from models import *


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = [
            'id',
            'title',
            'incident_status',
            'incident_date',
            'description',
        ]