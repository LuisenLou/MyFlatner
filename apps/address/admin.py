from django.contrib import admin
from .models import *

# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'via_class', 'via_name', 'via_number', 'floor', 'door', 'postal_code', 'city', 'state', 'country')
    list_display_links = ('id', 'via_name')
    list_filter = ('via_class', 'city', 'state', 'country')
    search_fields = ('via_name', 'city', 'state', 'country')
    ordering = ('id',)
    list_per_page = 25

admin.site.register(Address, AddressAdmin)