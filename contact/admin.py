from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service', 'project_type', 'created_at')
    list_filter = ('service', 'project_type', 'created_at')
    search_fields = ('name', 'email', 'phone', 'service', 'project_type', 'message')
    ordering = ('-created_at',)

    def __str__(self):
        return self.name
