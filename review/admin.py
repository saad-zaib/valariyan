from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'content', 'avatar')
    search_fields = ('name', 'role')
    ordering = ('name',)
    list_filter = ('role',)

    # Optional: If you want to display the content in a more readable way
    def content_preview(self, obj):
        return obj.content[:50]  # Show the first 50 characters

    content_preview.short_description = 'Content Preview'

    # If you want to show the content preview in the admin list view
    list_display = ('name', 'role', 'content_preview', 'avatar')

