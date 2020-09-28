from rest_framework import viewsets
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

class ReservaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Reserva.objects.all()
    serializer_class = serializers.ReservaSerializer
