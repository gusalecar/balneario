from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Reserva
from .serializers import ReservaSerializer

class TestRequest(APIView):
    def get(self, request):
        return Response({
            "test": "data"
        })

class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reserva.objects.filter(usuario=self.request.user)

    def create(self, request):
        reserva = self.serializer_class(data=request.data)
        if reserva.is_valid():
            reserva.save(usuario=request.user)
            return Response({ 'success': True })
        return Response(reserva.errors, status.HTTP_400_BAD_REQUEST)
