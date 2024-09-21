from rest_framework import serializers
from .models import Review
from django.urls import reverse

class ReviewSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['name', 'role', 'content', 'avatar']

    def get_avatar(self, obj):
        # Construct and return the full URL for the avatar image
        request = self.context.get('request')
        return request.build_absolute_uri(obj.avatar.url) if obj.avatar else None
