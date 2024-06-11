from django.contrib import admin
from .models import Contact_form
# Register your models here.


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'form_class', 'first_name', 'last_name', 'email', 'country', 'city', 'region', 'street', 'postal_code', 'created_at', 'ip_address')
    list_display_links = ('id', 'title')
    list_filter = ('form_class', 'country', 'created_at')
    search_fields = ('title', 'first_name', 'last_name', 'email', 'country', 'city', 'region', 'street')
    ordering = ('-created_at',)
    list_per_page = 25

admin.site.register(Contact_form, ContactFormAdmin)