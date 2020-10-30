from datetime import date
from rest_framework import serializers
from .models import Item, Precio, Reserva, ReservaDetalle, Transferencia

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [ 'numero', 'habilitado', 'tipo' ]

class ReservaDetalleSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = ReservaDetalle
        fields = [ 'id', 'fecha_inicio', 'fecha_fin', 'item', 'precio_unitario' ]
        read_only_fields = [ 'precio_unitario' ]

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
    estado = serializers.CharField(read_only=True)

    class Meta:
        model = Reserva
        fields = [ 'id', 'detalles', 'fecha', 'estado' ]

    def validate(self, attrs):
        datos = {}

        numeros = {}

        for detalle in attrs['detalles']:
            if not datos.get(detalle['item']['tipo']):
                datos[detalle['item']['tipo']] = [(
                    detalle['fecha_inicio'],
                    detalle['fecha_fin'],
                    detalle['item']['numero'],
                )]
                numeros[detalle['item']['tipo']] = [ detalle['item']['numero'] ]
            else:
                datos[detalle['item']['tipo']] += [(
                    detalle['fecha_inicio'],
                    detalle['fecha_fin'],
                    detalle['item']['numero'],
                )]
                numeros[detalle['item']['tipo']] += [ detalle['item']['numero'] ]

        for item, fechas in datos.items():
            for ini_nuevo, fin_nuevo, numero in fechas:
                if numeros[item].count(numero) > 1:
                    superpos = [
                        (x, y, z) for x, y, z in fechas if (
                            (x >= ini_nuevo) &
                            (y <= fin_nuevo) &
                            (z == numero)
                        )
                    ]
                    if len(superpos) > 1:
                        raise serializers.ValidationError({
                            'detalles': { item: f'Numero { numero } superpuesta' }
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
                precio_unitario=Precio.objects.get(item=detalle['item']['tipo']).valor,
            )
        return reserva

class TransferenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transferencia
        fields = '__all__'

    def validate_reserva(self, value):
        if (value.usuario == self.context['request'].user) & (value.estado == 'impago'):
            return value
        raise serializers.ValidationError('Reserva no valida')

    def create(self, validated_data):
        transferencia = Transferencia.objects.create(**validated_data)
        reserva = Reserva.objects.get(id=validated_data['reserva'].id)
        reserva.estado = 'procesando'
        reserva.save()
        return transferencia

class PrecioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Precio
        fields = '__all__'
