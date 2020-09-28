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

    class Meta:
        model = models.ReservaDetalle
        fields = [ 'fecha_inicio', 'fecha_fin', 'carpa', 'sombrilla', 'estacionamiento' ]

class ReservaSerializer(serializers.ModelSerializer):
    reservadetalle_set = ReservaDetalleSerializer(many=True)

    class Meta:
        model = models.Reserva
        fields = [ 'id', 'reservadetalle_set', 'fecha', 'usuario' ]
