from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ContactMessageSerializer,ContactMessageSerializer2
from django.core.mail import send_mail
from django.conf import settings
import requests
from twilio.rest import Client 


class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            contact_message = serializer.save()

            # Send email
            subject = 'New Contact Form Submission'
            message = f"""
            Name: {contact_message.name}
            Email: {contact_message.email}
            Phone: {contact_message.phone}
            Service: {contact_message.service}
            Project Type: {contact_message.project_type}
            Message: {contact_message.message}
            """
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# for static files
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'


class ContactMessageView2(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer2(data=request.data)
        if serializer.is_valid():
            contact_message = serializer.save()

            # Send email
            subject = 'New Contact Form Submission'
            message = f"""
            Name: {contact_message.name}
            Email: {contact_message.email}
            Phone: {contact_message.phone}
            Service: {contact_message.service}
            Project Type: {contact_message.project_type}
            Message: {contact_message.message}
            """
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


