# facts/admin.py

from django.contrib import admin
from .models import FactData

@admin.register(FactData)
class FactDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'happy_clients', 'projects_completed', 'team_members', 'earned')
    list_editable = ('happy_clients', 'projects_completed', 'team_members', 'earned')

    def has_add_permission(self, request):
        # Prevent creating multiple FactData instances
        return not FactData.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deleting the FactData instance
        return False