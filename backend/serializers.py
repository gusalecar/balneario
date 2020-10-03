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
    carpa = CarpaSerializer(allow_null=True)
    sombrilla = SombrillaSerializer(allow_null=True)
    estacionamiento = EstacionamientoSerializer(allow_null=True)

    class Meta:
        model = ReservaDetalle
        fields = [ 'id', 'fecha_inicio', 'fecha_fin', 'carpa', 'sombrilla', 'estacionamiento' ]

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
        if attrs['carpa']:
            if reservado(carpa__numero=attrs['carpa']['numero']):
                errors['carpa'] = 'reservado'
            if not Carpa.objects.filter(numero=attrs['carpa']['numero']):
                errors['carpa'] = 'no existe'
        elif attrs['sombrilla']:
            if reservado(sombrilla__numero=attrs['sombrilla']['numero']):
                errors['sombrilla'] = 'reservado'
            if not Sombrilla.objects.filter(numero=attrs['sombrilla']['numero']):
                errors['sombrilla'] = 'no existe'
        elif attrs['estacionamiento']:
            if reservado(estacionamiento__numero=attrs['estacionamiento']['numero']):
                errors['estacionamiento'] = 'reservado'
            if not Estacionamiento.objects.filter(numero=attrs['estacionamiento']['numero']):
                errors['estacionamiento'] = 'no existe'
        else:
            errors['reservable'] = 'Debe haber por lo menos uno'
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
            carpa = detalle['carpa']
            carpa = Carpa.objects.get(numero=carpa['numero']) if carpa else None
            sombrilla = detalle['sombrilla']
            sombrilla = Sombrilla.objects.get(numero=sombrilla['numero']) if sombrilla else None
            est = detalle['estacionamiento']
            est = Estacionamiento.objects.get(numero=est['numero']) if est else None
            detalle = ReservaDetalle.objects.create(
                reserva=reserva,
                fecha_fin=detalle['fecha_fin'],
                fecha_inicio=detalle['fecha_inicio'],
                carpa=carpa,
                sombrilla=sombrilla,
                estacionamiento=est,
            )
        return reserva
