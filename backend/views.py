from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models import Q
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from mercadopago import MP
from .models import Item, Precio, Reserva, ReservaDetalle, Transferencia
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
                Q(detalles__fecha_inicio__range=(params['fechainicio'], params['fechafin'])) |
                Q(detalles__fecha_fin__range=(params['fechainicio'], params['fechafin'])) |
                Q(
                    detalles__fecha_inicio__lt=params['fechainicio'],
                    detalles__fecha_fin__gt=params['fechafin']
                )
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

class PagoRequest(APIView):
    def get(self, request):
        id = request.query_params['id']
        detalles = list(ReservaDetalle.objects.filter(reserva__id=int(id)))
        precio_total = sum(det.precio_unitario for det in detalles)
        mp = MP(settings.MP_TOKEN)
        res = mp.create_preference({
            "items": [
                {
                    "title": "Total",
                    "quantity": 1,
                    "currency_id": "ARS",
                    "unit_price": precio_total
                }
            ]
        })
        return Response({ 'pref_id': res['response']['id'] })
