from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ContactMessageSerializer
from django.core.mail import send_mail
from django.conf import settings
import requests

class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            contact_message = serializer.save()
            
            # Send email (commented out for now)
            # subject = 'New Contact Form Submission'
            # message = f"""
            # Name: {contact_message.name}
            # Email: {contact_message.email}
            # Phone: {contact_message.phone}
            # Service: {contact_message.service}
            # Project Type: {contact_message.project_type}
            # Message: {contact_message.message}
            # """
            # send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
            
            # Send SMS (using Twilio as an example, commented out for now)
            # self.send_sms(message)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_sms(self, message):
        # Using Twilio as an example. You'll need to sign up for a Twilio account.
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        try:
            client.messages.create(
                body=message,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=settings.ADMIN_PHONE_NUMBER
            )
        except Exception as e:
            print(f"Failed to send SMS: {str(e)}")



# for static files
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
