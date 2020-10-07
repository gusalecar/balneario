from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item, Reserva
from .serializers import ItemSerializer, ReservaSerializer

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

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        params = self.request.query_params
        if params.get('tipo'):
            queryset = queryset.filter(tipo=params['tipo'])
        if params.get('numero'):
            queryset = queryset.filter(numero=params['numero'])
        if params.get('habilitado').capitalize() in [ 'True', 'False' ]:
            queryset = queryset.filter(habilitado=params['habilitado'].capitalize())
        return queryset
