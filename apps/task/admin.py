from django.contrib import admin
from .models import *
# Register your models here.

class TaskAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'task_date', 'task_limit_date', 'assigned_to', 'flat')
    list_display_links = ('title',)
    list_per_page = 25
    list_filter = ('status', 'task_date', 'task_limit_date', 'assigned_to', 'flat')
    search_fields = ('title', 'assigned_to__username', 'flat__name')
    ordering = ('task_limit_date',)

admin.site.register(Task, TaskAdmin)

