from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FactData
from .serializers import FactDataSerializer

class FactDataView(APIView):
    def get(self, request):
        fact_data = FactData.objects.first()
        if not fact_data:
            fact_data = FactData.objects.create()
        serializer = FactDataSerializer(fact_data)
        return Response(serializer.data)