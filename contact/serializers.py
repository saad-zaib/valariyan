from rest_framework import serializers
from .models import ContactMessage,ContactMessage2

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
class ContactMessageSerializer2(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage2
        fields = '__all__'
        