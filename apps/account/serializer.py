from djoser.serializers import UserCreateSerializer
from .models import *

from django.contrib.auth import get_user_model


Account = get_user_model()

class AccountSerializer(UserCreateSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'birth_date',
            'genre',
            'country',
            'province_or_state',
            'city',
            'ocupation',
            'profile_photo',
            'description',
            'role',
            'is_active',
            'is_staff',
            'is_editor',
        ]