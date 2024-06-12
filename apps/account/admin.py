from django.contrib import admin
from .models import *

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_editor')
    search_fields = ('username','first_name', 'last_name', 'email', 'is_staff', 'is_editor',)

admin.site.register(Account, AccountAdmin)