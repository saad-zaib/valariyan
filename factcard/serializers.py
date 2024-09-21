from rest_framework import serializers
from .models import FactData

class FactDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactData
        fields = ['happy_clients', 'projects_completed', 'team_members', 'earned']