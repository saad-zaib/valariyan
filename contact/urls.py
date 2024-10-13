from django.urls import path
from .views import ContactMessageView,ContactMessageView2,IndexView  # Adjust according to your views

urlpatterns = [
    path('', ContactMessageView.as_view(), name='contact_message'),
    path('/2', ContactMessageView2.as_view(), name='contact_message2'),
    # Add more paths as needed
]