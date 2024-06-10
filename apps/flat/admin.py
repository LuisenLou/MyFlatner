from django.contrib import admin
from .models import *
# Register your models here.

class FlatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'landlord', 'published', 'num_rooms', 'num_bathrooms', 'area', 'address', 'elevator','renovated')
    list_display_links = ('id', 'title')
    list_filter = ('published', 'num_rooms', 'num_bathrooms', 'area', 'landlord', 'elevator', 'renovated')
    search_fields = ('title', 'description', 'address__via_name', 'address__city', 'address__country')
    ordering = ('-published',)
    list_per_page = 25

admin.site.register(Flat, FlatAdmin)
