from rest_framework import serializers
from .models import Carpa, Sombrilla, Estacionamiento, Reserva, ReservaDetalle

class CarpaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carpa
        fields = [ 'numero' ]

class SombrillaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sombrilla
        fields = [ 'numero' ]

class EstacionamientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estacionamiento
        fields = [ 'numero' ]

class ReservaDetalleSerializer(serializers.ModelSerializer):
    carpa = serializers.IntegerField(required=False, source='carpa.numero')
    sombrilla = serializers.IntegerField(required=False, source='sombrilla.numero')
    estacionamiento = serializers.IntegerField(required=False, source='estacionamiento.numero')

    class Meta:
        model = ReservaDetalle
        fields = [ 'id', 'fecha_inicio', 'fecha_fin', 'carpa', 'sombrilla', 'estacionamiento' ]

    def validate_carpa(self, value): # pylint: disable=R0201
        if Carpa.objects.filter(numero=value):
            return value
        raise serializers.ValidationError('No existe')

    def validate_sombrilla(self, value): # pylint: disable=R0201
        if Sombrilla.objects.filter(numero=value):
            return value
        raise serializers.ValidationError('No existe')

    def validate_estacionamiento(self, value): # pylint: disable=R0201
        if Estacionamiento.objects.filter(numero=value):
            return value
        raise serializers.ValidationError('No existe')

    def validate(self, attrs):
        def reservado(**res):
            return ReservaDetalle.objects.filter(
                **res,
                fecha_fin__lte=attrs['fecha_fin'],
                fecha_inicio__gte=attrs['fecha_inicio']
            ).first()

        errors = {}
        if attrs['fecha_inicio'] > attrs['fecha_fin']:
            errors['fecha'] = 'La fecha final no puede ser mayor a la inicial'

        attrs['carpa'] = attrs.get('carpa')
        attrs['sombrilla'] = attrs.get('sombrilla')
        attrs['estacionamiento'] = attrs.get('estacionamiento')

        if attrs['carpa']:
            if reservado(carpa__numero=attrs['carpa']['numero']):
                errors['carpa'] = 'reservado'
            attrs['carpa'] = Carpa.objects.get(numero=attrs['carpa']['numero'])
        elif attrs['sombrilla']:
            if reservado(sombrilla__numero=attrs['sombrilla']['numero']):
                errors['sombrilla'] = 'reservado'
            attrs['sombrilla'] = Sombrilla.objects.get(numero=attrs['sombrilla']['numero'])
        elif attrs['estacionamiento']:
            if reservado(estacionamiento__numero=attrs['estacionamiento']['numero']):
                errors['estacionamiento'] = 'reservado'
            attrs['estacionamiento'] = (
                Estacionamiento.objects.get(numero=attrs['estacionamiento']['numero'])
            )
        if errors:
            raise serializers.ValidationError(errors)
        return attrs

class ReservaSerializer(serializers.ModelSerializer):
    fecha = serializers.DateTimeField(read_only=True)
    detalles = ReservaDetalleSerializer(many=True)

    class Meta:
        model = Reserva
        fields = [ 'id', 'detalles', 'fecha' ]

    def create(self, validated_data):
        reserva = Reserva.objects.create(usuario=validated_data['usuario'])
        for detalle in validated_data['detalles']:
            detalle = ReservaDetalle.objects.create(
                reserva=reserva,
                fecha_fin=detalle['fecha_fin'],
                fecha_inicio=detalle['fecha_inicio'],
                carpa=detalle['carpa'],
                sombrilla=detalle['sombrilla'],
                estacionamiento=detalle['estacionamiento'],
            )
        return reserva
