from django.contrib import admin
from .models import *

# Register your models here.
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'flat', 'applicant', 'receiver', 'incident_status', 'incident_date')
    list_display_links = ('id', 'flat')
    list_filter = ('incident_status',)
    search_fields = ('flat__title', 'applicant__username', 'receiver__username')
    ordering = ('-incident_date',)
    list_per_page = 25

admin.site.register(Incident, IncidentAdmin)