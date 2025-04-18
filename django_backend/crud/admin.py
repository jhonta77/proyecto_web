from django.contrib import admin

from .models import task

@admin.register(task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_created', 'created')
    search_fields = ('title', 'description')
    list_filter = ('is_created', 'created')
    ordering = ('-created',)
