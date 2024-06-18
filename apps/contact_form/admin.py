from django.contrib import admin
from .models import Contact_form
# Register your models here.


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'reason', 'reason', 'first_name', 'last_name', 'email', 'country', 'city', 'region','via', 'address_name', 'postal_code', 'created_at', 'ip_address')
    list_display_links = ('id', 'reason')
    list_filter = ('reason', 'country', 'created_at')
    search_fields = ('reason', 'first_name', 'last_name', 'email', 'country', 'city', 'region', 'via', 'address_name')
    ordering = ('-created_at',)
    list_per_page = 25

admin.site.register(Contact_form, ContactFormAdmin)