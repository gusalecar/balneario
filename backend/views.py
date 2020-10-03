from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers, models

class TestRequest(APIView):
    def get(self, request):
        return Response({
            "test": "data"
        })

class CarpaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Carpa.objects.all()
    serializer_class = serializers.CarpaSerializer
    lookup_field = 'numero'

class SombrillaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Sombrilla.objects.all()
    serializer_class = serializers.SombrillaSerializer
    lookup_field = 'numero'

class EstacionamientoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Estacionamiento.objects.all()
    serializer_class = serializers.EstacionamientoSerializer
    lookup_field = 'numero'

class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Reserva.objects.filter(usuario=self.request.user)

    def create(self, request):
        reserva = self.serializer_class(data=request.data)
        if reserva.is_valid():
            reserva.save(usuario=request.user)
            return Response({ 'success': True })
        return Response(reserva.errors, status.HTTP_400_BAD_REQUEST)
