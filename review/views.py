from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer

class ReviewListView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True, context={'request': request})  # Pass request context
        return Response(serializer.data)
