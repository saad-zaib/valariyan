from rest_framework import serializers
from .models import Project, Technology

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['name']

class ProjectSerializer(serializers.ModelSerializer):
    tech = TechnologySerializer(many=True, read_only=True)
    image = serializers.ImageField(use_url=True)
    pdf = serializers.FileField(use_url=True, required=False)

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'long_description',
            'tech',
            'github',
            'live',
            'image',
            'pdf',
        ]
