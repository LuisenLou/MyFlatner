from rest_framework import serializers
from .models import Contact_form

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_form
        fields = '__all__'