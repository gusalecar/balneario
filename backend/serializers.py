from datetime import date
from rest_framework import serializers
from .models import Item, Reserva, ReservaDetalle

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [ 'numero', 'tipo' ]

class ReservaDetalleSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = ReservaDetalle
        fields = [ 'id', 'fecha_inicio', 'fecha_fin', 'item' ]

    def validate_item(self, value):
        if not Item.objects.filter(**value, habilitado=True):
            raise serializers.ValidationError({ value['tipo']: 'Inexistente o no disponible' })
        return value

    def validate(self, attrs):
        errors = {}
        if attrs['fecha_inicio'] < date.today():
            errors['fecha_inicio'] = 'Fecha inicial menor al dia de hoy'
        if attrs['fecha_inicio'] > attrs['fecha_fin']:
            errors['fecha'] = 'Fecha final menor a inicial'
        if ReservaDetalle.objects.filter(
                item__numero=attrs['item']['numero'],
                item__tipo=attrs['item']['tipo'],
                fecha_fin__lte=attrs['fecha_fin'],
                fecha_inicio__gte=attrs['fecha_inicio']
            ).first():
            errors[attrs['item']['tipo']] = 'Reservado'
        if errors:
            raise serializers.ValidationError(errors)
        return attrs

class ReservaSerializer(serializers.ModelSerializer):
    fecha = serializers.DateTimeField(read_only=True)
    detalles = ReservaDetalleSerializer(many=True)

    class Meta:
        model = Reserva
        fields = [ 'id', 'detalles', 'fecha' ]

    def validate(self, attrs):
        datos = {}
        for detalle in attrs['detalles']:
            if not datos.get(detalle['item']['tipo']):
                datos[detalle['item']['tipo']] = [(
                    detalle['fecha_inicio'], detalle['fecha_fin']
                )]
            else:
                datos[detalle['item']['tipo']] += [(
                    detalle['fecha_inicio'], detalle['fecha_fin']
                )]

        for item, fechas in datos.items():
            for ini_nuevo, fin_nuevo in fechas:
                superpos = [ (x, y) for x, y in fechas if (x >= ini_nuevo) & (y <= fin_nuevo) ]
                if len(superpos) > 1:
                    raise serializers.ValidationError({
                        'detalles': { item: 'Reservaciones superpuestas' }
                    })

        return attrs

    def create(self, validated_data):
        reserva = Reserva.objects.create(usuario=validated_data['usuario'])
        for detalle in validated_data['detalles']:
            ReservaDetalle.objects.create(
                reserva=reserva,
                fecha_fin=detalle['fecha_fin'],
                fecha_inicio=detalle['fecha_inicio'],
                item=Item.objects.get(**detalle['item']),
            )
        return reserva
