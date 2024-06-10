from rest_framework import serializers
from models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'status',
            'task_date',
            'task_limit_date',
        ]