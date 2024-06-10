from django.contrib import admin
from .models import *
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'flat', 'tenant', 'month_price', 'available', 'available_date')
    list_display_links = ('id', 'title')
    list_filter = ('flat', 'tenant', 'available')
    search_fields = ('title', 'description', 'room_class')
    ordering = ('-available_date',)
    list_per_page = 25

admin.site.register(Room, RoomAdmin)