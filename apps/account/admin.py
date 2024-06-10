from django.contrib import admin
from .models import *

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'genre', 'country', 'role')
    list_display_links = ('username',)
    list_filter = ('role', 'ocupation', 'genre', 'country', 'city')
    search_fields = ('username', 'user__email', 'country', 'city')
    ordering = ('username',)
    list_per_page = 25

admin.site.register(Account, AccountAdmin)