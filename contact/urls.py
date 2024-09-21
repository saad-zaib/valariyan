from django.urls import path
from .views import ContactMessageView,IndexView  # Adjust according to your views

urlpatterns = [
    path('', ContactMessageView.as_view(), name='contact_message'),
    # Add more paths as needed
]
