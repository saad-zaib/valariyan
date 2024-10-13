from django.contrib import admin
from .models import ContactMessage,ContactMessage2

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service', 'subService','project_type', 'created_at')
    list_filter = ('service', 'project_type', 'created_at')
    search_fields = ('name', 'email', 'phone', 'service', 'project_type', 'message')
    ordering = ('-created_at',)

    def __str__(self):
        return self.name
@admin.register(ContactMessage2)
class ContactMessageAdmin2(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at' )
    list_filter = ( 'name','subject','email','created_at')
    search_fields = ('name', 'email','message')
    ordering = ('-created_at',)

    def __str__(self):
        return self.name
