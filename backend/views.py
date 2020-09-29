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
        serializer = self.serializer_class(data=request.data, context={ 'user': request.user })
        if serializer.is_valid():
            reserva = serializer.save()
            detalles = serializers.ReservaDetalleSerializer(
                data=request.data['reservadetalle_set'],
                many=True,
                context={ 'reserva': reserva }
            )
            if detalles.is_valid():
                detalles.save()
                return Response({ 'success': True })
            else:
                return Response(detalles.errors, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
