from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item, Precio, Reserva, Transferencia
from .serializers import (
    ItemSerializer, PrecioSerializer, ReservaSerializer, TransferenciaSerializer
)

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
            context = { 'reserva': request.data }
            context['reserva']['id'] = reserva.data['id']
            send_mail(
                'Comprobante de reserva',
                '',
                'from@example.com',
                [request.user.email],
                fail_silently=False,
                html_message=render_to_string(
                    'mailreserva.html',
                    context=context,
                    request=request,
                )
            )
            return Response(reserva.data)
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
        if params.get('habilitado'):
            if params['habilitado'].capitalize() in [ 'True', 'False' ]:
                queryset = queryset.filter(habilitado=params['habilitado'].capitalize())
        if (params.get('fechainicio') is not None) & (params.get('fechafin') is not None):
            queryset = queryset.filter(
                detalles__fecha_fin__lte=params['fechafin'],
                detalles__fecha_inicio__gte=params['fechainicio']
            )
        return queryset

class TransferenciaViewSet(viewsets.ModelViewSet):
    serializer_class = TransferenciaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transferencia.objects.filter(
            reserva__usuario=self.request.user
        )

class PrecioViewSet(viewsets.ModelViewSet):
    serializer_class = PrecioSerializer
    queryset = Precio.objects.all()
    lookup_field = 'item'

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
