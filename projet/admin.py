from django.contrib import admin
from .models import Project, Technology

class TechnologyAdmin(admin.ModelAdmin):
    search_fields = ['name']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github', 'live')
    list_filter = ('tech',)
    search_fields = ('title', 'description', 'long_description')
    filter_horizontal = ('tech',)

admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Project, ProjectAdmin)
