from rest_framework import serializers
from . import models

class CarpaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Carpa
        fields = [ 'numero' ]

class SombrillaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sombrilla
        fields = [ 'numero' ]

class EstacionamientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Estacionamiento
        fields = [ 'numero' ]

class ReservaDetalleSerializer(serializers.ModelSerializer):
    carpa = serializers.IntegerField(allow_null=True, source='carpa.numero')
    sombrilla = serializers.IntegerField(allow_null=True, source='sombrilla.numero')
    estacionamiento = serializers.IntegerField(allow_null=True, source='estacionamiento.numero')

    class Meta:
        model = models.ReservaDetalle
        fields = [ 'id', 'fecha_inicio', 'fecha_fin', 'carpa', 'sombrilla', 'estacionamiento' ]

    def create(self, validated_data):
        carpa = validated_data['carpa']['numero']
        sombrilla = validated_data['sombrilla']['numero']
        estacionamiento = validated_data['estacionamiento']['numero']

        carpa = models.Carpa.objects.get(numero=carpa) if carpa else None
        sombrilla = models.Sombrilla.objects.get(numero=sombrilla) if sombrilla else None
        estacionamiento = (
            models.Estacionamiento.objects.get(numero=estacionamiento) if estacionamiento else None
        )

        reservadetalle = models.ReservaDetalle.objects.create(
            carpa=carpa,
            sombrilla=sombrilla,
            estacionamiento=estacionamiento,
            fecha_fin=validated_data.pop('fecha_fin'),
            fecha_inicio=validated_data.pop('fecha_inicio'),
            reserva=self.context['reserva'],
        )
        return reservadetalle

class ReservaSerializer(serializers.ModelSerializer):
    reservadetalle_set = ReservaDetalleSerializer(many=True)
    fecha = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.Reserva
        fields = [ 'id', 'reservadetalle_set', 'fecha' ]

    def create(self, validated_data):
        reserva = models.Reserva.objects.create(usuario=self.context['user'])
        return reserva
