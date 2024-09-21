from django.urls import path
from .views import FactDataView  # Adjust according to your views

urlpatterns = [
    path('', FactDataView.as_view(), name='fact_message'),
    # Add more paths as needed
]
